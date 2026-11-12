def nights_stayed(days):
    if not isinstance(days, str) or '-' not in days:
        raise ValueError("Invalid days format. Expected 'checkin-checkout' (e.g. 12-15)")
    parts = days.split('-')
    if len(parts) != 2:
        raise ValueError("Invalid format. Expected exactly two values separated by '-'")
    try:
        check_in = int(parts[0].strip())
        check_out = int(parts[1].strip())
    except (ValueError, TypeError):
        raise ValueError("Check-in and check-out days must be valid integers")
    if check_out < check_in:
        raise ValueError("Check-out day cannot be before check-in day")
    return check_out - check_in


def room_floor(room_code):
    if not isinstance(room_code, str) or '-' not in room_code:
        raise ValueError("Invalid room code format. Expected e.g. 'D-305'")
    parts = room_code.split('-')
    if len(parts) < 2 or not parts[1].strip():
        raise ValueError("Room code missing room number")
    number = parts[1].strip()
    if not number or not number[0].isdigit():
        raise ValueError("Room number must start with a digit")
    return int(number[0])


def booking_label(names_csv):
    if not isinstance(names_csv, str):
        raise ValueError("Input names must be a string")
    names = [n.strip() for n in names_csv.split(',') if n.strip()]
    if not names:
        raise ValueError("At least one guest name is required")
    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    try:
        result = nights_stayed(user_input)
        print("Nights:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    try:
        result = room_floor(user_input)
        print("Floor:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    try:
        result = booking_label(user_input)
        print("Booking Label:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
