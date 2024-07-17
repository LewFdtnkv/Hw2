alphabet = 'abcdefghijklmnopqrstuvwxyz'


def NOD(a, b):
    if b == 0:
        return a
    else:
        return NOD(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_cipher_decrypt(ciphertext, a, b):
    plaintext = ''
    a_inverse = mod_inverse(a, len(alphabet))
    if a_inverse is None:
        return 'Error: a and len(alphabet) are not coprime'
    else:
        for letter in ciphertext:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new_index = (a_inverse * (index - b)) % len(alphabet)
                if letter.isupper():
                    plaintext += alphabet[new_index].upper()
                else:
                    plaintext += alphabet[new_index]
            else:
                plaintext += letter
    return plaintext


def affineCipherBruteForce(ciphertext):
    for a in range(2, len(alphabet)):
        if NOD(a, len(alphabet)) == 1:
            for b in range(len(alphabet)):
                plaintext = ''
                for letter in ciphertext:
                    if letter.lower() in alphabet:
                        index = alphabet.index(letter.lower())
                        new_index = ((index - b) * mod_inverse(a, len(alphabet))) % len(alphabet)
                        if letter.isupper():
                            plaintext += alphabet[new_index].upper()
                        else:
                            plaintext += alphabet[new_index]
                    else:
                        plaintext += letter
                print(f'a={a}, b={b}, plaintext={plaintext}')


print('Введите текст для расшифровки...')
ciphertext = input()
affineCipherBruteForce(ciphertext)
