"""Text summarization helpers using only standard Python."""

import re
from collections import Counter


def summarize_text(text: str, sentence_count: int = 3) -> str:
    """
    Create a simple summary by scoring sentences with word frequency.

    Args:
        text: Full source text.
        sentence_count: Maximum number of sentences in the summary.

    Returns:
        A concise summary string.
    """
    clean_text = text.strip()
    if not clean_text:
        return "No content available to summarize."

    # Split into sentences using punctuation.
    sentences = re.split(r"(?<=[.!?])\s+", clean_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return "No clear sentences found to summarize."

    # Build a simple word-frequency model.
    words = re.findall(r"[a-zA-Z]+", clean_text.lower())
    if not words:
        return "No words found to summarize."

    stop_words = {
        "the", "a", "an", "and", "or", "but", "if", "then", "is", "are", "was",
        "were", "be", "been", "being", "to", "of", "in", "on", "for", "with",
        "as", "at", "by", "from", "that", "this", "it", "its", "into", "about",
        "you", "your", "we", "our", "they", "their", "he", "she", "his", "her"
    }
    filtered_words = [word for word in words if word not in stop_words]
    if not filtered_words:
        filtered_words = words

    frequency = Counter(filtered_words)

    # Score each sentence by summing word frequencies.
    sentence_scores = []
    for sentence in sentences:
        sentence_words = re.findall(r"[a-zA-Z]+", sentence.lower())
        score = sum(frequency[word] for word in sentence_words if word in frequency)
        sentence_scores.append((sentence, score))

    # Keep top scoring sentences and preserve original order.
    top_n = max(1, min(sentence_count, len(sentences)))
    top_sentences = sorted(sentence_scores, key=lambda pair: pair[1], reverse=True)[:top_n]
    selected = {sentence for sentence, _ in top_sentences}
    ordered_summary = [sentence for sentence in sentences if sentence in selected]

    return " ".join(ordered_summary)
