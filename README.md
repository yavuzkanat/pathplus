# SmartPath

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

### Usage 

```python
from pathplus import FileManager

file = FileManager("example.txt")

print(file.hash())

print(file.info())
```

```python
from pathplus import DirectoryManager

directory = DirectoryManager("project")

print(directory.tree())
```

## Release Notes

### V.0.1.0

* File Hashing (SHA256, MD5, SHA512)

* File Information Helper

* Tree Information For Directories
