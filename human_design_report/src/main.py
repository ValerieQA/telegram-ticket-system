import json
import sys
from pathlib import Path

from build_pdf import build_pdf_report, render_html
from config import BLOCKS_JSON_PATH, CHART_JSON_PATH, RAW_TEXT_PATH, REPORT_HTML_PATH, REPORT_PDF_PATH, VALIDATION_JSON_PATH
from extract_pdf import extract_text_from_pdf, save_raw_text
from generate_blocks import fix_block, generate_report_blocks
from normalize_chart import chart_to_json, normalize_chart_data
from validate_report import validate_report


def _detect_block_name(location: str) -> str:
    low = location.lower()
    if "personality" in low:
        return "personality_planets"
    if "design" in low:
        return "design_planets"
    if any(key in low for key in ["type", "strategy", "authority", "profile", "definition"]):
        return "type_strategy_authority"
    return "overview"


def run_pipeline(pdf_path: Path) -> None:
    raw_text = extract_text_from_pdf(pdf_path)
    save_raw_text(raw_text, RAW_TEXT_PATH)

    chart_data = normalize_chart_data(raw_text)
    chart_json = chart_to_json(chart_data)
    CHART_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    CHART_JSON_PATH.write_text(chart_json, encoding="utf-8")

    blocks = generate_report_blocks(chart_json)
    validation = validate_report(chart_data, blocks)

    if not validation.valid:
        block_errors: dict[str, list[dict]] = {}
        for issue in validation.errors:
            block_name = _detect_block_name(issue["location"])
            block_errors.setdefault(block_name, []).append(issue)

        for block_name, issues in block_errors.items():
            blocks[block_name] = fix_block(chart_json, blocks[block_name], issues, block_name)

        validation = validate_report(chart_data, blocks)

    BLOCKS_JSON_PATH.write_text(json.dumps(blocks, ensure_ascii=False, indent=2), encoding="utf-8")
    VALIDATION_JSON_PATH.write_text(json.dumps(validation.__dict__, ensure_ascii=False, indent=2), encoding="utf-8")

    html = render_html(blocks, chart_data.model_dump())
    REPORT_HTML_PATH.write_text(html, encoding="utf-8")
    build_pdf_report(blocks, chart_data.model_dump(), REPORT_PDF_PATH)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python src/main.py input/client_chart.pdf")

    run_pipeline(Path(sys.argv[1]))
