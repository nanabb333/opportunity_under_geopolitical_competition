const DATA_FILES = {
  scenario: "../results/scenario_query_demo_results.json",
  pathways: "../results/observed_pathways.json",
  coverage: "../results/dataset_coverage_report.json",
  interactive: "../results/interactive_scenario_analysis.json",
  health: "../results/system_health_report.json",
  briefs: "../results/analyst_briefs.json",
};

const state = {
  scenarioData: null,
  pathwayData: null,
  coverageData: null,
  coverageError: null,
  interactiveData: null,
  interactiveError: null,
  selectedInteractiveScenarioId: null,
  healthData: null,
  healthError: null,
  briefData: null,
  briefError: null,
  selectedBriefScenarioId: null,
  errors: [],
};

function formatScore(score) {
  const value = Number(score);
  if (Number.isNaN(value)) {
    return "Not coded";
  }
  return value.toFixed(4);
}

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) {
    node.className = className;
  }
  if (text !== undefined) {
    node.textContent = text;
  }
  return node;
}

async function loadJson(label, path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`${path} returned HTTP ${response.status}`);
  }
  return response.json();
}

function renderDataStatus() {
  const status = document.getElementById("data-status");
  if (state.errors.length > 0) {
    status.textContent = "Evidence files incomplete";
    return;
  }
  const scenarioCount = state.scenarioData?.results?.length ?? 0;
  const pathwayCount = state.pathwayData?.results?.length ?? 0;
  const coverageStatus = state.coverageData ? "coverage loaded" : "coverage unavailable";
  const interactiveStatus = state.interactiveData ? "interactive assistant loaded" : "interactive assistant unavailable";
  const healthStatus = state.healthData ? `operations ${state.healthData.overall_status}` : "operations unavailable";
  const briefStatus = state.briefData ? "briefs loaded" : "briefs unavailable";
  status.textContent = `${scenarioCount} scenarios, ${pathwayCount} pathway summaries, ${coverageStatus}, ${interactiveStatus}, ${healthStatus}, ${briefStatus}`;
}

function renderErrors() {
  const panel = document.getElementById("error-panel");
  panel.innerHTML = "";
  if (state.errors.length === 0) {
    panel.hidden = true;
    return;
  }

  panel.hidden = false;
  panel.appendChild(el("h2", null, "Evidence files could not be loaded"));
  const explanation = el(
    "p",
    null,
    "Start a local server from the repository root and confirm the required JSON files exist."
  );
  panel.appendChild(explanation);

  const list = el("ul");
  state.errors.forEach((message) => {
    list.appendChild(el("li", null, message));
  });
  panel.appendChild(list);
}

function renderScenarioCards() {
  const container = document.getElementById("scenario-container");
  container.innerHTML = "";

  const scenarios = state.scenarioData?.results ?? [];
  if (scenarios.length === 0) {
    container.appendChild(el("p", "evidence-note", "No scenario query results are available."));
    return;
  }

  scenarios.forEach((scenario) => {
    const card = el("article", "scenario-card");
    card.appendChild(el("span", "scenario-id", scenario.scenario_id));
    card.appendChild(el("h3", null, scenario.question));

    const profile = scenario.scenario_profile ?? {};
    const profileList = el("ul", "profile-list");
    [
      ["Event family", profile.event_family],
      ["Sector", profile.affected_sector],
      ["Support signal", profile.state_support_signal],
      ["Pressure signal", profile.restriction_or_pressure_signal],
      ["Scenario pathway", profile.observed_market_pathway],
    ].forEach(([label, value]) => {
      const item = el("li");
      item.appendChild(el("span", null, label));
      item.appendChild(el("strong", null, value ?? "Not coded"));
      profileList.appendChild(item);
    });
    card.appendChild(profileList);

    card.appendChild(el("h3", null, "Top Historical Analogues"));
    const analogueList = el("ul", "analogue-list");
    (scenario.top_analogues ?? []).forEach((analogue) => {
      const item = el("li", "analogue-item");
      item.appendChild(el("h3", null, `${analogue.event_id}: ${analogue.event_title}`));

      const meta = el("div", "analogue-meta");
      meta.appendChild(el("span", "tag score-tag", `Similarity ${formatScore(analogue.similarity_score)}`));
      meta.appendChild(el("span", "tag", analogue.observed_market_pathway ?? "Not coded"));
      item.appendChild(meta);

      item.appendChild(el("p", "evidence-note", analogue.evidence_note ?? "No evidence note available."));
      analogueList.appendChild(item);
    });
    card.appendChild(analogueList);
    container.appendChild(card);
  });
}

