from pathlib import Path

import fitz


def extract_text_from_pdf(pdf_path: Path) -> str:
    pages: list[str] = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            pages.append(page.get_text("text"))
    return "\n".join(pages)


def save_raw_text(raw_text: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(raw_text, encoding="utf-8")
