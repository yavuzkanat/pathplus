import pytest
from pathplus import DirectoryManager

# This fixture creates a predictable file in a temporary directory for your hashing tests
@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    return test_file

def tree_size(sample_file):
        test = DirectoryManager(".")
        
        print("test :",test.tree())
