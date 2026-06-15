from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "dissertation_results" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1800
HEIGHT = 1200
MARGIN_L = 250
MARGIN_R = 120
MARGIN_T = 190
MARGIN_B = 240
PLOT_W = WIDTH - MARGIN_L - MARGIN_R
PLOT_H = HEIGHT - MARGIN_T - MARGIN_B

INK = "#1f2933"
AXIS = "#2f3437"
GRID = "#d8dde3"
TEXT_MUTED = "#5b6470"
POS = "#2f6f8f"
NEG = "#a94442"
NEUTRAL = "#4f6d8a"


@dataclass
class FigureSpec:
    key: str
    number: int
    title: str
    subtitle: str
    ylabel: str
    source_note: str
    labels: list[str]
    values: list[float]
    horizontal: bool = False
    y_min: float | None = None
    y_max: float | None = None


FIGURES = [
    FigureSpec(
        key="figure1_primary_outcome_car_sector_m1_p1",
        number=1,
        title="Primary Outcome (car_sector_m1_p1) Across Primary Cases",
        subtitle="Sector-adjusted CAR[-1,+1], percentage points",
        ylabel="car_sector_m1_p1",
        source_note="Source: validated event-study output, primary evidence variable car_sector_m1_p1.",
        labels=["E009 / INTC", "E010 / TSM", "E012 / MU"],
        values=[-4.3183, 2.1512, -2.5406],
        y_min=-5.0,
        y_max=3.0,
    ),
    FigureSpec(
        key="figure2_primary_case_descriptive_car_m7_p7",
        number=2,
        title="Descriptive CAR[-7,+7] Across Primary Cases",
        subtitle="Sector-adjusted descriptive CAR[-7,+7], percentage points",
        ylabel="CAR[-7,+7]",
        source_note="Source: validated event-study output, descriptive primary-case return measures.",
        labels=["E009 / INTC", "E010 / TSM", "E012 / MU"],
        values=[-0.0288, 5.9035, -3.2454],
        y_min=-4.0,
        y_max=7.0,
    ),
    FigureSpec(
        key="figure3_recipient_vs_nonrecipient_mean_car",
        number=3,
        title="Recipient vs Non-Recipient Mean CAR Comparison",
        subtitle="Mean SMH-adjusted CAR[-7,+7], percentage points",
        ylabel="Mean CAR[-7,+7]",
        source_note="Source: validated support/subsidy_award event audit; recipient N = 5, non-recipient N = 7.",
        labels=["Recipient", "Non-recipient"],
        values=[-0.3186, -2.1506],
        y_min=-3.0,
        y_max=0.6,
    ),
    FigureSpec(
        key="figure4_event_level_divergence_spread",
        number=4,
        title="Event-Level Divergence Across Validated Events",
        subtitle="Validated divergence spread, percentage points",
        ylabel="Divergence spread",
        source_note="Source: validated divergence audit; events ranked by spread from largest to smallest.",
        labels=["E010", "E011", "E012", "E009"],
        values=[15.8942, 9.0598, 1.7661, 1.5946],
        horizontal=True,
        y_min=0.0,
        y_max=17.0,
    ),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


FONT_TITLE = font(44, True)
FONT_SUBTITLE = font(25)
FONT_AXIS = font(24)
FONT_TICK = font(22)
FONT_LABEL = font(24)
FONT_VALUE = font(23, True)
FONT_NOTE = font(19)


def nice_ticks(y_min: float, y_max: float, step: float) -> list[float]:
    ticks = []
    v = y_min
    while v <= y_max + 1e-9:
        ticks.append(round(v, 4))
        v += step
    return ticks


def vertical_ticks(y_min: float, y_max: float) -> list[float]:
    span = y_max - y_min
    if span <= 4:
        step = 0.5
    elif span <= 9:
        step = 1.0
    else:
        step = 2.0
    return nice_ticks(y_min, y_max, step)


def text_center(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, fnt, fill=INK):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    draw.text((xy[0] - (bbox[2] - bbox[0]) / 2, xy[1]), text, font=fnt, fill=fill)


def draw_vertical_png(spec: FigureSpec, out: Path) -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    y_min, y_max = spec.y_min, spec.y_max
    assert y_min is not None and y_max is not None

    text_center(draw, (WIDTH / 2, 55), spec.title, FONT_TITLE)
    text_center(draw, (WIDTH / 2, 115), spec.subtitle, FONT_SUBTITLE, TEXT_MUTED)

    left, right = MARGIN_L, WIDTH - MARGIN_R
    top, bottom = MARGIN_T, HEIGHT - MARGIN_B

    def y_pos(value: float) -> float:
        return bottom - ((value - y_min) / (y_max - y_min)) * (bottom - top)

    ticks = vertical_ticks(y_min, y_max)
    for tick in ticks:
        y = y_pos(tick)
        draw.line((left, y, right, y), fill=GRID, width=2)
        label = f"{tick:.1f}%"
        bbox = draw.textbbox((0, 0), label, font=FONT_TICK)
        draw.text((left - 18 - (bbox[2] - bbox[0]), y - 13), label, font=FONT_TICK, fill=INK)

    zero_y = y_pos(0)
    draw.line((left, zero_y, right, zero_y), fill=AXIS, width=4)
    draw.line((left, top, left, bottom), fill=AXIS, width=3)
    draw.line((left, bottom, right, bottom), fill=AXIS, width=3)

    n = len(spec.values)
    slot = (right - left) / n
    bar_w = min(210, slot * 0.48)
    for idx, (label, value) in enumerate(zip(spec.labels, spec.values)):
        cx = left + slot * (idx + 0.5)
        yv = y_pos(value)
        y0 = y_pos(0)
        color = POS if value >= 0 else NEG
        draw.rectangle((cx - bar_w / 2, min(yv, y0), cx + bar_w / 2, max(yv, y0)), fill=color)
        value_label = f"{value:.4f}%"
        if value >= 0:
            vy = yv - 38
        else:
            vy = yv + 13
        text_center(draw, (cx, vy), value_label, FONT_VALUE, INK)
        text_center(draw, (cx, bottom + 34), label, FONT_LABEL, INK)

    # Rotated y-axis label.
    label_img = Image.new("RGBA", (380, 60), (255, 255, 255, 0))
    label_draw = ImageDraw.Draw(label_img)
    text_center(label_draw, (190, 8), spec.ylabel, FONT_AXIS, INK)
    rotated = label_img.rotate(90, expand=True)
    img.paste(rotated, (70, int(top + (bottom - top) / 2 - rotated.height / 2)), rotated)

    draw.text((left, HEIGHT - 105), spec.source_note, font=FONT_NOTE, fill=TEXT_MUTED)
    img.save(out, dpi=(300, 300))


def draw_horizontal_png(spec: FigureSpec, out: Path) -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    x_min, x_max = spec.y_min, spec.y_max
    assert x_min is not None and x_max is not None

    text_center(draw, (WIDTH / 2, 55), spec.title, FONT_TITLE)
    text_center(draw, (WIDTH / 2, 115), spec.subtitle, FONT_SUBTITLE, TEXT_MUTED)

    left, right = 320, WIDTH - 140
    top, bottom = 220, HEIGHT - 260

    def x_pos(value: float) -> float:
        return left + ((value - x_min) / (x_max - x_min)) * (right - left)

    for tick in [0, 5, 10, 15]:
        x = x_pos(tick)
        draw.line((x, top, x, bottom), fill=GRID, width=2)
        label = f"{tick:.0f}%"
        text_center(draw, (x, bottom + 18), label, FONT_TICK, INK)

    draw.line((left, top, left, bottom), fill=AXIS, width=3)
    draw.line((left, bottom, right, bottom), fill=AXIS, width=3)

    n = len(spec.values)
    slot = (bottom - top) / n
    bar_h = min(115, slot * 0.52)
    for idx, (label, value) in enumerate(zip(spec.labels, spec.values)):
        cy = top + slot * (idx + 0.5)
        xv = x_pos(value)
        draw.rectangle((left, cy - bar_h / 2, xv, cy + bar_h / 2), fill=NEUTRAL)
        draw.text((95, cy - 16), label, font=FONT_LABEL, fill=INK)
        draw.text((xv + 18, cy - 16), f"{value:.4f}%", font=FONT_VALUE, fill=INK)

    text_center(draw, ((left + right) / 2, bottom + 80), spec.ylabel, FONT_AXIS, INK)
    draw.text((left, HEIGHT - 105), spec.source_note, font=FONT_NOTE, fill=TEXT_MUTED)
    img.save(out, dpi=(300, 300))


def svg_text(x, y, text, size, weight="400", anchor="start", fill=INK):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}">{escape(text)}</text>'
    )


