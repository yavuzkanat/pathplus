from pathlib import Path
from pathplus import DirectoryManager


def test_tree(tmp_path):
    (tmp_path / "a.txt").write_text("Hello")
    (tmp_path / "b.txt").write_text("World")

    manager = DirectoryManager(tmp_path)
    tree = manager.tree()

    assert str(tmp_path.resolve()) in tree
    assert sorted(tree[str(tmp_path.resolve())]) == ["a.txt", "b.txt"]


def test_tree_includes_empty_directories(tmp_path):
    (tmp_path / "a.txt").write_text("Hello")
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()

    manager = DirectoryManager(tmp_path)
    tree = manager.tree(include_empty_dirs=True)

    assert str(tmp_path.resolve()) in tree
    assert str(empty_dir.resolve()) in tree
    assert tree[str(empty_dir.resolve())] == []


def test_file_counts_and_find(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    (src_dir / "main.py").write_text("print('hello')")
    (src_dir / "utils.py").write_text("print('utils')")
    (tmp_path / "README.md").write_text("docs")

    manager = DirectoryManager(tmp_path)
    files = manager.files()

    assert len(files) == 3
    assert manager.file_count() == 3
    assert manager.directory_count() == 1
    assert any(path.name == "main.py" for path in manager.find("*.py"))
    assert any(path.name == "README.md" for path in manager.find("README.*", recursive=False))


def test_total_size_and_largest_files(tmp_path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("A" * 10)
    b.write_text("B" * 20)

    manager = DirectoryManager(tmp_path)
    assert manager.total_size(formatted=False) == 30
    assert manager.total_size() == "30 Bytes"

    largest = manager.largest_files(limit=1)
    assert largest[0][0] == b.resolve()
    assert largest[0][1] == 20


def test_is_empty(tmp_path):
    manager = DirectoryManager(tmp_path)
    assert manager.is_empty() is True

    (tmp_path / "file.txt").write_text("data")
    assert manager.is_empty() is False
