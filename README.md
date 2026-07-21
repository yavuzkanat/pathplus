# Pathplus

A modern Python library for file and directory management built on top of pathlib.

## Goals

- Pythonic API
- Cross-platform
- Type-safe
- Well tested

## Setup

```bash
pip install pathplus
```

## Usage

```python
from pathplus import FileManager, DirectoryManager

file = FileManager("example.txt")
print(file.hash())
print(file.hash("sha256"))
print(file.hashes())
print(file.size())
print(file.size_bytes())
print(file.read_text())
print(file.read_bytes()[:16])
print(file.preview(lines=3, max_chars=120))
print(file.info())

folder = DirectoryManager("project")
print(folder.tree())
print(folder.files())
print(folder.file_count())
print(folder.total_size())
print(folder.find("*.py"))
```

## Features

- Compute file hashes with supported algorithms: `md5`, `sha256`, `sha512`
- Compare files and verify known hash values
- Inspect file metadata including creation, modification, and access times
- List files in a directory recursively or non-recursively
- Count files and subdirectories
- Find files by glob pattern
- Report total directory size and largest files

## Release Notes

### V.0.2.0

* Added `FileManager.hashes()` and `FileManager.exists()`
* Added rich file metadata in `FileManager.info()`
* Added `FileManager.size_bytes()` for raw byte size
* Added `DirectoryManager.files()`, `file_count()`, `directory_count()`, `find()`, `largest_files()`, `total_size_bytes()`, and `is_empty()`
* Added `DirectoryManager.tree(include_empty_dirs=True)`
* Updated package metadata and tests

### V.0.1.0

* File Hashing (SHA256, MD5, SHA512)
* File Information Helper
* Tree Information For Directories
