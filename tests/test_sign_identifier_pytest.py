

from utils.methods_database import (
    calculate_lifetime
)


def test_calculate_lifetime():
    var = calculate_lifetime(year=1992, month=7, day=16)
    var2 = calculate_lifetime()
    assert var != var2
