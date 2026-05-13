# Human Design Report MVP

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment

Create `.env` in project root:

```env
OPENAI_API_KEY=...
```

## Run

```bash
python src/main.py input/client_chart.pdf
```

## Output

- `output/client_report.pdf`
- `output/chart_data.json`
- `output/validation_report.json`
- `output/raw_text.txt`

## Notes

- Source of truth is the bodygraph PDF.
- GPT is used only for extraction fallback and writing narrative blocks.
- Validator checks that report values match extracted chart values.
