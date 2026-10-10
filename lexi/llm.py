import os

from dotenv import load_dotenv
from openai import OpenAI
from lexi.languages import LANGUAGE_PROFILES

load_dotenv()

client = OpenAI()


def rewrite_with_ai(
    text: str,
    language: str = "english",
    intensity: int = 50
) -> str:

    if language not in LANGUAGE_PROFILES:
        raise ValueError("Unsupported language")

    if not 0 <= intensity <= 100:
        raise ValueError("Intensity must be between 0 and 100")

    if intensity == 0:
        return text

    profile = LANGUAGE_PROFILES[language]

    instructions = f"""
    You are Lexi, an etymology-aware rewriting assistant.

    Language: {profile['name']}
    Constraint: {profile['instructions']}

    Rewriting intensity: {intensity}/100.

    Low intensity:
    Make minimal changes and prioritize natural language.

    High intensity:
    Strongly favor the specified etymological vocabulary.
    Allow descriptive compounds when necessary.

    Preserve the original meaning and grammatical correctness.
    Return only the rewritten text.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=text
    )

    return response.output_text