# Функция сортировки выбором
def selection_sort(alist):
    # Проходим по всему списку, кроме последнего элемента
    for i in range(0, len(alist) - 1):
        smallest = i  # Предполагаем, что текущий элемент является наименьшим
        # Ищем наименьший элемент в оставшейся части списка
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j  # Находим новый наименьший элемент
        # Обмениваем найденный наименьший элемент с текущим элементом
        alist[i], alist[smallest] = alist[smallest], alist[i]


# Запрашиваем список чисел от пользователя
alist = input('Enter the list of numbers: ').split()
# Преобразуем полученные строки в целые числа
alist = [int(x) for x in alist]
# Применяем сортировку выбором к списку
selection_sort(alist)
# Выводим отсортированный список
print('Sorted list: ', end='')
print(alist)
