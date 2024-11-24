numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Найти индекс пропущенного элемента
missing_index = numbers.index(None)

# Рассчитать сумму и количество для среднего арифметического (без пропущенного элемента)
sum_without_missing = sum(num for num in numbers if num is not None)
count_with_missing = len(numbers)

# Вычислить среднее арифметическое
average = sum_without_missing / (count_with_missing)

# Заменить пропущенный элемент
numbers[missing_index] = average

# Вывод обновлённого списка
print("Измененный список:", numbers)


