def heapify(arr, n, i):
    """Функция для построения кучи из списка"""
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # левый = 2*i + 1
    r = 2 * i + 2  # правый = 2*i + 2

    # Проверяем, существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем, существует ли правый дочерний элемент больший, чем наибольший на данный момент
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем

        # Применяем heapify к корню
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # меняем текущий корень с последним элементом
        heapify(arr, i, 0)


# Тестовый код
arr = [12, 11, 13, 5, 6, 7, -1, 0]
heapSort(arr)
print("Отсортированный массив:", arr)
