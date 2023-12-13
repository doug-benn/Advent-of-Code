def find_first(str):
    for char in str[0]:
        if char.isdigit():
            return char


def find_last(str):
    for char in reversed(str):
        if char.isdigit():
            return char


numbers = []

number_names = [
    ("one", "one1one"),
    ("two", "two2two"),
    ("three", "three3three"),
    ("four", "four4four"),
    ("five", "five5five"),
    ("six", "six6six"),
    ("seven", "seven7seven"),
    ("eight", "eight8eight"),
    ("nine", "nine9nine"),
]


with open("./2023/01/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        for pair in number_names:
            line = line.replace(pair[0], pair[1])
        first = find_first(line.split())
        last = find_last(line.strip())
        result = first + last
        numbers.append(int(result))

print(sum(numbers))
