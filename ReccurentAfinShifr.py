alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
dictinary = {a: v for a, v in zip(value, alphabet)}
print(dictinary)
print('введите 1 аддитивный ключ...')
additiveKey1 = int(input())

print('Введите 1 мильтипликативный ключ(число вида: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)...')
multiplicativeKey1 = int(input())
testMultKeyArr = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

if multiplicativeKey1 not in testMultKeyArr:
    print('Введено неверное число...')
    exit()
multiplicativeDeshifrateKey1 = 0
for i in range(len(alphabet)):
    if i * multiplicativeKey1 % len(alphabet) == 1:
        multiplicativeDeshifrateKey1 = i
print('введите 2 аддитивный ключ...')
additiveKey2 = int(input())
print('Введите 2 мильтипликативный ключ(число вида: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)...')
multiplicativeKey2 = int(input())
if multiplicativeKey2 not in testMultKeyArr:
    print('Введено неверное число...')
    exit()
multiplicativeDeshifrateKey1 = 0
for i in range(len(alphabet)):
    if i * multiplicativeKey1 % len(alphabet) == 1:
        multiplicativeDeshifrateKey1 = i
print(f'1 мильпликативный ключ для расшифровки: {multiplicativeDeshifrateKey1}')
multiplicativeDeshifrateKey2 = 0
for i in range(len(alphabet)):
    if i * multiplicativeKey2 % len(alphabet) == 1:
        multiplicativeDeshifrateKey2 = i
print(f'2 мильпликативный ключ для расшифровки: {multiplicativeDeshifrateKey2}')
print('Введите требуемое слово для зашифровки...')
word = input()
word1 = ''
for i in word:
    if i in alphabet:
        word1 += i
    elif 'A' <= i <= 'Z':
        word1 += i.lower()

word = word1


def encode(word, multiplicativeKey1, additiveKey2, multiplicativeKey2, additiveKey1):
    shifrateWord = ''
    for i in range(len(dictinary)):
        if word[0] == dictinary[i]:
            shifrateWord += alphabet[(i * multiplicativeKey1 + additiveKey1) % len(alphabet)]
    for i in range(len(dictinary)):
        if word[1] == dictinary[i]:
            shifrateWord += alphabet[(i * multiplicativeKey2 + additiveKey2) % len(alphabet)]
    for i in range(2, len(word)):
        tempAdd = additiveKey2
        additiveKey2 = (additiveKey1 * additiveKey2) % len(alphabet)
        additiveKey1 = tempAdd
        tempMult = multiplicativeKey2
        multiplicativeKey2 = (multiplicativeKey1 * multiplicativeKey2) % len(alphabet)
        multiplicativeKey1 = tempMult
        for j in range(len(alphabet)):
            if word[i] == alphabet[j]:
                shifrateWord += alphabet[(j * multiplicativeKey2 + additiveKey2) % len(alphabet)]
    print(f'Зашифрованное слово: {shifrateWord}')
    return shifrateWord


shifr = encode(word, multiplicativeKey1, additiveKey2, multiplicativeKey2, additiveKey1)


def decode(shifr, additiveKey1, additiveKey2):
    engineWord = ''
    print('Введите 1 мультипликативный ключ для расшифровки...')
    multiplicativeDeshifrateKey1 = int(input())
    print('Введите 2 мультипликативный ключ для расшифровки...')
    multiplicativeDeshifrateKey2 = int(input())
    for i in range(len(dictinary)):
        if shifr[0] == dictinary[i]:
            engineWord += alphabet[((i - additiveKey1 + len(alphabet)) * multiplicativeDeshifrateKey1) % len(alphabet)]
    for i in range(len(dictinary)):
        if shifr[1] == dictinary[i]:
            engineWord += alphabet[((i - additiveKey2 + len(alphabet)) * multiplicativeDeshifrateKey2) % len(alphabet)]
    for i in range(2, len(shifr)):
        tempAdd = additiveKey2
        additiveKey2 = (additiveKey1 * additiveKey2) % len(alphabet)
        additiveKey1 = tempAdd
        tempDMult = multiplicativeDeshifrateKey2
        multiplicativeDeshifrateKey2 = (multiplicativeDeshifrateKey1 * multiplicativeDeshifrateKey2) % len(alphabet)
        multiplicativeDeshifrateKey1 = tempDMult
        for j in range(len(alphabet)):
            if shifr[i] == alphabet[j]:
                engineWord += alphabet[
                    ((j - additiveKey2 + len(alphabet)) * multiplicativeDeshifrateKey2) % len(alphabet)]

    print(f'Расшифрованное слово: {engineWord}')


decode(shifr, additiveKey1, additiveKey2)