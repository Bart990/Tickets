# Сортировка подсчетом
def counting_sort(arr):
    # Находим максимальное и минимальное значения для определения диапазона
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count_arr = [0] * range_of_elements  # Список нулей длинной в значение максимального элемента + 1 для 0
    output_arr = [0] * len(arr)  # Список нулей по кол-ву элементов входного массива

    for i in range(len(arr)):  # Смотрим на значение элемента входного массива и прибавляем 1 индекс равный значению данного элемента
        count_arr[arr[i] - min_val] += 1

    # Изменяем count_arr, добавляя предыдущее значение к текущему
    # Это необходимо, чтобы определить позицию элемента в отсортированном массиве
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in reversed(range(len(arr))):
        # Определяем индекс в отсортированном массиве для текущего элемента
        index = count_arr[arr[i] - min_val] - 1
        # Размещаем элемент в отсортированном массиве
        output_arr[index] = arr[i]
        # Уменьшаем счетчик в массиве подсчета
        count_arr[arr[i] - min_val] -= 1

    return output_arr


# Пример использования
arr = [12, 11, 13, 5, -3, 6, 0, 2, 7, 1, 2]
print("Сортировка подсчетом\nОтсортированный массив:", counting_sort(arr))
