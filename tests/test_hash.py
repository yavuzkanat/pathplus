import pytest
from pathplus import file_manager

# This fixture creates a predictable file in a temporary directory for your hashing tests
@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    return test_file


# --- Hashing Tests using the tmp_path fixture ---

def test_hash_sha256(sample_file):
    # Pass the dynamic temporary file path to your FileManager
    h = file_manager.FileManager(str(sample_file))
    assert h.hash() == "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"


def test_hash_sha512(sample_file):
    h = file_manager.FileManager(str(sample_file))
    assert h.hash("sha512") == "374d794a95cdcfd8b35993185fef9ba368f160d8daf432d08ba9f1ed1e5abe6cc69291e0fa2fe0006a52570ef18c19def4e617c33ce52ef0a6e5fbe318cb0387"


def test_hash_md5(sample_file):
    h = file_manager.FileManager(str(sample_file))
    assert h.hash("md5") == "65a8e27d8879283831b664bd8b7f0ad4"


# --- Error Handling Tests ---

def test_hash_missing_alg(sample_file):
    h = file_manager.FileManager(str(sample_file))
    with pytest.raises(ValueError):
        h.hash("md6")


def test_hash_missing_file():
    # This remains unchanged since it deliberately targets a non-existent file
    with pytest.raises(FileNotFoundError):
        h2 = file_manager.FileManager("./testlaksd")
        h2.hash()