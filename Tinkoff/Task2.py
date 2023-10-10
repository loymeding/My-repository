# Создание словаря sheriff_dict, где каждой букве присваивается начальное значение 0
sheriff_dict = {
    's': 0,
    'h': 0,
    'e': 0,
    'r': 0,
    'i': 0,
    'f': 0
}

# Ввод строки s
s = input()

# Подсчет количества для каждой буквы в строке s
for letter in s:
    # Если буква есть в ключах словаря sheriff_dict,
    # то увеличиваем значение этой буквы на 1
    if letter in sheriff_dict.keys():
        sheriff_dict[letter] += 1

# Деление количества для буквы 'f' на 2, т.к для формирования слова требуется две буквы 'f'
sheriff_dict['f'] = sheriff_dict['f'] // 2

# Получение списка значений словаря sheriff_dict
count_letters = list(sheriff_dict.values())

# Нахождение минимального количества для букв для определения сколько слов sheriff можно из них составить
min_count_letter = count_letters[0]

# Проверка каждого значения в списке count_letters
for count in count_letters:
    # Если текущее значение count меньше минимального значения min_count_letter,
    # то присваиваем этому значению значение count
    if count < min_count_letter:
        min_count_letter = count

# Вывод минимального количества буквы
print(min_count_letter)