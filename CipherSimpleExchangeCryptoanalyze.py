import random

filename = "OpenText.txt"  # имя файла, который мы хотим проанализировать
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph1 = 'abcdefghijklmnopqrstuvwxyz'
# Создаем словарь для подсчета символов
char_count = {}

# Открываем файл на чтение
with open(filename, 'r') as file:
    # Итерируемся по символам в файле

    for char in file.read().lower():
        if char in alph:
            char_count[char] += 1
        if char in alph1:
            # Если символ уже встречался, увеличиваем его количество
            if char in char_count:
                char_count[char] += 1
            # Если символ встречается впервые, добавляем его в словарь
            else:
                char_count[char] = 1

# Выводим результаты
print("Результаты подсчета символов в открытом тексте '{}':".format(filename))
sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

print(sorted_char_count)

print(' ')
lst = list(alph1)  # преобразуем строку в список символов
random.shuffle(lst)  # перемешиваем список
s_shuffled = ''.join(lst)  # объединяем список символов в строку

with open("OpenText.txt", "r") as f:
    text = f.read().lower()

# Заменяем каждый символ из текста на символ из перемешанного списка
encrypted_text = ""
for char in text:
    if char not in alph1:
        encrypted_text += char
    else:
        for i in range(len(alph1)):
            if char == alph1[i]:
                encrypted_text += s_shuffled[i]

# создаем пустой словарь
letter_count = {}
for letter in encrypted_text:
    if letter.isalpha():
        letter = letter.lower()  # переводим буквы в нижний регистр для упрощения подсчета
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

print(sorted_letter_count)
