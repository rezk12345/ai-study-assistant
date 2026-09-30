"""Terminal entry point for the AI Study Assistant project."""

from pathlib import Path

from modules.quiz_generator import generate_quiz_questions
from modules.session_tracker import SessionTracker
from modules.summarizer import summarize_text


NOTES_FILE = Path("notes") / "study_notes.txt"


def print_menu() -> None:
    """Display the main menu options."""
    print("\n=== AI Study Assistant ===")
    print("1. Load text file")
    print("2. Summarize loaded text")
    print("3. Generate quiz from loaded text")
    print("4. Start study session")
    print("5. Stop study session")
    print("6. View total study time")
    print("7. Save notes")
    print("8. Exit")


def load_text_file() -> str:
    """Load text content from a user-provided file path."""
    file_path = input("Enter path to the text file: ").strip()
    if not file_path:
        print("No file path entered.")
        return ""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return ""
    except OSError as error:
        print(f"Error reading file: {error}")
        return ""

    if not content:
        print("The file is empty.")
        return ""

    print("File loaded successfully.")
    return content


def run_quiz(text: str) -> None:
    """Generate and run an interactive quiz from text."""
    questions = generate_quiz_questions(text)
    if not questions:
        print("Not enough content to generate quiz questions.")
        return

    print("\n=== Quiz Time ===")
    score = 0

    for index, item in enumerate(questions, start=1):
        print(f"\nQ{index}: {item['question']}")
        user_answer = input("Your answer: ").strip()
        expected = item["answer"]

        if user_answer.lower() == expected.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. Correct answer: {expected}")

    print(f"\nFinal score: {score}/{len(questions)}")


def save_notes() -> None:
    """Save user notes to a notes file."""
    print("\nEnter your notes (type 'DONE' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)

    note_text = "\n".join(lines).strip()
    if not note_text:
        print("No notes entered.")
        return

    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(note_text + "\n" + ("-" * 40) + "\n")
        print(f"Notes saved to: {NOTES_FILE}")
    except OSError as error:
        print(f"Error saving notes: {error}")


def main() -> None:
    """Main loop for handling user input and features."""
    loaded_text = ""
    tracker = SessionTracker()

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            loaded_text = load_text_file()
        elif choice == "2":
            if not loaded_text:
                print("Load a text file first.")
            else:
                print("\n=== Summary ===")
                print(summarize_text(loaded_text))
        elif choice == "3":
            if not loaded_text:
                print("Load a text file first.")
            else:
                run_quiz(loaded_text)
        elif choice == "4":
            print(tracker.start_session())
        elif choice == "5":
            print(tracker.stop_session())
        elif choice == "6":
            print(f"Total study time: {tracker.get_total_time()}")
        elif choice == "7":
            save_notes()
        elif choice == "8":
            if tracker.is_running():
                print("A session is active. Stopping it before exit.")
                print(tracker.stop_session())
            print("Goodbye. Keep studying!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
