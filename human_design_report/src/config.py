from pathlib import Path

# Base directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
PROMPTS_DIR = PROJECT_ROOT / "prompts"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

# OpenAI settings
OPENAI_MODEL = "gpt-4.1-mini"
OPENAI_TEMPERATURE = 0.2

# Output files
RAW_TEXT_PATH = OUTPUT_DIR / "raw_text.txt"
CHART_JSON_PATH = OUTPUT_DIR / "chart_data.json"
VALIDATION_JSON_PATH = OUTPUT_DIR / "validation_report.json"
BLOCKS_JSON_PATH = OUTPUT_DIR / "report_blocks.json"
REPORT_HTML_PATH = OUTPUT_DIR / "client_report.html"
REPORT_PDF_PATH = OUTPUT_DIR / "client_report.pdf"
