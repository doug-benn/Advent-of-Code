def find_first(str):
    for char in str[0]:
        if char.isdigit():
            return char


def find_last(str):
    for char in reversed(str):
        if char.isdigit():
            return char


numbers = []

with open("./2023/01/part_1_input.txt") as file:
    lines = file.readlines()
    for line in lines:
        first = find_first(line.split())
        last = find_last(line.strip())
        result = first + last
        numbers.append(int(result))

print(sum(numbers))
