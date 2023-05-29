def encrypt_rail_fence(text, key):
    encrypted_string = ""
    idx = 0
    rail = [[] for _ in range(key)]
    direction = 1

    for char in text:
        rail[idx].append(char)
        idx += direction

        if idx == 0 or idx == key - 1:
            direction = -direction

    for row in rail:
        encrypted_string += "".join(row)

    return encrypted_string


def decrypt_rail_fence(text, key):
    decrypted_text = ""
    idx = 0
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction = 1

    for i in range(len(text)):
        rail[idx][i] = '*'
        idx += direction

        if idx == 0 or idx == key - 1:
            direction = -direction

    idx = 0

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] == '*' and idx < len(text):
                rail[i][j] = text[idx]
                idx += 1

    idx = 0
    direction = 1

    for i in range(len(text)):
        decrypted_text += rail[idx][i]
        idx += direction

        if idx == 0 or idx == key - 1:
            direction = -direction

    return decrypted_text


def main():
    text = input("Enter Text: ")
    key = int(input("Enter Key: "))

    encrypted_text = encrypt_rail_fence(text, key)
    print("Encrypted Message:", encrypted_text)

    decrypted_text = decrypt_rail_fence(encrypted_text, key)
    print("Decrypted Message:", decrypted_text)


if __name__ == "__main__":
    main()
