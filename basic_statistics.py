def analyse(numbers):
    numbers.sort()

    # MEAN
    total = 0
    for n in numbers:
        total += n
    mean = total / len(numbers)

    # MEDIAN
    index = (len(numbers) + 1) / 2
    if type(index) == int:
        median = numbers[int(index)]
    elif type(index) == float:
        num1 = numbers[int(index - 0.5)]
        num2 = numbers[int(index + 0.5)]
        middle = (num1 + num2) / 2
        median = middle

    # MODE
    highest = 0
    mode = None
    for n in numbers:
        count = numbers.count(n)
        if count > highest:
            highest = count
            if count > 1:
                mode = n

    # RANGE
    range = (numbers.pop()) - numbers.pop(0)

    return mean, median, mode, range

numbers = []
user_input = input("-STATISTICS CALCULATOR-\nPlease enter some numbers (e.g 10 2 130 4): ").split()
for n in user_input:
    numbers.append(int(n))

mean, median, mode, range = analyse(numbers)
print(f"Mean: {mean}\nMedian: {median}\nMode: {mode}\nRange: {range}")