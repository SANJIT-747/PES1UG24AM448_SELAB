from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label
import pytest

@given(st.text() | st.none())
def test_nights_stayed_no_crash(s):
    try:
        nights_stayed(s)
    except (ValueError, TypeError):
        pass # Properly handled input validation error
    except Exception as e:
        pytest.fail(f"nights_stayed crashed with unexpected exception: {type(e).__name__}: {e}")

@given(st.text() | st.none())
def test_room_floor_no_crash(s):
    try:
        room_floor(s)
    except (ValueError, TypeError):
        pass # Properly handled input validation error
    except Exception as e:
        pytest.fail(f"room_floor crashed with unexpected exception: {type(e).__name__}: {e}")

@given(st.text() | st.none())
def test_booking_label_no_crash(s):
    try:
        booking_label(s)
    except (ValueError, TypeError):
        pass # Properly handled input validation error
    except Exception as e:
        pytest.fail(f"booking_label crashed with unexpected exception: {type(e).__name__}: {e}")
