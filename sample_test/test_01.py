import pytest

@pytest.mark.parametrize("a, b", [(2,8), (4,6)])
def test_01(a, b, run_setup):
  assert run_setup == a + b



# @pytest.mark.xfailif
# def test_04():
#   assert False
