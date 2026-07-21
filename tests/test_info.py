import pytest
from pathplus import FileManager


@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    return test_file


def test_info_returns_expected_values(sample_file):
    manager = FileManager(sample_file)
    info = manager.info()

    assert info["name"] == "test.txt"
    assert info["path"] == sample_file.resolve()
    assert info["directory"] == sample_file.parent.resolve()
    assert info["size"] == 13
    assert info["size_formatted"] == "13 Bytes"
    assert info["extension"] == ".txt"
    assert info["stem"] == "test"
    assert info["is_file"] is True
    assert info["is_dir"] is False


def test_size_bytes_and_formatted(sample_file):
    manager = FileManager(sample_file)
    assert manager.size_bytes() == 13
    assert manager.size() == "13 Bytes"


def test_exists(sample_file):
    manager = FileManager(sample_file)
    assert manager.exists() is True

    missing = FileManager(sample_file.parent / "missing.txt")
    assert missing.exists() is False


def test_read_bytes_and_text(sample_file):
    manager = FileManager(sample_file)
    assert manager.read_bytes() == b"Hello, World!"
    assert manager.read_text() == "Hello, World!"


def test_preview_returns_first_lines(sample_file):
    manager = FileManager(sample_file)
    preview = manager.preview(lines=1, max_chars=100)
    assert preview == "Hello, World!"


def test_preview_truncates_to_max_chars(tmp_path):
    long_file = tmp_path / "long.txt"
    long_file.write_text("a\n" * 50)
    manager = FileManager(long_file)

    preview = manager.preview(lines=5, max_chars=10)
    assert preview.endswith("...")
    assert len(preview) <= 13


def test_preview_invalid_arguments(sample_file):
    manager = FileManager(sample_file)
    with pytest.raises(ValueError):
        manager.preview(lines=0)
    with pytest.raises(ValueError):
        manager.preview(max_chars=0)
