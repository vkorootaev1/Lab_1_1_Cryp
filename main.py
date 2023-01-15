import collections
import csv
import sys
from collections import Counter


# Максимальная и минимальная частота в последовательности
def max_min_number(arr):
    max_num = - sys.maxsize
    min_num = sys.maxsize

    for val in arr.values():
        if val > max_num:
            max_num = val
        if val < min_num:
            min_num = val
    return max_num, min_num


# Параметры
a = 21
b = 31
n = 100
x0 = a
list_of_numbers = []
x = x0

# Генерация псевдослучайных чисел
for i in range(0, 100 * n):
    x = (a * x + b) % n
    list_of_numbers.append(x)

# Сортировка и подсчет частот
counter_numbers = Counter(list_of_numbers)
counter_numbers = collections.OrderedDict(sorted(counter_numbers.items()))

print('Отсортированный список (число, частота):\n', counter_numbers, sep='')
print('Всего уникальных чисел в последовательности: \n', len(counter_numbers), sep='')

max_n, min_n = max_min_number(counter_numbers)
print('Максимальное значение повторений числа: \n', max_n, '\nМинимальное значение повторений числа: \n', min_n, sep='')

max_dev = max(min_n/100 - 1, max_n/100 - 1)
print('Максимальное отклонение:', max_dev*100, '%')

# Запись в файл
with open('output_file.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=';')
    for key, value in counter_numbers.items():
        writer.writerow([key, value])

for i in range(0, len(list_of_numbers)):
    print(i+1, ') ', list_of_numbers[i], sep='')

