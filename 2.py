from collections import Counter

def group_characters(input_str):

    characters = input_str.split()

    counter = Counter(characters)


    grouped = []
    for char, count in counter.items():
        grouped.append([char] * count)

    return grouped


input_str = input("Введите строку символов, разделенных пробелами: ")
result = group_characters(input_str)

print("Результат:", result)