function renderCoverage() {
  const container = document.getElementById("coverage-container");
  container.innerHTML = "";

  if (!state.coverageData) {
    container.appendChild(
      el(
        "p",
        "fallback-note",
        `Coverage report unavailable. Run python3 scripts/dataset_coverage_analysis.py to generate ${DATA_FILES.coverage}.`
      )
    );
    if (state.coverageError) {
      container.appendChild(el("p", "fallback-detail", state.coverageError));
    }
    return;
  }

  const coverage = state.coverageData.coverage ?? {};
  const cards = [
    ["event_family", "Event family coverage"],
    ["affected_sector", "Sector coverage"],
    ["country_or_region", "Geography coverage"],
  ];

  cards.forEach(([field, title]) => {
    const card = el("article", "coverage-card");
    card.appendChild(el("h3", null, title));
    const counts = coverage[field]?.counts ?? [];
    if (counts.length === 0) {
      card.appendChild(el("p", "evidence-note", "No coverage values available."));
    } else {
      const list = el("ul", "coverage-list");
      counts.forEach((item) => {
        const row = el("li");
        row.appendChild(el("span", null, item.value));
        row.appendChild(el("strong", null, String(item.count)));
        list.appendChild(row);
      });
      card.appendChild(list);
    }
    container.appendChild(card);
  });
}

function renderOperationsOverview() {
  const container = document.getElementById("operations-container");
  container.innerHTML = "";

  if (!state.healthData) {
    container.appendChild(
      el(
        "p",
        "fallback-note",
        `Operations health report unavailable. Run python3 scripts/system_health_report.py to generate ${DATA_FILES.health}.`
      )
    );
    if (state.healthError) {
      container.appendChild(el("p", "fallback-detail", state.healthError));
    }
    return;
  }

  const dataset = state.healthData.dataset_status ?? {};
  const queue = state.healthData.queue_status ?? {};
  const coverage = state.healthData.coverage_status ?? {};
  const validation = state.healthData.validation_status ?? {};
  const dashboard = state.healthData.dashboard_status ?? {};

  const cards = [
    ["Dataset size", dataset.dataset_size ?? "Not coded", dataset.status ?? "Not coded"],
    ["Queue size", queue.queue_size ?? "Not coded", queue.status ?? "Not coded"],
    ["Reviewed events", queue.reviewed_events ?? "Not coded", "Queue"],
    ["Pending events", queue.pending_events ?? "Not coded", "Queue"],
    ["Latest update date", dataset.latest_update_date ?? "Not recorded", "Change log"],
    ["Coverage status", coverage.status ?? "Not coded", coverage.matches_dataset ? "Current" : "Check coverage"],
    ["Validation status", validation.status ?? "Not coded", validation.message ?? "No validation message"],
    ["Dashboard status", dashboard.status ?? "Not coded", "Static files"],
  ];

  cards.forEach(([label, value, note]) => {
    const card = el("article", "operations-card");
    card.appendChild(el("span", "operations-label", label));
    card.appendChild(el("strong", "operations-value", String(value)));
    card.appendChild(el("p", "evidence-note", String(note)));
    container.appendChild(card);
  });
}

