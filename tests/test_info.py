import pytest
from pathplus import FileManager

# This fixture creates a predictable file in a temporary directory for your hashing tests
@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    return test_file


def test_info(tmp_path):
    info = FileManager(tmp_path).info()
    print(info)
    assert True

def test_size(tmp_path):
    info = FileManager(tmp_path)
    print(info.size())