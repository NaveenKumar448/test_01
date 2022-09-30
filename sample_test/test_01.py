import pytest

def test_01():
  assert True

def test_02():
  assert "a" in "apple"

@pytest.mark.xfail
def test_04():
  assert False