def svg_line(x1, y1, x2, y2, stroke, width=1.5):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{width}"/>'


def draw_vertical_svg(spec: FigureSpec, out: Path) -> None:
    y_min, y_max = spec.y_min, spec.y_max
    assert y_min is not None and y_max is not None
    left, right = MARGIN_L, WIDTH - MARGIN_R
    top, bottom = MARGIN_T, HEIGHT - MARGIN_B

    def y_pos(value: float) -> float:
        return bottom - ((value - y_min) / (y_max - y_min)) * (bottom - top)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">Figure {spec.number}. {escape(spec.title)}</title>",
        f"<desc id=\"desc\">{escape(spec.subtitle)}</desc>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>',
        svg_text(WIDTH / 2, 82, spec.title, 44, "700", "middle"),
        svg_text(WIDTH / 2, 135, spec.subtitle, 25, "400", "middle", TEXT_MUTED),
    ]
    for tick in vertical_ticks(y_min, y_max):
        y = y_pos(tick)
        parts.append(svg_line(left, y, right, y, GRID, 2))
        parts.append(svg_text(left - 18, y + 8, f"{tick:.1f}%", 22, "400", "end"))
    zero_y = y_pos(0)
    parts.extend([
        svg_line(left, zero_y, right, zero_y, AXIS, 4),
        svg_line(left, top, left, bottom, AXIS, 3),
        svg_line(left, bottom, right, bottom, AXIS, 3),
    ])
    n = len(spec.values)
    slot = (right - left) / n
    bar_w = min(210, slot * 0.48)
    for idx, (label, value) in enumerate(zip(spec.labels, spec.values)):
        cx = left + slot * (idx + 0.5)
        yv = y_pos(value)
        y0 = y_pos(0)
        color = POS if value >= 0 else NEG
        parts.append(f'<rect x="{cx - bar_w / 2:.1f}" y="{min(yv, y0):.1f}" width="{bar_w:.1f}" height="{abs(yv - y0):.1f}" fill="{color}"/>')
        vy = yv - 22 if value >= 0 else yv + 34
        parts.append(svg_text(cx, vy, f"{value:.4f}%", 23, "700", "middle"))
        parts.append(svg_text(cx, bottom + 58, label, 24, "400", "middle"))
    parts.append(f'<text x="78" y="{top + (bottom - top) / 2:.1f}" transform="rotate(-90 78 {top + (bottom - top) / 2:.1f})" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="{INK}">{escape(spec.ylabel)}</text>')
    parts.append(svg_text(left, HEIGHT - 105, spec.source_note, 19, "400", "start", TEXT_MUTED))
    parts.append("</svg>")
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")


