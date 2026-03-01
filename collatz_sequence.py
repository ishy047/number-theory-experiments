step = 0

num = int(input("Enter a number: "))

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