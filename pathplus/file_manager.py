from __future__ import annotations

from datetime import datetime
from hashlib import md5, sha256, sha512
from pathlib import Path

from .utils import format_size


class FileManager:
    _ALGORITHMS = {
        "sha256": sha256,
        "sha512": sha512,
        "md5": md5,
    }

    SUPPORTED_ALGORITHMS = tuple(_ALGORITHMS.keys())

    def __init__(self, path: str | Path):
        self._path = Path(path)

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, target_path: str | Path) -> None:
        self._path = Path(target_path)

    def exists(self) -> bool:
        return self._path.exists()

    def hash(self, algorithm: str = "md5", file: str | Path | None = None) -> str:
        """Compute a file hash using the specified algorithm."""
        try:
            hash_func = self._ALGORITHMS[algorithm]()
        except KeyError as exc:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc

        current_path = Path(file) if file is not None else self._path
        with open(current_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hash_func.update(chunk)

        return hash_func.hexdigest()

    def hashes(self) -> dict[str, str]:
        """Return a dictionary of hashes for all supported algorithms."""
        return {algorithm: self.hash(algorithm) for algorithm in self.SUPPORTED_ALGORITHMS}

    def info(self) -> dict[str, str | Path | int | bool]:
        """Return metadata information for the file."""
        stat = self._path.stat()
        return {
            "name": self._path.name,
            "path": self._path.resolve(),
            "directory": self._path.parent.resolve(),
            "size": stat.st_size,
            "size_formatted": format_size(stat.st_size),
            "created_time": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
            "modified_time": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
            "accessed_time": datetime.fromtimestamp(stat.st_atime).strftime("%Y-%m-%d %H:%M:%S"),
            "extension": self._path.suffix,
            "stem": self._path.stem,
            "is_file": self._path.is_file(),
            "is_dir": self._path.is_dir(),
            "is_symlink": self._path.is_symlink(),
        }

    def compare(self, other: str | Path, algorithm: str = "md5") -> bool:
        """Compare this file against another file using the selected hash algorithm."""
        return self.hash(algorithm) == self.hash(algorithm, file=other)

    def verify(self, hash_value: str, algorithm: str = "md5") -> bool:
        """Verify the current file against a known hash value."""
        return self.hash(algorithm) == hash_value

    def size_bytes(self) -> int:
        """Return the file size in bytes."""
        return self._path.stat().st_size

    def size(self) -> str:
        """Return the file size in a human readable string."""
        return format_size(self.size_bytes())

    def read_bytes(self) -> bytes:
        """Return the raw bytes of the file."""
        return self._path.read_bytes()

    def read_text(self, encoding: str = "utf-8", errors: str = "strict") -> str:
        """Return the file contents decoded as text."""
        return self._path.read_text(encoding=encoding, errors=errors)

    def preview(
        self,
        lines: int = 10,
        max_chars: int = 500,
        encoding: str = "utf-8",
        errors: str = "replace",
    ) -> str:
        """Return a short text preview for the file."""
        if lines <= 0:
            raise ValueError("lines must be a positive integer")
        if max_chars <= 0:
            raise ValueError("max_chars must be a positive integer")

        text = self.read_text(encoding=encoding, errors=errors)
        if not text:
            return ""

        preview_lines = text.splitlines()
        preview_text = "\n".join(preview_lines[:lines])

        if len(preview_text) > max_chars:
            return preview_text[:max_chars].rstrip("\n") + "..."

        if len(text) > len(preview_text):
            return preview_text + "\n..." if preview_text else "..."

        return preview_text
