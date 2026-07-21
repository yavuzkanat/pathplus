# 0.2.0 (2026.07.21)

## File Manager

### Added Features

* `hashes()` to return all supported digests
* `exists()` to verify path presence
* richer metadata returned by `info()` including directory, timestamps, stem, and file type flags
* `size_bytes()` for raw size in bytes
* `read_text()`, `read_bytes()`, and `preview()` for file content access

## Directory Manager

### Added Features

* `files()` and `file_count()` for recursive file listing
* `directory_count()` to count subdirectories
* `find()` to locate paths by glob pattern
* `largest_files()` to discover the largest files in a directory
* `total_size_bytes()` and `is_empty()`

#  0.1.2 (2026.07.21)

##  File Manager

### Fixed Bugs

* The hash method has been rewritten again in order to follow the "DRY" rules and use chunks to make it RAM-friendly.

# 0.1.1 (2026-07-19)

## File Manager

### Added New Methods

* hash
* info
* compare
* size

### Directory Manager

* tree
* total_size

## Fixed Bugs

* Some bugs have been fixed which can't work well in methods.

# 0.1.0 (2026-07-19)

**Birthday !**
