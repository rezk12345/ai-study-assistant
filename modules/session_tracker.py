"""Simple study session timing utilities."""

from datetime import datetime


class SessionTracker:
    """Track a single active study session and total elapsed time."""

    def __init__(self) -> None:
        self._start_time: datetime | None = None
        self.total_seconds: float = 0.0

    def start_session(self) -> str:
        """Start a session if not already running."""
        if self._start_time is not None:
            return "A study session is already running."

        self._start_time = datetime.now()
        return f"Session started at {self._start_time.strftime('%H:%M:%S')}."

    def stop_session(self) -> str:
        """Stop current session and add elapsed time to total."""
        if self._start_time is None:
            return "No active session. Start one first."

        end_time = datetime.now()
        elapsed = (end_time - self._start_time).total_seconds()
        self.total_seconds += elapsed
        self._start_time = None

        return (
            f"Session stopped. This session: {format_seconds(elapsed)}. "
            f"Total study time: {self.get_total_time()}."
        )

    def is_running(self) -> bool:
        """Return True if a study session is currently active."""
        return self._start_time is not None

    def get_total_time(self) -> str:
        """Get the formatted total study time."""
        current_total = self.total_seconds
        if self._start_time is not None:
            current_total += (datetime.now() - self._start_time).total_seconds()
        return format_seconds(current_total)


def format_seconds(seconds: float) -> str:
    """Convert seconds into HH:MM:SS format."""
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
