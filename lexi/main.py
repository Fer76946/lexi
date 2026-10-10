from lexi.llm import rewrite_with_ai


def main():
    print("Welcome to Lexi!")

    while True:
        text = input("\nEnter text (or 'quit'): ")

        if text.lower() == "quit":
            break

        if not text.strip():
            continue

        try:
            intensity = int(input("Rewriting intensity (0-100): "))

            result = rewrite_with_ai(
                text,
                language="english",
                intensity=intensity
            )

            print("\nLexi:", result)

        except ValueError:
            print("Please enter a valid number between 0 and 100.")

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()