"""Quiz generation helpers based on loaded study text."""

import re


def generate_quiz_questions(text: str, max_questions: int = 5) -> list[dict]:
    """
    Generate simple fill-in-the-blank style quiz questions.

    Args:
        text: Source text to build questions from.
        max_questions: Maximum number of questions to return.

    Returns:
        A list of dictionaries with 'question' and 'answer' keys.
    """
    clean_text = text.strip()
    if not clean_text:
        return []

    sentences = re.split(r"(?<=[.!?])\s+", clean_text)
    sentences = [s.strip() for s in sentences if len(s.split()) >= 6]

    questions = []
    for sentence in sentences:
        words = re.findall(r"[A-Za-z]+", sentence)
        if len(words) < 6:
            continue

        # Select a meaningful candidate word (long enough, likely informative).
        candidate_words = [word for word in words if len(word) > 4]
        if not candidate_words:
            continue

        answer = candidate_words[0]
        question_text = sentence.replace(answer, "_____", 1)
        questions.append({"question": question_text, "answer": answer})

        if len(questions) >= max_questions:
            break

    return questions
