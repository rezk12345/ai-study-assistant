# AI Study Assistant

AI Study Assistant is a beginner-friendly terminal application built with pure Python (standard library only).  
It helps you study from text files by summarizing content, generating quiz questions, tracking study sessions, and saving notes.

## Features

- Load any `.txt` file from your computer
- Summarize loaded text using simple frequency-based logic
- Generate fill-in-the-blank quiz questions
- Start and stop a study timer
- Save study notes to a file
- Use a clear terminal menu for navigation

## Project Structure

```text
AI Study Assistant/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── summarizer.py
│   ├── quiz_generator.py
│   └── session_tracker.py
├── data/
│   └── example_text.txt
├── notes/
│   └── (created automatically when saving notes)
└── README.md
```

## Requirements

- Python 3.10+ (recommended)
- No external packages required

## How to Run

1. Open terminal in the project folder.
2. Run:

```bash
python main.py
```

3. Use menu options to:
   - Load a text file (try `data/example_text.txt`)
   - Summarize text
   - Generate quiz
   - Track study sessions
   - Save notes

## Notes and Error Handling

- If you enter an invalid file path, the program displays a friendly error.
- If a file is empty or no text is loaded yet, the app guides you with clear messages.
- Notes are appended to `notes/study_notes.txt`.

## Educational Purpose

The summarizer and quiz generator use simple local logic to stay easy to understand.  
This project is designed as a clean learning example with professional structure.
