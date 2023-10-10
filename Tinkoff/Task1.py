# Ввод значений n и s
n, s = map(int, input().split())

# Ввод списка cost_list
cost_list = list(map(int, input().split()))

# Инициализация переменной max_valid_cost
max_valid_cost = -1

# Проверка каждого элемента cost_list
for cost in cost_list:
    # Если cost больше max_valid_cost и меньше или равно s,
    # то присваиваем текущее значение cost переменной max_valid_cost
    if (cost > max_valid_cost) and (cost <= s):
        max_valid_cost = cost

# Если найдено допустимое значение, то выводим его
if max_valid_cost > -1:
    print(max_valid_cost)
else:
    print(0)