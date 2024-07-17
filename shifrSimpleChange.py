import random

engineAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                  ]
arrAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
               ]
print('Введите ключ ')
random.shuffle(arrAlphabet)
print('исходный алфавит: ')
print(engineAlphabet)
print('Новый алфавит: ')
print(arrAlphabet)
print('Введите фразу для зашифровки...')
word = input()


def encode(word):
    x = 0
    shifrateWord = ''
    for i in word:
        if i == ' ':
            shifrateWord += ' '
        else:
            for j in range(len(engineAlphabet)):
                if i == engineAlphabet[j]:
                    shifrateWord += arrAlphabet[j]
    print(f'Зашифрованная фраза: {shifrateWord}')
    return shifrateWord


shifr = encode(word)


def decode(shifr):
    engineWord = ''
    for i in shifr:
        if i == ' ':
            engineWord += ' '
        else:
            for j in range(len(arrAlphabet)):
                if i == arrAlphabet[j]:
                    engineWord += engineAlphabet[j]
    print(f'Исходная фраза: {engineWord}')


decode(shifr)
