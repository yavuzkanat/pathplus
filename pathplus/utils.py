from __future__ import annotations

from pathlib import Path


def format_size(bytes_size: int, decimal_places: int = 2) -> str:
    """Format a byte count as a human-readable string."""
    if bytes_size < 1_000:
        return f"{bytes_size} Bytes"
    if bytes_size < 1_000_000:
        return f"{bytes_size / 1_000:.{decimal_places}f} KB"
    if bytes_size < 1_000_000_000:
        return f"{bytes_size / 1_000_000:.{decimal_places}f} MB"
    return f"{bytes_size / 1_000_000_000:.{decimal_places}f} GB"


def resolve_path(path: str | Path) -> Path:
    """Resolve a path-like object to an absolute Path."""
    return Path(path).resolve()
