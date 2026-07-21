import pytest
from pathplus import FileManager


@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    return test_file


@pytest.fixture
def sample_file2(tmp_path):
    test_file = tmp_path / "test2.txt"
    test_file.write_text("Hello, World!2")
    return test_file


def test_compare_different_files(sample_file, sample_file2):
    h = FileManager(sample_file)
    assert h.compare(sample_file2) is False


def test_compare_same_file(sample_file):
    h = FileManager(sample_file)
    assert h.compare(sample_file) is True


def test_compare_with_algorithm(sample_file):
    h = FileManager(sample_file)
    assert h.compare(sample_file, algorithm="sha256") is True


def test_verify(sample_file):
    h = FileManager(sample_file)
    assert h.verify("65a8e27d8879283831b664bd8b7f0ad4") is True
    assert h.verify("00000000000000000000000000000000") is False
