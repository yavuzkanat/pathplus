from pathplus import file
import pytest


h = file.FileManager("./tests/test.txt")

def test_hash_sha256():
    assert h.hash() == "70df2ecf96d91748097e43f4ec254742b0d0f4afd228b391282fa3dfa49ab3bd"

def test_hash_sha512():
    assert h.hash("sha512") == "991cff1b560ce6c47aac26bb57855e9577ab2ad7760a9a7ba178a1d1b03e21e14fe585a11618a37f7fb9f8e684e959d383378a1676687f676a2808edc38d1de1"

def test_hash_md5():
    assert h.hash("md5") == "e9a36a3bd6aca5c982819848300235c0"

def test_hash_missing_alg():
    

    with pytest.raises(ValueError):

        h.hash("md6")
        


def test_hash_missing_file():
    

    with pytest.raises(FileNotFoundError):

        h2 = file.FileManager("./testlaksd")
        h2.hash()
        
    