from __future__ import annotations

import os
from pathlib import Path

from .utils import format_size


class DirectoryManager:
    def __init__(self, path: str | Path):
        self._path = Path(path)

    def tree(self, include_empty_dirs: bool = False) -> dict[str, list[str]]:
        """Generate a dictionary mapping directories to the files they directly contain."""
        if not self._path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self._path}")

        data: dict[str, list[str]] = {}
        for root, dirs, files in os.walk(self._path.resolve()):
            if files or include_empty_dirs:
                data[str(Path(root).resolve())] = sorted(files)
        return data

    def files(self, recursive: bool = True) -> list[Path]:
        """Return the files contained in the directory."""
        if not self._path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self._path}")

        if recursive:
            return sorted([path for path in self._path.rglob("*") if path.is_file()])

        return sorted([path for path in self._path.iterdir() if path.is_file()])

    def file_count(self, recursive: bool = True) -> int:
        """Return the number of files in the directory."""
        return len(self.files(recursive=recursive))

    def directory_count(self, recursive: bool = True) -> int:
        """Return the number of subdirectories."""
        if not self._path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self._path}")

        if recursive:
            return sum(1 for path in self._path.rglob("*") if path.is_dir())

        return sum(1 for path in self._path.iterdir() if path.is_dir())

    def find(self, pattern: str = "*", recursive: bool = True) -> list[Path]:
        """Find paths matching a glob pattern."""
        if not self._path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self._path}")

        if recursive:
            return sorted(self._path.rglob(pattern))

        return sorted(self._path.glob(pattern))

    def largest_files(self, limit: int = 5) -> list[tuple[Path, int]]:
        """Return the largest files by size."""
        files = self.files(recursive=True)
        file_sizes = [(path, path.stat().st_size) for path in files]
        return sorted(file_sizes, key=lambda item: item[1], reverse=True)[:limit]

    def total_size_bytes(self) -> int:
        """Return the total size of all files inside the directory."""
        return sum(path.stat().st_size for path in self.files(recursive=True))

    def total_size(self, formatted: bool = True) -> str | int:
        """Return the total directory size, optionally formatted."""
        size = self.total_size_bytes()
        return format_size(size) if formatted else size

    def is_empty(self) -> bool:
        """Return True when the directory contains no files or subdirectories."""
        if not self._path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self._path}")
        return not any(self._path.iterdir())        
        
        
        