function renderInteractiveAssistant() {
  const container = document.getElementById("interactive-container");
  container.innerHTML = "";

  const scenarios = state.interactiveData?.results ?? [];
  if (scenarios.length === 0) {
    container.appendChild(
      el(
        "p",
        "fallback-note",
        `Interactive scenario analysis unavailable. Run python3 scripts/analyse_scenario_profile.py to generate ${DATA_FILES.interactive}.`
      )
    );
    if (state.interactiveError) {
      container.appendChild(el("p", "fallback-detail", state.interactiveError));
    }
    return;
  }

  if (!state.selectedInteractiveScenarioId) {
    state.selectedInteractiveScenarioId = scenarios[0].scenario_id;
  }

  const selectedScenario = scenarios.find(
    (scenario) => scenario.scenario_id === state.selectedInteractiveScenarioId
  ) ?? scenarios[0];

  const controls = el("div", "interactive-controls");
  const label = el("label", "scenario-select-label", "Scenario");
  label.setAttribute("for", "interactive-scenario-select");

  const select = el("select", "scenario-select");
  select.id = "interactive-scenario-select";
  scenarios.forEach((scenario) => {
    const option = el("option", null, `${scenario.scenario_id}: ${scenario.scenario_question}`);
    option.value = scenario.scenario_id;
    option.selected = scenario.scenario_id === selectedScenario.scenario_id;
    select.appendChild(option);
  });
  select.addEventListener("change", (event) => {
    state.selectedInteractiveScenarioId = event.target.value;
    renderInteractiveAssistant();
  });
  controls.appendChild(label);
  controls.appendChild(select);
  container.appendChild(controls);

  const summary = el("article", "interactive-summary");
  summary.appendChild(el("span", "scenario-id", selectedScenario.scenario_id));
  summary.appendChild(el("h3", null, selectedScenario.scenario_question));
  summary.appendChild(el("p", "evidence-note", selectedScenario.analyst_note));

  const profile = selectedScenario.scenario_profile ?? {};
  const profileList = el("ul", "profile-list compact-profile-list");
  [
    ["Event family", profile.event_family],
    ["Sector", profile.affected_sector],
    ["Region", profile.country_or_region],
    ["Support signal", profile.state_support_signal],
    ["Pressure signal", profile.restriction_or_pressure_signal],
    ["Surprise level", profile.surprise_level],
  ].forEach(([labelText, value]) => {
    const item = el("li");
    item.appendChild(el("span", null, labelText));
    item.appendChild(el("strong", null, value ?? "Not coded"));
    profileList.appendChild(item);
  });
  summary.appendChild(profileList);
  container.appendChild(summary);

  const layout = el("div", "interactive-layout");

  const analogueColumn = el("section", "interactive-column");
  analogueColumn.appendChild(el("h3", null, "Top Historical Analogues"));
  const analogueList = el("div", "analogue-stack");
  (selectedScenario.top_analogues ?? []).forEach((analogue) => {
    const card = el("article", "mini-card");
    card.appendChild(el("h3", null, `${analogue.event_id}: ${analogue.event_title}`));
    const meta = el("div", "analogue-meta");
    meta.appendChild(el("span", "tag score-tag", `Similarity ${formatScore(analogue.similarity_score)}`));
    meta.appendChild(el("span", "tag", analogue.observed_market_pathway ?? "Not coded"));
    card.appendChild(meta);
    card.appendChild(
      el(
        "p",
        "evidence-note",
        `Matched fields: ${(analogue.matched_fields ?? []).join(", ") || "None"}`
      )
    );
    card.appendChild(el("p", "evidence-note", analogue.evidence_note ?? "No evidence note available."));
    analogueList.appendChild(card);
  });
  analogueColumn.appendChild(analogueList);

  const pathwayColumn = el("section", "interactive-column");
  pathwayColumn.appendChild(el("h3", null, "Observed Pathway Summary"));
  const pathwayList = el("ul", "pathway-summary-list");
  (selectedScenario.observed_pathway_summary ?? []).forEach((pathway) => {
    const item = el("li");
    item.appendChild(el("strong", null, pathway.pathway_name));
    item.appendChild(el("span", "tag count-tag", `${pathway.count} analogue(s)`));
    item.appendChild(
      el("p", "evidence-note", `Representative events: ${(pathway.representative_events ?? []).join(", ")}`)
    );
    pathwayList.appendChild(item);
  });
  pathwayColumn.appendChild(pathwayList);

  pathwayColumn.appendChild(el("h3", null, "Limitations"));
  pathwayColumn.appendChild(
    el("p", "evidence-note", selectedScenario.limitations_note ?? state.interactiveData.limitations_note)
  );

  layout.appendChild(analogueColumn);
  layout.appendChild(pathwayColumn);
  container.appendChild(layout);
}

