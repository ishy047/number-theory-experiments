import random

step = 0
process = input("Random, or Input?").lower()

if process == "random":
    size = input("What range? (e.g type: 1 90) ").split()
    num = random.randint(int(size[0]), int(size[1]))
else:
    num = int(input("Enter a number: "))

print(f"Number: {num} ")

while num != 1:
    if num % 2 == 0:
        step += 1
        num //= 2
        print(f"\033[90m{step}:\033[0m {num}")
    else:
        step += 1
        num *= 3
        num += 1
        print(f"\033[90m{step}:\033[0m {num}")

print(f"It took {step} steps to reach {num}")