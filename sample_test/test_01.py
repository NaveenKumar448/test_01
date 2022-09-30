import pytest

@pytest.mark.parametrize("a, b", [(2,8), (4,6)])
def test_01(a, b, run_setup):
  assert run_setup == a + b

# def test_02():
#   assert "a" in "apple"

# @pytest.mark.xfailif
# def test_04():
#   assert False
