import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

# --- Test booking_cost ---
def test_booking_cost_standard():
    assert booking_cost("standard", 2, 2, False) == 4000

def test_booking_cost_deluxe_peak_season():
    # 3500 + 875 = 4375 * 3 = 13125
    assert booking_cost("deluxe", 3, 2, True) == 13125

def test_booking_cost_suite_extra_guests():
    # 6000 * 2 + (4 - 2) * 500 * 2 = 12000 + 2000 = 14000
    assert booking_cost("suite", 2, 4, False) == 14000

def test_booking_cost_long_stay_discount():
    # standard: 2000 * 7 = 14000; discount: 14000 // 10 = 1400; total = 12600
    assert booking_cost("standard", 7, 2, False) == 12600

def test_booking_cost_unknown_room():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("penthouse", 2, 2, False)

def test_booking_cost_invalid_nights():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)

# --- Test cancellation_refund ---
def test_cancellation_refund_full():
    assert cancellation_refund(1000, 10, False) == 1000
    assert cancellation_refund(1000, 7, True) == 1000

def test_cancellation_refund_moderate():
    assert cancellation_refund(1000, 5, False) == 500
    assert cancellation_refund(1000, 2, True) == 750

def test_cancellation_refund_late():
    assert cancellation_refund(1000, 1, False) == 0
    assert cancellation_refund(1000, 0, True) == 250

# --- Test room_upgrade ---
def test_room_upgrade_no_rooms_free():
    assert room_upgrade("standard", True, 0) == "standard"

def test_room_upgrade_standard_member():
    assert room_upgrade("standard", True, 3) == "deluxe"

def test_room_upgrade_standard_non_member():
    assert room_upgrade("standard", False, 3) == "standard"

def test_room_upgrade_deluxe_member():
    assert room_upgrade("deluxe", True, 3) == "suite"

def test_room_upgrade_deluxe_non_member():
    assert room_upgrade("deluxe", False, 3) == "deluxe"

def test_room_upgrade_suite():
    assert room_upgrade("suite", True, 3) == "suite"
    assert room_upgrade("suite", False, 3) == "suite"

def test_room_upgrade_other_room():
    assert room_upgrade("executive", True, 3) == "executive"
