# Функция для сравнения и обмена элементов
def compAndSwap(a, i, j, dire):
    # Если dire == 1 и элемент a[i] > a[j], или если dire == 0 и a[i] < a[j], то меняем местами
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]


# Функция для слияния битонной последовательности
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:  # Если количество элементов больше 1
        k = cnt // 2  # Делим последовательность на две части
        for i in range(low, low + k):  # Для каждой пары элементов в разделенных половинах
            compAndSwap(a, i, i + k, dire)  # Сравниваем и возможно меняем местами
        bitonicMerge(a, low, k, dire)  # Рекурсивно применяем функцию к первой половине
        bitonicMerge(a, low + k, k, dire)  # Рекурсивно применяем функцию ко второй половине


# Рекурсивная функция для битонной сортировки
def bitonicSort(a, low, cnt, dire):
    if cnt > 1:  # Если количество элементов больше 1
        k = cnt // 2  # Делим последовательность на две части
        bitonicSort(a, low, k, 1)  # Рекурсивно сортируем первую половину по возрастанию
        bitonicSort(a, low + k, k, 0)  # Рекурсивно сортируем вторую половину по убыванию
        bitonicMerge(a, low, cnt, dire)  # Сливаем две битонные последовательности


# Основная функция сортировки
def sort(a, N, up):
    bitonicSort(a, 0, N, up)  # Вызываем битонную сортировку для всего массива


# Пример использования:
a = [3, 7, 4, 8, 6, 2, 1, 5]  # Исходный массив для сортировки
N = len(a)  # Количество элементов в массиве
up = 1  # Направление сортировки: 1 для возрастания, 0 для убывания

sort(a, N, up)  # Сортируем массив
print("\nSorted array is")  # Выводим отсортированный массив
for i in range(N):
    print("%d" % a[i], end=" ")