def draw_horizontal_svg(spec: FigureSpec, out: Path) -> None:
    x_min, x_max = spec.y_min, spec.y_max
    assert x_min is not None and x_max is not None
    left, right = 320, WIDTH - 140
    top, bottom = 220, HEIGHT - 260

    def x_pos(value: float) -> float:
        return left + ((value - x_min) / (x_max - x_min)) * (right - left)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">Figure {spec.number}. {escape(spec.title)}</title>",
        f"<desc id=\"desc\">{escape(spec.subtitle)}</desc>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>',
        svg_text(WIDTH / 2, 82, spec.title, 44, "700", "middle"),
        svg_text(WIDTH / 2, 135, spec.subtitle, 25, "400", "middle", TEXT_MUTED),
    ]
    for tick in [0, 5, 10, 15]:
        x = x_pos(tick)
        parts.append(svg_line(x, top, x, bottom, GRID, 2))
        parts.append(svg_text(x, bottom + 48, f"{tick:.0f}%", 22, "400", "middle"))
    parts.extend([svg_line(left, top, left, bottom, AXIS, 3), svg_line(left, bottom, right, bottom, AXIS, 3)])
    n = len(spec.values)
    slot = (bottom - top) / n
    bar_h = min(115, slot * 0.52)
    for idx, (label, value) in enumerate(zip(spec.labels, spec.values)):
        cy = top + slot * (idx + 0.5)
        xv = x_pos(value)
        parts.append(f'<rect x="{left:.1f}" y="{cy - bar_h / 2:.1f}" width="{xv - left:.1f}" height="{bar_h:.1f}" fill="{NEUTRAL}"/>')
        parts.append(svg_text(95, cy + 8, label, 24))
        parts.append(svg_text(xv + 18, cy + 8, f"{value:.4f}%", 23, "700"))
    parts.append(svg_text((left + right) / 2, bottom + 105, spec.ylabel, 24, "400", "middle"))
    parts.append(svg_text(left, HEIGHT - 105, spec.source_note, 19, "400", "start", TEXT_MUTED))
    parts.append("</svg>")
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")


