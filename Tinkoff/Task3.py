def can_get_winning_sequence(n, a, b):
    # Инициализация переменных l и r, отвечающих за левую и правую границы рассматриваемого отрезка
    l, r = 0, n - 1

    # Переменная для отслеживания наличия различий между списками a и b
    found_diff = False

    # Цикл для обхода списка a и b
    while l <= r:
        # Если элементы a и b на позиции l равны, переходим к следующей позиции l
        if a[l] == b[l]:
            l += 1
        # Если элементы a и b на позиции r равны, переходим к предыдущей позиции r
        elif a[r] == b[r]:
            r -= 1
        else:
            # Если элементы не равны, прекращаем обход
            break

    # Сортируем элементы списка a в интервале [l, r + 1]
    a[l: r + 1] = sorted(a[l:r + 1])

    # Проверяем наличие различий между элементами списка a и b в интервале [l, r + 1]
    for idx in range(l, r + 1):
        if a[idx] != b[idx]:
            found_diff = True

    # Если различий нет, возвращаем "YES", иначе "NO"
    if not found_diff:
        return "YES"
    else:
        return "NO"


# Ввод данных и вызов функции can_get_winning_sequence
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = can_get_winning_sequence(n, a, b)

# Вывод результата
print(result)
