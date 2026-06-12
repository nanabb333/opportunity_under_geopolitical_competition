#!/usr/bin/env python3
"""Build market return and event-study files for the portfolio sample."""

from __future__ import annotations

import csv
import hashlib
import http.cookiejar
import io
import re
import ssl
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
EVENTS = DATA_DIR / "events.csv"
ASSETS = DATA_DIR / "assets.csv"
LINKS = DATA_DIR / "event_asset_links.csv"
LOCAL_PRICE_DIR = DATA_DIR / "raw_prices"
MARKET_RETURNS_OUT = DATA_DIR / "market_returns.csv"
EVENT_RETURNS_OUT = DATA_DIR / "event_firm_returns.csv"
REPORT_OUT = DATA_DIR / "data_validation_report.md"
LOCAL_REPORT_OUT = DATA_DIR / "local_price_validation_report.md"
FIRST_RESULTS_MEMO_OUT = DATA_DIR / "first_results_memo.md"

CORE_EVENT_ASSET_PAIRS = {
    ("E009", "A005"),
    ("E010", "A006"),
    ("E012", "A007"),
}
LOCAL_BENCHMARK_ASSET_IDS = {"A001", "A002", "A003"}


TICKER_MAP = {
    "SOX": "^SOX",
    "SMSN": "005930.KS",
}

STOOQ_MAP = {
    "SPY": "spy.us",
    "QQQ": "qqq.us",
    "SMH": "smh.us",
    "SOX": "sox.us",
    "INTC": "intc.us",
    "TSM": "tsm.us",
    "MU": "mu.us",
    "SMSN": "005930.kr",
    "NVDA": "nvda.us",
    "AMD": "amd.us",
    "ASML": "asml.us",
    "AMAT": "amat.us",
    "LRCX": "lrcx.us",
    "KLAC": "klac.us",
    "BAESY": "baesy.us",
    "SONY": "sony.us",
    "TM": "tm.us",
    "KWEB": "kweb.us",
    "CQQQ": "cqqq.us",
}

STOOQ_SSL_CONTEXT = ssl._create_unverified_context()
STOOQ_COOKIE_JAR = http.cookiejar.CookieJar()
STOOQ_OPENER = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=STOOQ_SSL_CONTEXT),
    urllib.request.HTTPCookieProcessor(STOOQ_COOKIE_JAR),
)


@dataclass(frozen=True)
class WindowResult:
    t0: pd.Timestamp | None
    event_day_return: float | None
    ar_market_event_day: float | None
    ar_tech_event_day: float | None
    ar_sector_event_day: float | None
    car_market_m1_p1: float | None
    car_tech_m1_p1: float | None
    car_sector_m1_p1: float | None
    car_market_m3_p3: float | None
    car_sector_m3_p3: float | None
    car_market_m7_p7: float | None
    car_sector_m7_p7: float | None
    event_window_coverage: str
    data_quality_flag: str
    notes: str


def read_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    events = pd.read_csv(EVENTS, dtype=str)
    assets = pd.read_csv(ASSETS, dtype=str)
    links = pd.read_csv(LINKS, dtype=str)
    for col in ["primary_test_eligible", "geopolitical_competition_link", "strategic_importance",
                "state_support", "support_directness", "support_credibility", "threat_signal",
                "opportunity_signal", "substitution_reallocation", "confound_flag_event"]:
        if col in events.columns:
            events[col] = pd.to_numeric(events[col], errors="coerce")
    for col in ["strategic_asset", "public_market_available"]:
        if col in assets.columns:
            assets[col] = pd.to_numeric(assets[col], errors="coerce")
    for col in ["primary_beneficiary", "link_strength"]:
        if col in links.columns:
            links[col] = pd.to_numeric(links[col], errors="coerce")
    return events, assets, links


def validate_inputs(events: pd.DataFrame, assets: pd.DataFrame, links: pd.DataFrame) -> list[str]:
    issues: list[str] = []
    if not events["event_id"].is_unique:
        issues.append("events.csv has duplicate event_id values.")
    if not assets["asset_id"].is_unique:
        issues.append("assets.csv has duplicate asset_id values.")
    missing_events = sorted(set(links["event_id"]) - set(events["event_id"]))
    missing_assets = sorted(set(links["asset_id"]) - set(assets["asset_id"]))
    if missing_events:
        issues.append(f"event_asset_links.csv references missing events: {missing_events}")
    if missing_assets:
        issues.append(f"event_asset_links.csv references missing assets: {missing_assets}")
    return issues


