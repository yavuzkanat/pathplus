import pytest
from pathplus import FileManager


@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    return test_file


def test_hash_sha256(sample_file):
    h = FileManager(sample_file)
    assert h.hash("sha256") == "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"


def test_hash_sha512(sample_file):
    h = FileManager(sample_file)
    assert h.hash("sha512") == "374d794a95cdcfd8b35993185fef9ba368f160d8daf432d08ba9f1ed1e5abe6cc69291e0fa2fe0006a52570ef18c19def4e617c33ce52ef0a6e5fbe318cb0387"


def test_hash_md5(sample_file):
    h = FileManager(sample_file)
    assert h.hash("md5") == "65a8e27d8879283831b664bd8b7f0ad4"


def test_hashes_returns_all_algorithms(sample_file):
    h = FileManager(sample_file)
    hashes = h.hashes()

    assert hashes["md5"] == "65a8e27d8879283831b664bd8b7f0ad4"
    assert hashes["sha256"] == "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
    assert hashes["sha512"].startswith("374d794a95cdcfd8b35993")


def test_hash_missing_alg(sample_file):
    h = FileManager(sample_file)
    with pytest.raises(ValueError):
        h.hash("md6")


def test_hash_missing_file():
    with pytest.raises(FileNotFoundError):
        h2 = FileManager("./testlaksd")
        h2.hash()
