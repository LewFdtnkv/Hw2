alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
dictinary = {a: v for a, v in zip(value, alphabet)}

print('введите аддитивный ключ...')
additiveKey = int(input())
print('Введите мильтипликативный ключ(число вида: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)...')
multiplicativeKey = int(input())
testMultKeyArr = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

if multiplicativeKey not in testMultKeyArr:
    print('Введено неверное число...')
    exit()
multiplicativeDeshifrateKey = 0
for i in range(len(alphabet)):
    if i * multiplicativeKey % len(alphabet) == 1:
        multiplicativeDeshifrateKey = i
print(f'мильпликативный ключ для расшифровки: {multiplicativeDeshifrateKey}')
print('Введите требуемое слово для зашифровки...')
word = input()


def encode():
    shifrateWord = ''
    for i in word:
        if 'A' <= i <= 'Z':
            i = i.lower()
        for j in dictinary:
            if i == dictinary[j]:
                code = (j * multiplicativeKey + additiveKey) % len(alphabet)
                shifrateWord += dictinary[code]

    print(f'зашифрованное слово: {shifrateWord}')
    return shifrateWord


shifr = encode()


def decode(shifr):
    print('Введите аддитивный ключ для расшифровки...')
    addKey = int(input())
    print('Введите мильпликативный ключ для расшифровки...')
    multplicativeDeshifrateKey = int(input())
    engineWord = ''
    for i in shifr:
        for j in dictinary:
            if i == dictinary[j]:
                code = ((j - addKey + len(alphabet)) * multplicativeDeshifrateKey) % len(alphabet)
                engineWord += dictinary[code]
    print(f'Расшифрованное слово: {engineWord}')


decode(shifr)
