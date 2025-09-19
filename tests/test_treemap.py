import pytest
from treemap import TreeMap

def test_insert_and_update_and_len():
    tm = TreeMap()
    tm.insert(5, "a")
    tm.insert(3, "b")
    tm.insert(7, "c")
    assert len(tm) == 3

    # update existing key shouldn't change size
    tm.insert(5, "z")
    assert len(tm) == 3
    assert tm.get(5) == "z"

def test_contains_and_get_default():
    tm = TreeMap()
    for k, v in [(10, "x"), (5, "y"), (12, "z")]:
        tm.insert(k, v)

    assert 10 in tm
    assert 11 not in tm
    assert tm.get(11) is None
    assert tm.get(11, "missing") == "missing"

def test_sorted_views():
    tm = TreeMap()
    for k, v in [(2, "b"), (1, "a"), (3, "c")]:
        tm.insert(k, v)
    assert tm.keys() == [1, 2, 3]
    assert tm.values() == ["a", "b", "c"]
    assert tm.items() == [(1, "a"), (2, "b"), (3, "c")]
