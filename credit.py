def IsValidLuhn(digits):
    '''
    Wikipedia C# Luhn Algorithm Code

    int checkDigit = 0;
    for (int i = digits.Length - 2; i >= 0; --i)
    {
        checkDigit +=
            (i & 1) == (digits.Length & 1)
                ? digits[i] > 4 ? digits[i] * 2 - 9 : digits[i] * 2
                : digits[i];
    }

    return (10 - checkDigit % 10) % 10 == digits[^1];
    '''

    check_digit = 0
    length = len(digits)

    for i in range(length - 2, -1, -1):
        if (i & 1) == (length & 1):
            check_digit += digits[i] * 2 - 9 if digits[i] > 4 else digits[i] * 2
        else:
            check_digit += digits[i]

    return (10 - check_digit % 10) % 10 == digits[-1]

def extract_digits(input_string):
    # Initialize an empty list to store the digits
    digits_array = []
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            # Append the digit to the list
            digits_array.append(int(char))  # Convert to integer if needed
    return digits_array

# Example usage (number taken from internet, not real)
#luhn = '4569403961014710'
luhn = '378282246310005'

luhn2 = extract_digits(luhn)
print(IsValidLuhn(luhn2))

# generates basically every credit card number
if(not True):
    for i in range(1000000000000000,10000000000000000,1):
        if(IsValidLuhn(extract_digits(str(i)))):
            print(i)