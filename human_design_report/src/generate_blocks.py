from config import PROMPTS_DIR
from openai_client import OpenAIClient


def _load_prompt(filename: str) -> str:
    return (PROMPTS_DIR / filename).read_text(encoding="utf-8")


def _build_user_prompt(chart_json: str, extra: str = "") -> str:
    return (
        "Use only source JSON as truth. If data is missing, say it is missing.\n"
        "Language: Russian. Tone: soft, non-dogmatic, practical.\n\n"
        f"Source chart JSON:\n{chart_json}\n\n{extra}"
    ).strip()


def generate_block(client: OpenAIClient, prompt_file: str, chart_json: str, extra: str = "") -> str:
    system_prompt = _load_prompt(prompt_file)
    return client.generate_text(system_prompt, _build_user_prompt(chart_json, extra))


def generate_report_blocks(chart_json: str) -> dict[str, str]:
    client = OpenAIClient()
    return {
        "overview": generate_block(client, "overview.md", chart_json),
        "type_strategy_authority": generate_block(client, "type_strategy_authority.md", chart_json),
        "personality_planets": generate_block(client, "planet_block.md", chart_json, "Write only Personality planets."),
        "design_planets": generate_block(client, "planet_block.md", chart_json, "Write only Design planets."),
        "centers": generate_block(client, "centers.md", chart_json),
        "channels": generate_block(client, "channels.md", chart_json),
        "business_social": generate_block(client, "business_social.md", chart_json),
        "final_summary": generate_block(client, "final_summary.md", chart_json),
    }


def fix_block(chart_json: str, block_text: str, errors: list[dict], block_name: str) -> str:
    client = OpenAIClient()
    system_prompt = (
        "You are fixing one Human Design report block. "
        "Fix only listed errors. Do not add new gate.line values. Keep Russian language."
    )
    user_prompt = (
        f"Block name: {block_name}\n"
        f"Chart JSON:\n{chart_json}\n\n"
        f"Current block text:\n{block_text}\n\n"
        f"Errors:\n{errors}\n\n"
        "Instruction: fix only these errors, do not rewrite unrelated parts."
    )
    return client.generate_text(system_prompt, user_prompt)
