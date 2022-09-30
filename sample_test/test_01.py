import pytest

def test_01(run_setup):
  assert run_setup == 11

# def test_02():
#   assert "a" in "apple"

# @pytest.mark.xfailif
# def test_04():
#   assert False
