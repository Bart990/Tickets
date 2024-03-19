# Сортировка слиянием
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2  # Середина массива входных данных
    left = nums[:mid]  # Левая часть входных данных
    right = nums[mid:]  # Правая часть входных данных

    merge_sort(left)  # Делим левую часть, до момента пока списки не будут содержать 1 элемент
    merge_sort(right)  # Делим правую часть, до момента пока списки не будут содержать 1 элемент

    left_index = 0  # Индекс в left
    right_index = 0  # Индекс в right
    nums_index = 0  # Индекс в nums

    while left_index < len(left) and right_index < len(right):
        # Если число из списка left меньше, чем число из списка right, мы вставляем его в nums на позицию nums_index,
        # после чего увеличиваем индекс left_index на единицу и наоборот
        if left[left_index] < right[right_index]:
            nums[nums_index] = left[left_index]
            left_index += 1
        else:
            nums[nums_index] = right[right_index]
            right_index += 1
        nums_index += 1

    # Перебираем возможные оставшиеся элементы в списке left и добавляем в nums
    while left_index < len(left):
        nums[nums_index] = left[left_index]
        left_index += 1
        nums_index += 1

    # Перебираем возможные оставшиеся элементы в списке right и добавляем в nums
    while right_index < len(right):
        nums[nums_index] = right[right_index]
        right_index += 1
        nums_index += 1

    return nums


# Пример использования
arr = [12, 11, 13, 5, -3, 6, 0, 2, 2, 7, 1, 2]
sorted_arr = merge_sort(arr)
print("Сортировка слиянием \nОтсортированный массив:", sorted_arr)