def select_core_local_inputs(
    events: pd.DataFrame,
    assets: pd.DataFrame,
    links: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, set[str]]:
    core_events = events.loc[events["primary_test_eligible"] == 1].copy()
    core_links = links.loc[
        links.apply(lambda row: (row["event_id"], row["asset_id"]) in CORE_EVENT_ASSET_PAIRS, axis=1)
    ].copy()
    required_asset_ids = set(core_links["asset_id"]) | LOCAL_BENCHMARK_ASSET_IDS
    core_assets = assets.loc[assets["asset_id"].isin(required_asset_ids)].copy()
    return core_events, core_assets, core_links, required_asset_ids


def format_price_frame(
    data: pd.DataFrame,
    asset_id: str,
    ticker: str,
    source_ticker: str,
    source: str,
    prefer_adj_close: bool = False,
) -> pd.DataFrame:
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [c[0] for c in data.columns]
    if prefer_adj_close and "Adj Close" in data.columns:
        close_col = "Adj Close"
    else:
        close_col = "Close" if "Close" in data.columns else "Adj Close"
    if close_col not in data.columns:
        raise ValueError("no close column")
    if "trade_date" in data.columns:
        tmp = data[["trade_date", close_col]].rename(columns={close_col: "close_price_adjusted"})
    elif "Date" in data.columns:
        tmp = data[["Date", close_col]].rename(columns={"Date": "trade_date", close_col: "close_price_adjusted"})
    else:
        tmp = data[[close_col]].rename(columns={close_col: "close_price_adjusted"}).reset_index()
        tmp = tmp.rename(columns={tmp.columns[0]: "trade_date"})
    tmp["trade_date"] = pd.to_datetime(tmp["trade_date"]).dt.date.astype(str)
    tmp["close_price_adjusted"] = pd.to_numeric(tmp["close_price_adjusted"], errors="coerce")
    tmp = tmp.dropna(subset=["trade_date", "close_price_adjusted"])
    tmp = tmp.drop_duplicates(subset=["trade_date"], keep="last")
    tmp = tmp.sort_values("trade_date").reset_index(drop=True)
    tmp["asset_id"] = asset_id
    tmp["ticker"] = ticker
    tmp["yf_ticker"] = source_ticker
    tmp["daily_return"] = tmp["close_price_adjusted"].pct_change()
    tmp["data_source"] = source
    tmp["trading_calendar_notes"] = ""
    return tmp[[
        "asset_id", "ticker", "yf_ticker", "trade_date", "close_price_adjusted",
        "daily_return", "data_source", "trading_calendar_notes"
    ]]


def read_local_price_file(asset: pd.Series) -> tuple[pd.DataFrame | None, str | None]:
    ticker = str(asset["ticker"])
    path = LOCAL_PRICE_DIR / f"{ticker}.csv"
    if not path.exists():
        return None, f"{ticker}.csv not found"
    try:
        data = pd.read_csv(path)
    except Exception as exc:  # noqa: BLE001
        return None, f"{ticker}.csv read error: {exc}"
    if "Date" not in data.columns:
        return None, f"{ticker}.csv missing Date column"
    if "Adj Close" not in data.columns and "Close" not in data.columns:
        return None, f"{ticker}.csv missing Adj Close/Close column"
    data = data.rename(columns={"Date": "trade_date"})
    try:
        prices = format_price_frame(
            data,
            str(asset["asset_id"]),
            ticker,
            ticker,
            "local_csv",
            prefer_adj_close=True,
        )
    except Exception as exc:  # noqa: BLE001
        return None, f"{ticker}.csv parse error: {exc}"
    if prices.empty:
        return None, f"{ticker}.csv produced zero valid price rows"
    return prices, None


