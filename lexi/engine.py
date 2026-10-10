import re

REPLACEMENTS = {
    "government": "leadership",
    "provided": "gave",
    "assistance": "help",
    "population": "folk",
    "commence": "begin",
    "purchase": "buy",
    "residence": "home",
    "liberty": "freedom",
}

ETYMOLOGIES = {
    "government": {
        "origin": "French, ultimately Greek",
        "replacement_origin": "Old English"
    },
    "provided": {
        "origin": "Latin",
        "replacement_origin": "Old English"
    },
    "assistance": {
        "origin": "French/Latin",
        "replacement_origin": "Old English"
    },
    "population": {
        "origin": "Latin",
        "replacement_origin": "Old English"
    }
}

def rewrite(text: str) -> str:
    def replace(match):
        word = match.group(0)
        replacement = REPLACEMENTS.get(word.lower(), word)

        if word.isupper():
            return replacement.upper()
        if word.istitle():
            return replacement.capitalize()

        return replacement

    return re.sub(r"\b[A-Za-z]+\b", replace, text)

def explain(text: str) -> list[dict]:
    explanations = []

    for match in re.finditer(r"\b[A-Za-z]+\b", text):
        word = match.group(0)
        key = word.lower()

        if key in REPLACEMENTS:
            info = ETYMOLOGIES.get(key, {})

            explanations.append({
                "original": word,
                "replacement": REPLACEMENTS[key],
                "origin": info.get("origin", "Unknown"),
                "replacement_origin": info.get(
                    "replacement_origin", "Unknown"
                )
            })

    return explanations