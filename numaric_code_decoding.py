def decode_from_numeric_code(numeric_code):
    elements = numeric_code.split()  # Split the code into parts
    result = []
    
    for element in elements:
        if element.startswith("+"):  # Uppercase letter
            num = int(element[1:])  # Remove "+" and convert to a number
            result.append(chr(num + 64))  # Convert number to uppercase letter
        elif element.isdigit():  # Lowercase letter
            num = int(element)  # Convert to a number
            result.append(chr(num + 96))  # Convert number to lowercase letter
        elif element.startswith("-") and element[1:].isdigit():  # Numbers
            result.append(element[1:])  # Remove "-" to restore the original number
        else:  # Special characters or spaces
            result.append(element)
    
    return ''.join(result)

# Example usage
numeric_code = input("ENTER THE CODE : ")
decoded_text = decode_from_numeric_code(numeric_code)
print(decoded_text)