def load_local_prices(assets: pd.DataFrame) -> tuple[pd.DataFrame, list[str], list[str], list[str]]:
    frames: list[pd.DataFrame] = []
    found: list[str] = []
    missing: list[str] = []
    issues: list[str] = []
    for asset in assets.sort_values("asset_id").itertuples(index=False):
        asset_series = pd.Series(asset._asdict())
        prices, issue = read_local_price_file(asset_series)
        label = f"{asset.asset_id} {asset.ticker}"
        if prices is None:
            missing.append(label)
            if issue:
                issues.append(f"{label}: {issue}")
            continue
        frames.append(prices)
        found.append(f"{label}: {len(prices)} rows")
    if frames:
        out = pd.concat(frames, ignore_index=True)
    else:
        out = pd.DataFrame(columns=[
            "asset_id", "ticker", "yf_ticker", "trade_date", "close_price_adjusted",
            "daily_return", "data_source", "trading_calendar_notes"
        ])
    return out, found, missing, issues


def download_stooq(
    asset_id: str,
    ticker: str,
    start: str,
    end: str,
) -> pd.DataFrame:
    stooq_ticker = STOOQ_MAP.get(ticker)
    if not stooq_ticker:
        raise ValueError("no Stooq ticker mapping")
    d1 = start.replace("-", "")
    d2 = end.replace("-", "")
    url = f"https://stooq.com/q/d/l/?s={stooq_ticker}&d1={d1}&d2={d2}&i=d"
    raw = fetch_stooq_url(url)
    if "Access denied" in raw:
        raise ValueError("access denied by Stooq")
    if raw.lstrip().startswith("<!DOCTYPE") or raw.lstrip().startswith("<html"):
        raise ValueError("non-CSV HTML response from Stooq")
    data = pd.read_csv(io.StringIO(raw))
    if data.empty or "No data" in data.columns:
        raise ValueError("no rows returned")
    data = data.rename(columns={"Date": "trade_date"})
    return format_price_frame(data, asset_id, ticker, stooq_ticker, "stooq")


