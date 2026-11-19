import pytest
from src.booking_refund import is_refundable

@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate, expected",[
        (47, True, False), # just below refund threshold 
        (48, True, True),  # exactly at threshold (identified defect)
        (49, True, True),  # just above refund threshold 
        (72, False, False), # normal values input
    ]
)

def test_is_refundable_valid(hours_before_checkin, flexible_rate, expected):
    result = is_refundable(hours_before_checkin, flexible_rate)
    assert result is expected

#------------------------------------------
#test for type error
@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate",[
        (5, '56'),  # string instead of bool for flexible_rate
        ("48",True), # string instead of int for hours_before_checkin
        (48, 1), # integer instead of bool for flexible_rate

    ]
)
 
def test_is_refundable_type_error(hours_before_checkin, flexible_rate):
    with pytest.raises(TypeError):
        is_refundable(hours_before_checkin, flexible_rate)

#------------------------------------------
#test for value error 
def test_is_refundable_value_error():
    hours_before_checkin = -7
    flexible_rate = True
    with pytest.raises(ValueError):
        is_refundable(hours_before_checkin, flexible_rate)
