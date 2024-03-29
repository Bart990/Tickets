# Функция быстрой сортировки
def quick_sort(arr):
    # Если массив содержит 0 или 1 элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr
    # Выбираем элемент, относительно которого будем разделять массив (опорный элемент)
    pivot = arr[len(arr) // 2]
    # Создаем подмассив с элементами меньше опорного
    left = [x for x in arr if x < pivot]
    # Создаем подмассив с элементами, равными опорному (для стабильности сортировки)
    middle = [x for x in arr if x == pivot]
    # Создаем подмассив с элементами больше опорного
    right = [x for x in arr if x > pivot]
    # Рекурсивно применяем быструю сортировку к подмассивам и объединяем их
    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
arr = [3, 6, 8, 10, 1, 2, 1, -1, 0]  # Исходный массив для сортировки
print(quick_sort(arr))  # Вывод отсортированного массива
