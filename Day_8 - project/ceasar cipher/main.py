def encrypt(plain_text, shift_amount):
    cipher_text = ""
    plain_text = plain_text.lower()
    for i in plain_text:
        if not i.isalpha():
            cipher_text += i
        else:
            index = alphabet.index(i)
            new_index = index + shift_amount
            if new_index > 25:
                new_index = new_index - 25
            cipher_text += alphabet[new_index]

    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    cipher_text = cipher_text.lower()
    for i in cipher_text:
        if not i.isalpha():
            plain_text += i
        else:
            index = alphabet.index(i)
            new_index = index - shift_amount
            if new_index < 0:
                new_index = new_index + 25
            plain_text += alphabet[new_index]

    print(f"The decoded text is {plain_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("not defined")
