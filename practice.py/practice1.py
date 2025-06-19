def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for symbol in reversed(roman):
        value = roman_values[symbol]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Ask user to input a Roman numeral
roman_number = input("Enter a Roman numeral: ").upper()
result = roman_to_integer(roman_number)
print(f"The integer value of {roman_number} is {result}")
