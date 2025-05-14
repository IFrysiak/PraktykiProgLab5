"""Calculator tests"""

import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    """Add test"""
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """Subtract test"""
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """Multiply test"""
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """Divide test"""
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "number, expected", [(0, "0"), (1, "1"), (2, "10"), (5, "101"), (100, "1100100")]
)
def test_valid_conversion(number, expected):
    """Test if conversion correct"""
    assert utils.to_binary(number) == expected


@pytest.mark.parametrize("number", [-1, 101, 150])
def test_out_of_range(number):
    """Test if number out of range [0,100]"""
    with pytest.raises(ValueError):
        utils.to_binary(number)


@pytest.mark.parametrize("number", [10.5, 0.1, 99.9])
def test_not_natural_number_float(number):
    """Test for float numbers"""
    with pytest.raises(TypeError):
        utils.to_binary(number)
