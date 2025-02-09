from string import ascii_letters


def encrypt(message: str, key: int) -> str:
    result = ''

    for char in message:
        if char not in ascii_letters:
            result += char
        else:
            new_char_key = (ascii_letters.index(char) + key) % len(ascii_letters)
            result += ascii_letters[new_char_key]

    return result


def decrypt(message: str, key: int) -> str:
    return encrypt(message, -key)


def brute_force(message):
    brute_data = {}
    for key in range(1, len(ascii_letters) + 1):
        brute_data[key] = decrypt(message, key)
    return brute_data


if __name__ == '__main__':
    message = 'Hello world!'

    encrypted_message = encrypt(message, 5)
    print(encrypted_message)

    print(decrypt(encrypted_message, 5))

    print(brute_force(encrypted_message))
