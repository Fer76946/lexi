from lexi.engine import rewrite, explain

print("Welcome to Lexi!")

while True:
    text = input("\nEnter English text (or 'quit'): ")

    if text.lower() == "quit":
        break

    result = rewrite(text)
    explanations = explain(text)

    print("\nLexi:", result)

    if explanations:
        print("\nSubstitution explanations:")

        for item in explanations:
            print(
                f"- {item['original']} → {item['replacement']}"
            )
            print(
                f"  Origin: {item['origin']}"
            )
            print(
                f"  Replacement origin: {item['replacement_origin']}"
            )