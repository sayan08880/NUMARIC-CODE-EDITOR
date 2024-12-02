def transform_to_numeric_code(text):
    result = []
    for char in text:
        if char.isalpha():  # Check if it's a letter
            if char.isupper():
                # Capital letter: add '+' and corresponding alphabet number
                result.append(f"+{ord(char) - 64}")
            else:
                # Lowercase letter: just the corresponding alphabet number
                result.append(f"{ord(char) - 96}")
        elif char.isdigit():  # Check if it's a number
            # Prepend '-' to the number
            result.append(f"-{char}")
        else:
            # Special characters or spaces remain unchanged
            result.append(char)
    return " ".join(result)

# Example usage
text = input("ENTER THE WORD TO TRANSFOSE : ")
numeric_code = transform_to_numeric_code(text)
print(numeric_code)
