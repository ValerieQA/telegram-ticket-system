import json
import re
from typing import Any

from pydantic import BaseModel, Field

from openai_client import OpenAIClient

PLANET_NAMES = [
    "Sun",
    "Earth",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
    "North Node",
    "South Node",
    "Chiron",
]


class ChartData(BaseModel):
    type: str | None = None
    strategy: str | None = None
    authority: str | None = None
    profile: str | None = None
    definition: str | None = None
    incarnation_cross: str | None = None
    personality: dict[str, str | None] = Field(default_factory=dict)
    design: dict[str, str | None] = Field(default_factory=dict)
    channels: list[str] = Field(default_factory=list)
    centers: dict[str, Any] = Field(default_factory=dict)


def _find_single(raw_text: str, label: str) -> str | None:
    pattern = rf"{label}\s*[:\-]\s*(.+)"
    match = re.search(pattern, raw_text, re.IGNORECASE)
    return match.group(1).strip() if match else None


def _find_planets_block(raw_text: str, block_name: str) -> dict[str, str | None]:
    result = {planet: None for planet in PLANET_NAMES}
    for planet in PLANET_NAMES:
        pattern = rf"{block_name}.*?{planet}\s*[:\-]\s*(\d{{1,2}}\.\d)"
        match = re.search(pattern, raw_text, re.IGNORECASE | re.DOTALL)
        if match:
            result[planet] = match.group(1)
    return {k: v for k, v in result.items() if v is not None}


def _heuristic_parse(raw_text: str) -> ChartData:
    data = ChartData(
        type=_find_single(raw_text, "Type"),
        strategy=_find_single(raw_text, "Strategy"),
        authority=_find_single(raw_text, "Authority"),
        profile=_find_single(raw_text, "Profile"),
        definition=_find_single(raw_text, "Definition"),
        incarnation_cross=_find_single(raw_text, "Incarnation Cross"),
        personality=_find_planets_block(raw_text, "Personality"),
        design=_find_planets_block(raw_text, "Design"),
    )
    return data


def _fallback_parse_with_openai(raw_text: str) -> ChartData:
    client = OpenAIClient()
    system_prompt = "Extract Human Design chart data from text. Return strict JSON only. Do not invent missing fields."
    user_prompt = (
        "Extract fields: type, strategy, authority, profile, definition, incarnation_cross, "
        "personality, design, channels, centers.\n"
        "Planet values must be in gate.line format like 44.5.\n"
        f"RAW TEXT:\n{raw_text[:25000]}"
    )
    parsed = client.generate_json(system_prompt, user_prompt)
    return ChartData.model_validate(parsed)


def normalize_chart_data(raw_text: str) -> ChartData:
    parsed = _heuristic_parse(raw_text)
    has_minimum = bool(parsed.type or parsed.profile or parsed.personality or parsed.design)
    if has_minimum:
        return parsed
    return _fallback_parse_with_openai(raw_text)


def chart_to_json(chart_data: ChartData) -> str:
    return json.dumps(chart_data.model_dump(), ensure_ascii=False, indent=2)
