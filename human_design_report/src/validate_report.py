import re
from dataclasses import asdict, dataclass

from normalize_chart import ChartData


@dataclass
class ValidationIssue:
    type: str
    expected: str | None
    found: str | None
    location: str


@dataclass
class ValidationResult:
    valid: bool
    errors: list[dict]
    warnings: list[str]


def _extract_gate_lines(text: str) -> set[str]:
    return set(re.findall(r"\b\d{1,2}\.\d\b", text))


def _mentioned_near(full_text: str, side: str, planet: str, gate_line: str) -> bool:
    pattern = rf"{re.escape(planet)}\s*\({re.escape(side)}\).*?{re.escape(gate_line)}|{re.escape(side)}\s+{re.escape(planet)}.*?{re.escape(gate_line)}"
    return re.search(pattern, full_text, re.IGNORECASE | re.DOTALL) is not None


def validate_report(chart: ChartData, blocks: dict[str, str]) -> ValidationResult:
    full_text = "\n\n".join(blocks.values())
    found_gate_lines = _extract_gate_lines(full_text)
    errors: list[dict] = []
    warnings: list[str] = []

    expected_entries: list[tuple[str, str, str]] = []
    for side_name, side_data in (("Personality", chart.personality), ("Design", chart.design)):
        for planet, gate_line in side_data.items():
            if gate_line:
                expected_entries.append((side_name, planet, gate_line))

    expected_gate_lines = {item[2] for item in expected_entries}

    for side_name, planet, gate_line in expected_entries:
        if gate_line not in full_text:
            errors.append(asdict(ValidationIssue("missing_gate_line", gate_line, None, f"{side_name} {planet}")))
        elif not _mentioned_near(full_text, side_name, planet, gate_line):
            errors.append(asdict(ValidationIssue("personality_design_mismatch", gate_line, gate_line, f"{side_name} {planet}")))

    for gate_line in sorted(found_gate_lines):
        if gate_line not in expected_gate_lines:
            errors.append(asdict(ValidationIssue("extra_gate_line", None, gate_line, "report")))

    for side_name, planet, _ in expected_entries:
        if f"{planet} ({side_name})" not in full_text and f"{side_name} {planet}" not in full_text:
            errors.append(asdict(ValidationIssue("missing_planet", planet, None, f"{side_name} {planet}")))

    for field_name in ["type", "profile", "authority", "strategy", "definition"]:
        value = getattr(chart, field_name)
        if value and value not in full_text:
            errors.append(asdict(ValidationIssue("field_mismatch", value, None, field_name)))

    return ValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)