function renderAnalystBriefs() {
  const container = document.getElementById("brief-container");
  container.innerHTML = "";

  const briefs = state.briefData?.briefs ?? [];
  if (briefs.length === 0) {
    container.appendChild(
      el(
        "p",
        "fallback-note",
        `Analyst briefs unavailable. Run python3 scripts/generate_analyst_briefs.py to generate ${DATA_FILES.briefs}.`
      )
    );
    if (state.briefError) {
      container.appendChild(el("p", "fallback-detail", state.briefError));
    }
    return;
  }

  if (!state.selectedBriefScenarioId) {
    state.selectedBriefScenarioId = briefs[0].scenario_id;
  }

  const selectedBrief = briefs.find(
    (brief) => brief.scenario_id === state.selectedBriefScenarioId
  ) ?? briefs[0];

  const controls = el("div", "interactive-controls");
  const label = el("label", "scenario-select-label", "Brief scenario");
  label.setAttribute("for", "brief-scenario-select");

  const select = el("select", "scenario-select");
  select.id = "brief-scenario-select";
  briefs.forEach((brief) => {
    const option = el("option", null, `${brief.scenario_id}: ${brief.scenario_title ?? brief.scenario_question}`);
    option.value = brief.scenario_id;
    option.selected = brief.scenario_id === selectedBrief.scenario_id;
    select.appendChild(option);
  });
  select.addEventListener("change", (event) => {
    state.selectedBriefScenarioId = event.target.value;
    renderAnalystBriefs();
  });
  controls.appendChild(label);
  controls.appendChild(select);
  container.appendChild(controls);

  const briefCard = el("article", "brief-card");
  briefCard.appendChild(el("span", "scenario-id", selectedBrief.scenario_id));
  briefCard.appendChild(el("h3", null, selectedBrief.scenario_title ?? selectedBrief.scenario_description?.question ?? selectedBrief.scenario_question));
  briefCard.appendChild(
    el("p", "evidence-note", selectedBrief.scenario_description?.profile_summary ?? selectedBrief.scenario_description ?? "No profile summary available.")
  );
  briefCard.appendChild(el("p", "evidence-note", selectedBrief.analyst_note ?? "No analyst note available."));

  const sectionFlow = el("div", "brief-flow");

  const analogueSection = el("section", "brief-section");
  analogueSection.appendChild(el("h3", null, "Historical Analogues"));
  const analogueList = el("ul", "brief-list");
  (selectedBrief.most_relevant_historical_analogues ?? []).forEach((analogue) => {
    const item = el("li");
    item.appendChild(el("strong", null, `${analogue.event_id}: ${analogue.event_title}`));
    item.appendChild(
      el(
        "p",
        "evidence-note",
        `Similarity ${formatScore(analogue.similarity_score)}; pathway: ${analogue.observed_market_pathway}; matched fields: ${(analogue.matched_fields ?? []).join(", ") || "None"}`
      )
    );
    analogueList.appendChild(item);
  });
  analogueSection.appendChild(analogueList);

  const pathwaySection = el("section", "brief-section");
  pathwaySection.appendChild(el("h3", null, "Observed Pathways"));
  const pathwayList = el("ul", "brief-list");
  (selectedBrief.observed_historical_pathways ?? selectedBrief.common_observed_pathways ?? []).forEach((pathway) => {
    const item = el("li");
    item.appendChild(el("strong", null, pathway.pathway_name));
    item.appendChild(el("p", "evidence-note", pathway.analyst_note ?? pathway.summary_note));
    item.appendChild(
      el("p", "evidence-note", `Representative events: ${(pathway.representative_events ?? []).join(", ")}`)
    );
    pathwayList.appendChild(item);
  });
  pathwaySection.appendChild(pathwayList);

  const evidenceSection = el("section", "brief-section");
  evidenceSection.appendChild(el("h3", null, "Key Evidence"));
  const evidenceList = el("ul", "brief-list");
  (selectedBrief.key_evidence ?? selectedBrief.key_evidence_notes ?? []).forEach((note) => {
    if (typeof note === "string") {
      evidenceList.appendChild(el("li", null, note));
    } else {
      evidenceList.appendChild(el("li", null, `${note.event_id}: ${note.evidence_note}`));
    }
  });
  evidenceSection.appendChild(evidenceList);

  const caveatsSection = el("section", "brief-section");
  caveatsSection.appendChild(el("h3", null, "Analytical Caveats"));
  const caveatsList = el("ul", "brief-list");
  (selectedBrief.analytical_caveats ?? []).forEach((caveat) => {
    caveatsList.appendChild(el("li", null, caveat));
  });
  caveatsSection.appendChild(caveatsList);

  const limitationsSection = el("section", "brief-section");
  limitationsSection.appendChild(el("h3", null, "Research Limitations"));
  const limitationsList = el("ul", "brief-list");
  (selectedBrief.research_limitations ?? []).forEach((limitation) => {
    limitationsList.appendChild(el("li", null, limitation));
  });
  limitationsSection.appendChild(limitationsList);

  sectionFlow.appendChild(analogueSection);
  sectionFlow.appendChild(pathwaySection);
  sectionFlow.appendChild(evidenceSection);
  sectionFlow.appendChild(caveatsSection);
  sectionFlow.appendChild(limitationsSection);
  briefCard.appendChild(sectionFlow);
  container.appendChild(briefCard);
}