def write_notes() -> None:
    captions = [
        "# Figure Captions",
        "",
        "Figure 1. Primary Outcome (car_sector_m1_p1) Across Primary Cases. Bars report the validated sector-adjusted CAR[-1,+1] primary outcome for E009 / INTC, E010 / TSM, and E012 / MU.",
        "",
        "Figure 2. Descriptive CAR[-7,+7] Across Primary Cases. Bars report validated descriptive sector-adjusted CAR[-7,+7] values for the three primary cases.",
        "",
        "Figure 3. Recipient vs Non-Recipient Mean CAR Comparison. Bars report validated mean SMH-adjusted CAR[-7,+7] for recipient and non-recipient observations in the support-event audit.",
        "",
        "Figure 4. Event-Level Divergence Across Validated Events. Horizontal bars report validated divergence spreads ranked from largest to smallest.",
        "",
    ]
    (FIG_DIR / "figure_captions.md").write_text("\n".join(captions), encoding="utf-8")

    sources = [
        "# Figure Source Notes",
        "",
        "Figure 1: Source: validated event-study output, primary evidence variable car_sector_m1_p1. Values used: E009 / INTC = -4.3183; E010 / TSM = 2.1512; E012 / MU = -2.5406.",
        "",
        "Figure 2: Source: validated event-study output, descriptive primary-case return measures. Values used: E009 / INTC = -0.0288; E010 / TSM = 5.9035; E012 / MU = -3.2454.",
        "",
        "Figure 3: Source: validated support/subsidy_award event audit. Values used: Recipient Mean CAR = -0.3186; Non-Recipient Mean CAR = -2.1506.",
        "",
        "Figure 4: Source: validated divergence audit. Values used: E009 = 1.5946; E010 = 15.8942; E011 = 9.0598; E012 = 1.7661. Ranking is by validated spread value, largest first.",
        "",
        "No new analysis was performed. Figures use only the validated values supplied for Chapter 5 Results.",
        "",
    ]
    (FIG_DIR / "figure_source_notes.md").write_text("\n".join(sources), encoding="utf-8")

    placement = [
        "# Suggested Placement in Chapter 5",
        "",
        "- Figure 1: Place in Section 5.2, immediately after the paragraph reporting the primary outcome classifications.",
        "- Figure 2: Place in Section 5.3, after the paragraph listing the descriptive Day0_AR and CAR[-7,+7] values.",
        "- Figure 3: Place in Section 5.5, after the recipient versus non-recipient summary paragraph.",
        "- Figure 4: Optional. Place after Figure 3 in Section 5.5 or in an appendix/subsection on event-level divergence if the final thesis discusses the divergence audit.",
        "",
    ]
    (FIG_DIR / "figure_placement_notes.md").write_text("\n".join(placement), encoding="utf-8")


def main() -> None:
    for spec in FIGURES:
        svg_out = FIG_DIR / f"{spec.key}.svg"
        png_out = FIG_DIR / f"{spec.key}.png"
        if spec.horizontal:
            draw_horizontal_svg(spec, svg_out)
            draw_horizontal_png(spec, png_out)
        else:
            draw_vertical_svg(spec, svg_out)
            draw_vertical_png(spec, png_out)
    write_notes()


if __name__ == "__main__":
    main()
