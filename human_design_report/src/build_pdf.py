from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from config import TEMPLATES_DIR


def render_html(blocks: dict[str, str], chart_data: dict) -> str:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("report.html")
    return template.render(blocks=blocks, chart=chart_data)


def build_pdf_report(blocks: dict[str, str], chart_data: dict, output_pdf_path: Path) -> None:
    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
    html = render_html(blocks, chart_data)
    HTML(string=html).write_pdf(str(output_pdf_path))
