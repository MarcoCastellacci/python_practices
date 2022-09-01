numbers = []
for number in range(0,101):
    numbers.append(number)
    if 100 in numbers:
        print(sorted(numbers, reverse=True))
        