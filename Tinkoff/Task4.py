import collections


# Преобразование входных данных.
# Вводим количество чисел и количество пар
n, m = list(map(int, input().split()))

# Вводим числа
a = list(map(int, input().split()))

# Создаем словарь сумм
sum_dict = collections.defaultdict(list)

# Заполняем словарь сумм
for num in a:
    sum_dict[num] = []
    sum_dict[num + num] = [num, num]

# Заполняем словарь суммами пар чисел
for i in range(m-1):
    for j in range(i + 1, m):
        sum_dict[a[i] + a[j]] = [a[i], a[j]]

# Находим результат
result = []

# Проверяем, есть ли сумма n - num в словаре sum_dict
for num in a:
    if (n - num) in sum_dict.keys():
        result = list([num, *sum_dict[n-num]])

# Если результат пустой, то выводим -1, иначе выводим результат
if len(result) == 0:
    print(-1)
else:
    print(len(result))
    print(*result)