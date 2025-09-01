from string import ascii_letters as a_l


def encrypt(message: str, key: str) -> str:
    encrypted_message = ''
    key_len = len(key)
    letter_count = 0  # counts only letters

    for char in message:
        if char not in a_l:
            encrypted_message += char
        else:
            key_index = letter_count % key_len
            key_char = key[key_index]
            hidden_index = (a_l.index(char) + a_l.index(key_char)) % len(a_l)
            encrypted_message += a_l[hidden_index]
            letter_count += 1
    return encrypted_message


def decrypt(message: str, key: str) -> str:
    decrypted_message = ''
    key_len = len(key)
    letter_count = 0

    for char in message:
        if char not in a_l:
            decrypted_message += char
        else:
            key_index = letter_count % key_len
            key_char = key[key_index]
            open_index = (a_l.index(char) - a_l.index(key_char)) % len(a_l)
            decrypted_message += a_l[open_index]
            letter_count += 1
    return decrypted_message


if __name__ == '__main__':
    message = 'Kill Harry Potter!'

    encrypted_message = encrypt(message, 'snape')
    print(encrypted_message)

    print(decrypt(encrypted_message, 'snape'))
