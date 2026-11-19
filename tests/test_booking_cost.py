import pytest
from src.booking_cost import calculate_booking_cost


# Test 1: Valid booking costs
@pytest.mark.parametrize(
    "nights, nightly_rate_cents, expected",
    [
        (2, 5000, 10000), # normal accepted values
        (6, 5000, 30000),  #normal accepted values
        (7, 5000, 35000),  # 7 nights (boundary value for line 9 in booking_cost.py) (identified defect )
        (8, 20000, 160000),  # 8 nights (identified defect)
        (5, 0, 0),   # 0 nightly rate cents (minimum valid nightly rate cents)
        (30, 5000, 150000), # 30 nights (identified defect) (maximum valid nights) 
        (1, 5000, 5000),   # 1 night (minimum valid nights)
    ]
)
def test_booking_cost_valid(nights, nightly_rate_cents, expected):
    result = calculate_booking_cost(nights, nightly_rate_cents)
    assert result == expected


# Test 2: test for type error 
@pytest.mark.parametrize(
    "nights, nightly_rate_cents",
    [
        ("7", 7888), # string instead of int for nights
        (5, "5000"), # string instead of int for nightly_rate_cents
        (True, 5000), # boolean instead of int for nights
    ]
)
def test_booking_cost_type_error(nights, nightly_rate_cents):
    
    with pytest.raises(TypeError):
        calculate_booking_cost(nights, nightly_rate_cents)


# Test 3: test for value error 
@pytest.mark.parametrize(
    "nights, nightly_rate_cents",
    [
        (6, -777),  # negative nightly rate
        (0, 5000),  # zero nights  
        (31, 5000),  # more than 30 nights
    ]
)
def test_booking_cost_value_error(nights, nightly_rate_cents):
    with pytest.raises(ValueError):
        calculate_booking_cost(nights, nightly_rate_cents)