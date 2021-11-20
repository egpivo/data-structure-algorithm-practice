def rotational_cipher(input, rotation_factor):
    result = ""

    for char in input:
        if char.isnumeric():
            result += str((int(char) + rotation_factor) % 10)
        elif char.isalpha():
            if char.isupper():
                result += chr((ord(char) + rotation_factor - 65) % 26 + 65)
            else:
                result += chr((ord(char) + rotation_factor - 97) % 26 + 97)
        else:
            result += char
    return result


if __name__ == "__main__":
    input = "abcde-123"
    rotation_factor = 2
    print(f"Solution: {rotational_cipher(input, rotation_factor)}")
