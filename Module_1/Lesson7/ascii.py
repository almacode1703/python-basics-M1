print("ASCII Value Checker")
print("=" * 30)

# take input
char = input("Enter a single character: ")

# validation
if type(char) is str and len(char) == 1:

    # get ASCII value
    ascii_val = ord(char)

    # display
    print(f"\nCharacter: '{char}'")
    print(f"ASCII Value: {ascii_val}")

    # identify type
    print("Character Type:", end=" ")

    if 65 <= ascii_val <= 90:
        print("Uppercase Letter")

    elif 97 <= ascii_val <= 122:
        print("Lowercase Letter")

    elif 48 <= ascii_val <= 57:
        print("Digit")

    elif ascii_val == 32:
        print("Space")

    else:
        print("Special Character")

else:
    print("\nError: Please enter exactly ONE character!")
