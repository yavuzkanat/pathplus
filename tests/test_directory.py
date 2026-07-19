from pathplus import DirectoryManager
import pytest




def test_tree(tmp_path):
    # Geçici dizinde dosyalar oluştur
    (tmp_path / "a.txt").write_text("Hello")
    (tmp_path / "b.txt").write_text("World")

    manager = DirectoryManager(tmp_path)

    tree = manager.tree()

    assert str(tmp_path) in tree
    assert sorted(tree[str(tmp_path)]) == ["a.txt", "b.txt"]