function renderPathways() {
  const container = document.getElementById("pathway-container");
  container.innerHTML = "";

  const scenarios = state.pathwayData?.results ?? [];
  if (scenarios.length === 0) {
    container.appendChild(el("p", "evidence-note", "No observed pathway summaries are available."));
    return;
  }

  scenarios.forEach((scenario) => {
    const card = el("article", "pathway-card");
    card.appendChild(el("h3", null, scenario.scenario_question));

    const list = el("ul", "pathway-list");
    (scenario.pathway_summary ?? []).forEach((pathway) => {
      const item = el("li", "pathway-item");
      const header = el("div", "pathway-item-header");
      header.appendChild(el("strong", null, pathway.pathway_name));
      header.appendChild(el("span", "tag count-tag", `${pathway.count} analogue(s)`));
      item.appendChild(header);

      item.appendChild(
        el("p", "evidence-note", `Representative events: ${(pathway.representative_events ?? []).join(", ")}`)
      );
      item.appendChild(el("p", "evidence-note", pathway.analyst_note ?? "No analyst note available."));

      const evidenceList = el("ul", "evidence-list");
      (pathway.evidence_notes ?? []).forEach((note) => {
        evidenceList.appendChild(
          el("li", null, `${note.event_id}: ${note.evidence_note}`)
        );
      });
      item.appendChild(evidenceList);
      list.appendChild(item);
    });

    card.appendChild(list);
    container.appendChild(card);
  });
}

async function init() {
  const [scenarioResult, pathwayResult, coverageResult, interactiveResult, healthResult, briefResult] = await Promise.allSettled([
    loadJson("scenario", DATA_FILES.scenario),
    loadJson("pathways", DATA_FILES.pathways),
    loadJson("coverage", DATA_FILES.coverage),
    loadJson("interactive", DATA_FILES.interactive),
    loadJson("health", DATA_FILES.health),
    loadJson("briefs", DATA_FILES.briefs),
  ]);

  if (scenarioResult.status === "fulfilled") {
    state.scenarioData = scenarioResult.value;
  } else {
    state.errors.push(`Missing or unreadable file: ${DATA_FILES.scenario}. ${scenarioResult.reason.message}`);
  }

  if (pathwayResult.status === "fulfilled") {
    state.pathwayData = pathwayResult.value;
  } else {
    state.errors.push(`Missing or unreadable file: ${DATA_FILES.pathways}. ${pathwayResult.reason.message}`);
  }

  if (coverageResult.status === "fulfilled") {
    state.coverageData = coverageResult.value;
  } else {
    state.coverageError = `Missing or unreadable file: ${DATA_FILES.coverage}. ${coverageResult.reason.message}`;
  }

  if (interactiveResult.status === "fulfilled") {
    state.interactiveData = interactiveResult.value;
  } else {
    state.interactiveError = `Missing or unreadable file: ${DATA_FILES.interactive}. ${interactiveResult.reason.message}`;
  }

  if (healthResult.status === "fulfilled") {
    state.healthData = healthResult.value;
  } else {
    state.healthError = `Missing or unreadable file: ${DATA_FILES.health}. ${healthResult.reason.message}`;
  }

  if (briefResult.status === "fulfilled") {
    state.briefData = briefResult.value;
  } else {
    state.briefError = `Missing or unreadable file: ${DATA_FILES.briefs}. ${briefResult.reason.message}`;
  }

  renderDataStatus();
  renderErrors();
  renderOperationsOverview();
  renderCoverage();
  renderInteractiveAssistant();
  renderAnalystBriefs();
  renderScenarioCards();
  renderPathways();
}

init();