def fetch_stooq_url(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = STOOQ_OPENER.open(request, timeout=30)
    raw = response.read().decode("utf-8")
    if "/__verify" not in raw:
        return raw

    challenge = re.search(r'c="([^"]+)".*?d=(\d+)', raw, flags=re.S)
    if not challenge:
        raise ValueError("Stooq verification challenge could not be parsed")
    token = challenge.group(1)
    difficulty = int(challenge.group(2))
    prefix = "0" * difficulty
    nonce = 0
    while True:
        digest = hashlib.sha256(f"{token}{nonce}".encode("utf-8")).hexdigest()
        if digest.startswith(prefix):
            break
        nonce += 1

    verify_body = urllib.parse.urlencode({"c": token, "n": str(nonce)}).encode("utf-8")
    verify_request = urllib.request.Request(
        "https://stooq.com/__verify",
        data=verify_body,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )
    STOOQ_OPENER.open(verify_request, timeout=30).read()
    retry = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with STOOQ_OPENER.open(retry, timeout=30) as retry_response:
        return retry_response.read().decode("utf-8")


def download_yfinance(
    asset_id: str,
    ticker: str,
    yf_ticker: str,
    start: str,
    end: str,
) -> pd.DataFrame:
    data = yf.download(
        yf_ticker,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
        threads=False,
    )
    if data.empty:
        raise ValueError("no rows returned")
    return format_price_frame(data, asset_id, ticker, yf_ticker, "yfinance")


def download_prices(assets: pd.DataFrame, events: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    event_dates = pd.to_datetime(events["event_date"])
    start = (event_dates.min() - pd.Timedelta(days=45)).date().isoformat()
    end = (event_dates.max() + pd.Timedelta(days=45)).date().isoformat()
    download_assets = assets[
        (assets["public_market_available"].astype(str) == "1")
        & (assets["data_feasibility"].isin(["available", "conditional", "optional"]))
    ].copy()
    download_assets["yf_ticker"] = download_assets["ticker"].map(TICKER_MAP).fillna(download_assets["ticker"])

    frames: list[pd.DataFrame] = []
    failures: list[str] = []
    for row in download_assets.itertuples(index=False):
        asset_id = row.asset_id
        ticker = row.ticker
        yf_ticker = row.yf_ticker
        errors: list[str] = []
        try:
            frames.append(download_stooq(asset_id, ticker, start, end))
            continue
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Stooq: {exc}")
        try:
            frames.append(download_yfinance(asset_id, ticker, yf_ticker, start, end))
            continue
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Yahoo Finance: {exc}")
        failures.append(f"{asset_id} {ticker} ({yf_ticker}): " + " | ".join(errors))
    if frames:
        prices = pd.concat(frames, ignore_index=True)
    else:
        prices = pd.DataFrame(columns=[
            "asset_id", "ticker", "yf_ticker", "trade_date", "close_price_adjusted",
            "daily_return", "data_source", "trading_calendar_notes"
        ])
    return prices, failures


def trading_calendar_for_asset(prices: pd.DataFrame, asset_id: str) -> pd.DataFrame:
    out = prices.loc[prices["asset_id"] == asset_id].copy()
    out["trade_ts"] = pd.to_datetime(out["trade_date"])
    return out.sort_values("trade_ts").reset_index(drop=True)


def choose_t0(asset_prices: pd.DataFrame, event_date: pd.Timestamp, force_next_day: bool) -> tuple[int | None, str]:
    if asset_prices.empty:
        return None, "no price data"
    dates = asset_prices["trade_ts"]
    if force_next_day:
        candidates = asset_prices.index[dates > event_date]
        note = "foreign/conditional timing: first trading day after event date"
    else:
        candidates = asset_prices.index[dates >= event_date]
        note = "first trading day on or after event date"
    if len(candidates) == 0:
        return None, "no trading day on/after event date"
    return int(candidates[0]), note


def sum_window(asset_prices: pd.DataFrame, t0_idx: int, lo: int, hi: int) -> tuple[float | None, bool]:
    start = t0_idx + lo
    end = t0_idx + hi
    if start < 0 or end >= len(asset_prices):
        return None, False
    vals = asset_prices.loc[start:end, "daily_return"]
    if vals.isna().any():
        return None, False
    return float(vals.sum()), True


def compute_for_link(
    event: pd.Series,
    asset: pd.Series,
    prices_by_asset: dict[str, pd.DataFrame],
    sector_benchmark: str = "A003",
    market_benchmark: str = "A001",
    tech_benchmark: str = "A002",
) -> WindowResult:
    asset_id = str(asset.get("asset_id", asset.name))
    event_date = pd.to_datetime(event["event_date"])
    asset_prices = prices_by_asset.get(asset_id, pd.DataFrame())
    force_next = asset.get("data_feasibility") == "conditional" and asset.get("listing_region") not in ["US", "US_ADR"]
    t0_idx, t0_note = choose_t0(asset_prices, event_date, force_next)
    if t0_idx is None:
        return WindowResult(None, None, None, None, None, None, None, None, None, None, None, None, "none", "missing", t0_note)

    t0_date = asset_prices.loc[t0_idx, "trade_ts"]
    event_day = asset_prices.loc[t0_idx, "daily_return"]
    coverage_notes = []
    if pd.isna(event_day):
        coverage_notes.append("event-day return missing")

    market_prices = prices_by_asset.get(market_benchmark, pd.DataFrame())
    tech_prices = prices_by_asset.get(tech_benchmark, pd.DataFrame())
    sector_prices = prices_by_asset.get(sector_benchmark, pd.DataFrame())

    def benchmark_return(bench_prices: pd.DataFrame, target_date: pd.Timestamp) -> float | None:
        if bench_prices.empty:
            return None
        hit = bench_prices.loc[bench_prices["trade_ts"] == target_date, "daily_return"]
        if hit.empty or pd.isna(hit.iloc[0]):
            return None
        return float(hit.iloc[0])

    def car_adjusted(lo: int, hi: int, bench_asset: str) -> tuple[float | None, bool]:
        raw, ok = sum_window(asset_prices, t0_idx, lo, hi)
        bench = prices_by_asset.get(bench_asset, pd.DataFrame())
        if raw is None or bench.empty:
            return None, False
        dates = asset_prices.loc[t0_idx + lo:t0_idx + hi, "trade_ts"]
        bench_vals = []
        for d in dates:
            br = benchmark_return(bench, d)
            if br is None:
                return None, False
            bench_vals.append(br)
        return float(raw - sum(bench_vals)), ok

    market_event = benchmark_return(market_prices, t0_date)
    tech_event = benchmark_return(tech_prices, t0_date)
    sector_event = benchmark_return(sector_prices, t0_date)
    event_day_float = None if pd.isna(event_day) else float(event_day)
    ar_market_event_day = None if event_day_float is None or market_event is None else event_day_float - market_event
    ar_tech_event_day = None if event_day_float is None or tech_event is None else event_day_float - tech_event
    ar_sector_event_day = None if event_day_float is None or sector_event is None else event_day_float - sector_event

    car_market_m1_p1, ok_m1 = car_adjusted(-1, 1, market_benchmark)
    car_tech_m1_p1, ok_t1 = car_adjusted(-1, 1, tech_benchmark)
    car_sector_m1_p1, ok_s1 = car_adjusted(-1, 1, sector_benchmark)
    car_market_m3_p3, ok_m3 = car_adjusted(-3, 3, market_benchmark)
    car_sector_m3_p3, ok_s3 = car_adjusted(-3, 3, sector_benchmark)
    car_market_m7_p7, ok_m7 = car_adjusted(-7, 7, market_benchmark)
    car_sector_m7_p7, ok_s7 = car_adjusted(-7, 7, sector_benchmark)

    if ok_s1 and ok_m1:
        quality = "clean"
    elif event_day_float is not None:
        quality = "caution"
    else:
        quality = "weak"
    if event.get("confound_flag_event", 0) == 1:
        quality = "caution"

    coverage = []
    for label, ok in [
        ("m1p1_market", ok_m1), ("m1p1_sector", ok_s1),
        ("m1p1_tech", ok_t1),
        ("m3p3_market", ok_m3), ("m3p3_sector", ok_s3),
        ("m7p7_market", ok_m7), ("m7p7_sector", ok_s7),
    ]:
        if not ok:
            coverage.append(f"{label}:missing")
    if not coverage:
        coverage.append("all requested windows covered")
    note = f"t0={t0_date.date()}; {t0_note}"
    return WindowResult(
        t0_date,
        event_day_float,
        ar_market_event_day,
        ar_tech_event_day,
        ar_sector_event_day,
        car_market_m1_p1,
        car_tech_m1_p1,
        car_sector_m1_p1,
        car_market_m3_p3,
        car_sector_m3_p3,
        car_market_m7_p7,
        car_sector_m7_p7,
        "; ".join(coverage),
        quality,
        note,
    )


def build_event_returns(events: pd.DataFrame, assets: pd.DataFrame, links: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    prices_by_asset = {asset_id: trading_calendar_for_asset(prices, asset_id) for asset_id in prices["asset_id"].unique()}
    event_map = events.set_index("event_id")
    asset_map = assets.set_index("asset_id")
    rows: list[dict[str, object]] = []
    for link in links.itertuples(index=False):
        event = event_map.loc[link.event_id]
        asset = asset_map.loc[link.asset_id]
        result = compute_for_link(event, asset, prices_by_asset)
        rows.append({
            "event_id": link.event_id,
            "asset_id": link.asset_id,
            "exposure_role": link.exposure_role,
            "primary_beneficiary": link.primary_beneficiary,
            "analysis_role": link.analysis_role,
            "expected_direction": link.expected_direction,
            "event_t0_trade_date": None if result.t0 is None else result.t0.date().isoformat(),
            "event_day_return": result.event_day_return,
            "ar_market_event_day": result.ar_market_event_day,
            "ar_tech_event_day": result.ar_tech_event_day,
            "ar_sector_event_day": result.ar_sector_event_day,
            "car_market_m1_p1": result.car_market_m1_p1,
            "car_tech_m1_p1": result.car_tech_m1_p1,
            "car_sector_m1_p1": result.car_sector_m1_p1,
            "car_market_m3_p3": result.car_market_m3_p3,
            "car_sector_m3_p3": result.car_sector_m3_p3,
            "car_market_m7_p7": result.car_market_m7_p7,
            "car_sector_m7_p7": result.car_sector_m7_p7,
            "earnings_conflict": "",
            "macro_conflict": "",
            "event_window_coverage": result.event_window_coverage,
            "data_quality_flag": result.data_quality_flag,
            "calculation_notes": result.notes,
        })
    return pd.DataFrame(rows)


def write_report(
    events: pd.DataFrame,
    assets: pd.DataFrame,
    links: pd.DataFrame,
    prices: pd.DataFrame,
    returns: pd.DataFrame,
    schema_issues: list[str],
    download_failures: list[str],
) -> None:
    linked_assets = sorted(links["asset_id"].unique())
    downloaded_assets = sorted(prices["asset_id"].unique())
    missing_linked = sorted(set(linked_assets) - set(downloaded_assets))
    conditional_assets = assets.loc[assets["data_feasibility"] == "conditional", ["asset_id", "ticker", "asset_name"]]
    weak_rows = returns.loc[returns["data_quality_flag"].isin(["missing", "weak"])]
    coverage_issues = returns.loc[returns["event_window_coverage"] != "all requested windows covered"]

    lines = [
        "# Data Validation Report",
        "",
        "## Scope",
        "",
        "This report validates market data construction only. It does not interpret results.",
        "",
        "## Input Counts",
        "",
        f"- events.csv rows: {len(events)}",
        f"- assets.csv rows: {len(assets)}",
        f"- event_asset_links.csv rows: {len(links)}",
        f"- market_returns.csv rows: {len(prices)}",
        f"- event_firm_returns.csv rows: {len(returns)}",
        "",
        "## Schema and Key Validation",
        "",
    ]
    if schema_issues:
        lines.extend([f"- {issue}" for issue in schema_issues])
    else:
        lines.append("- No schema/key integrity issues detected before return construction.")
    lines.extend(["", "## Download Failures", ""])
    if download_failures:
        lines.extend([f"- {failure}" for failure in download_failures])
    else:
        lines.append("- No ticker download failures reported by the pipeline.")
    lines.extend(["", "## Linked Assets Without Downloaded Price Data", ""])
    if missing_linked:
        for asset_id in missing_linked:
            row = assets.loc[assets["asset_id"] == asset_id].iloc[0]
            lines.append(f"- {asset_id} {row['ticker']} ({row['asset_name']})")
    else:
        lines.append("- All linked assets have downloaded price data.")
    lines.extend(["", "## Conditional Assets", ""])
    if not conditional_assets.empty:
        for row in conditional_assets.itertuples(index=False):
            lines.append(f"- {row.asset_id} {row.ticker}: {row.asset_name}")
        lines.append("")
        lines.append("Conditional assets are retained when price data are available, but they are not automatically clean primary-test observations.")
    else:
        lines.append("- No conditional assets in assets.csv.")
    lines.extend(["", "## Event-Window Coverage Issues", ""])
    if not coverage_issues.empty:
        for row in coverage_issues.itertuples(index=False):
            lines.append(f"- {row.event_id}/{row.asset_id}: {row.event_window_coverage}; {row.calculation_notes}")
    else:
        lines.append("- All event-asset rows have requested event-window coverage.")
    lines.extend(["", "## Weak or Missing Event-Firm Rows", ""])
    if not weak_rows.empty:
        for row in weak_rows.itertuples(index=False):
            lines.append(f"- {row.event_id}/{row.asset_id}: {row.data_quality_flag}; {row.calculation_notes}")
    else:
        lines.append("- No rows flagged weak or missing.")
    lines.extend(["", "## Post-Freeze Issues", ""])
    lines.append("- Added requested schema fields only: primary_test_eligible and primary_beneficiary.")
    lines.append("- No theory, sample-logic, or event-universe changes were made by the return pipeline.")
    lines.append("- Samsung remains conditional; the pipeline maps SMSN to 005930.KS and uses the first local trading day after the event date for conditional non-US listings.")
    REPORT_OUT.write_text("\n".join(lines) + "\n")


def write_local_price_report(
    events: pd.DataFrame,
    assets: pd.DataFrame,
    links: pd.DataFrame,
    prices: pd.DataFrame,
    returns: pd.DataFrame,
    schema_issues: list[str],
    found_files: list[str],
    missing_files: list[str],
    local_issues: list[str],
) -> None:
    covered_rows = returns.loc[returns["car_sector_m1_p1"].notna()]
    missing_rows = returns.loc[returns["car_sector_m1_p1"].isna()]
    coverage_issues = returns.loc[returns["event_window_coverage"] != "all requested windows covered"]

    lines = [
        "# Local Price Validation Report",
        "",
        "## Scope",
        "",
        "This report validates the local manually downloaded price-data pathway only. It does not interpret returns.",
        "",
        "## Local Price Directory",
        "",
        f"- Expected directory: {LOCAL_PRICE_DIR}",
        "",
        "## Frozen Core Rows Re-Run",
        "",
    ]
    for row in links.itertuples(index=False):
        event = events.loc[events["event_id"] == row.event_id].iloc[0]
        asset = assets.loc[assets["asset_id"] == row.asset_id].iloc[0]
        lines.append(f"- {row.event_id} / {asset.ticker}: {event.event_name}")

    lines.extend(["", "## Files Found", ""])
    if found_files:
        lines.extend([f"- {item}" for item in found_files])
    else:
        lines.append("- No local price files found for required core assets or benchmarks.")

    lines.extend(["", "## Missing or Unusable Files", ""])
    if missing_files:
        lines.extend([f"- {item}" for item in missing_files])
    else:
        lines.append("- No required local price files are missing.")

    if local_issues:
        lines.extend(["", "## Local File Issues", ""])
        lines.extend([f"- {item}" for item in local_issues])

    lines.extend([
        "",
        "## Output Counts",
        "",
        f"- market_returns.csv rows: {len(prices)}",
        f"- event_firm_returns.csv rows: {len(returns)}",
        f"- rows with primary outcome car_sector_m1_p1 calculated: {len(covered_rows)}",
        f"- rows still missing primary outcome car_sector_m1_p1: {len(missing_rows)}",
        "",
        "## Event-Window Coverage",
        "",
    ])
    if coverage_issues.empty:
        lines.append("- All core rows have requested event-window coverage.")
    else:
        for row in coverage_issues.itertuples(index=False):
            lines.append(f"- {row.event_id}/{row.asset_id}: {row.event_window_coverage}; {row.calculation_notes}")

    lines.extend(["", "## Rows Successfully Calculated", ""])
    if covered_rows.empty:
        lines.append("- None.")
    else:
        for row in covered_rows.itertuples(index=False):
            lines.append(f"- {row.event_id}/{row.asset_id}: car_sector_m1_p1 calculated; t0={row.event_t0_trade_date}")

    lines.extend(["", "## Rows Still Missing", ""])
    if missing_rows.empty:
        lines.append("- None.")
    else:
        for row in missing_rows.itertuples(index=False):
            lines.append(f"- {row.event_id}/{row.asset_id}: {row.data_quality_flag}; {row.calculation_notes}")

    lines.extend(["", "## Schema and Key Validation", ""])
    if schema_issues:
        lines.extend([f"- {issue}" for issue in schema_issues])
    else:
        lines.append("- No schema/key integrity issues detected before local return construction.")

    lines.extend(["", "## Post-Freeze Guardrails", ""])
    lines.append("- No theory, event-universe, or frozen sample-logic changes were made.")
    lines.append("- This run is limited to E009/INTC, E010/TSM, and E012/MU plus SMH, SPY, and QQQ price inputs.")
    lines.append("- Adj Close is used when available; Close is used only when Adj Close is absent.")
    LOCAL_REPORT_OUT.write_text("\n".join(lines) + "\n")


def fmt_pct(value: object) -> str:
    if value is None or pd.isna(value):
        return "pending"
    return f"{float(value) * 100:.2f}%"


def classify_evidence(row: pd.Series) -> str:
    value = row.get("car_sector_m1_p1")
    if value is None or pd.isna(value):
        return "pending - price/window data missing"
    value = float(value)
    if value > 0.0025:
        if row.get("data_quality_flag") == "clean":
            return "supportive evidence"
        return "weak evidence"
    if value < -0.0025:
        return "theory-weakening evidence"
    return "null evidence"


def immediate_interpretation(row: pd.Series) -> str:
    classification = classify_evidence(row)
    if classification.startswith("pending"):
        return "No empirical interpretation is available until the local price files cover the event window."
    if classification == "supportive evidence":
        return "The beneficiary outperformed the semiconductor-sector benchmark in the primary window, which is consistent with investors pricing credible state support as firm-specific opportunity."
    if classification == "weak evidence":
        return "The primary sector-adjusted reaction is positive, but data quality or benchmark consistency prevents treating it as clean support."
    if classification == "null evidence":
        return "The primary sector-adjusted reaction is economically close to zero, so the event does not provide clear evidence for or against the mechanism."
    return "The beneficiary underperformed the semiconductor-sector benchmark in the primary window, which is inconsistent with the expected state-support opportunity reaction for this event."


def write_first_results_memo(
    events: pd.DataFrame,
    assets: pd.DataFrame,
    returns: pd.DataFrame,
) -> None:
    event_map = events.set_index("event_id")
    asset_map = assets.set_index("asset_id")
    lines = [
        "# First Results Memo",
        "",
        "## Scope",
        "",
        "This memo reports the first frozen core event-study outputs only. It does not discuss publication potential and does not generalize beyond the three main eligible support events.",
        "",
        "## Evidence Classification Rule",
        "",
        "- Primary evidence variable: car_sector_m1_p1.",
        "- Supportive evidence: car_sector_m1_p1 > 0.25 percentage points and data_quality_flag is clean.",
        "- Weak evidence: car_sector_m1_p1 > 0.25 percentage points but data quality or benchmark coverage is not clean.",
        "- Null evidence: car_sector_m1_p1 is between -0.25 and +0.25 percentage points.",
        "- Theory-weakening evidence: car_sector_m1_p1 < -0.25 percentage points.",
        "- Pending: primary outcome cannot be calculated from available local price files.",
        "",
        "## Event Results",
        "",
    ]
    for row in returns.sort_values(["event_id", "asset_id"]).itertuples(index=False):
        result = pd.Series(row._asdict())
        event = event_map.loc[result["event_id"]]
        asset = asset_map.loc[result["asset_id"]]
        classification = classify_evidence(result)
        lines.extend([
            f"### {result['event_id']} / {asset['ticker']}",
            "",
            f"- Event description: {event['event_name']} ({event['event_date']}); named beneficiary asset: {asset['asset_name']}.",
            f"- Event trading date used: {result['event_t0_trade_date'] if pd.notna(result['event_t0_trade_date']) else 'pending'}.",
            f"- Raw return: {fmt_pct(result['event_day_return'])}.",
            f"- Market-adjusted return: {fmt_pct(result['ar_market_event_day'])} event-day; {fmt_pct(result['car_market_m1_p1'])} CAR [-1,+1] versus SPY.",
            f"- Sector-adjusted return: {fmt_pct(result['ar_sector_event_day'])} event-day; {fmt_pct(result['car_sector_m1_p1'])} CAR [-1,+1] versus SMH.",
            f"- Benchmark comparison: SPY CAR adjustment {fmt_pct(result['car_market_m1_p1'])}; QQQ CAR adjustment {fmt_pct(result.get('car_tech_m1_p1'))}; SMH CAR adjustment {fmt_pct(result['car_sector_m1_p1'])}.",
            f"- Immediate interpretation: {immediate_interpretation(result)}",
            f"- Evidence category: {classification}.",
            f"- Calculation status: {result['data_quality_flag']}; {result['event_window_coverage']}; {result['calculation_notes']}.",
            "",
        ])
    lines.extend([
        "## Guardrails",
        "",
        "- The memo evaluates consistency with the frozen State Support mechanism only.",
        "- It does not claim causal proof from three events.",
        "- It does not interpret missing price rows as evidence.",
    ])
    FIRST_RESULTS_MEMO_OUT.write_text("\n".join(lines) + "\n")


def main() -> None:
    events, assets, links = read_inputs()
    schema_issues = validate_inputs(events, assets, links)
    core_events, core_assets, core_links, _required_asset_ids = select_core_local_inputs(events, assets, links)
    prices, found_files, missing_files, local_issues = load_local_prices(core_assets)
    prices.to_csv(MARKET_RETURNS_OUT, index=False, quoting=csv.QUOTE_MINIMAL)
    returns = build_event_returns(core_events, assets, core_links, prices)
    returns.to_csv(EVENT_RETURNS_OUT, index=False, quoting=csv.QUOTE_MINIMAL)
    write_local_price_report(
        core_events,
        assets,
        core_links,
        prices,
        returns,
        schema_issues,
        found_files,
        missing_files,
        local_issues,
    )
    write_first_results_memo(core_events, assets, returns)


if __name__ == "__main__":
    main()
