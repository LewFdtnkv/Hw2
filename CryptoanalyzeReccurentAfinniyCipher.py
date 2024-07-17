alphabet = 'abcdefghijklmnopqrstuvwxyz'
testMultKeyArr = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
print('Введите шифротекст...')
cipherText = input()
additiveKey1 = 0
multiplicativeKey1 = 0
additiveKey2 = 0
multiplicativeKey2 = 0


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
