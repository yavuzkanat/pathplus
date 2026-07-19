import pytest
from pathplus import FileManager

# This fixture creates a predictable file in a temporary directory for your hashing tests
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


def test_compare(sample_file,sample_file2):
    # Pass the dynamic temporary file path to your FileManager
    h = FileManager(str(sample_file))
    assert False == h.compare(sample_file2)
    

def test_compare2(sample_file,sample_file2):
    # Pass the dynamic temporary file path to your FileManager
    h = FileManager(str(sample_file))
    assert True == h.compare(sample_file)
    

def test_verify(sample_file):
    h = FileManager(str(sample_file))
    assert True == h.verify("65a8e27d8879283831b664bd8b7f0ad4")  
