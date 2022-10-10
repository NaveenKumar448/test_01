import pytest

@pytest.mark.parametrize("ex_val", [(True), (1)])
def test_01(ex_val):
    assert ex_val == True