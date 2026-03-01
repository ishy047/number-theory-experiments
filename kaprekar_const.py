descending_num = []
ascending_num = []

def find_highest(num):
    highest = 0
    for i in str(num):
        if int(i) > highest:
            highest = int(i)
    return highest

def rearrange_descending(num):
    for i in range(4):
        descending_num.append(find_highest(num))
        num = str(num).replace(str(find_highest(num)), "", 1)
    num = "".join(map(str, descending_num))
    return num

def find_lowest(num):
    lowest = 9
    for i in str(num):
        if int(i) < lowest:
            lowest = int(i)
    return lowest

def rearrange_ascending(num):
    for i in range(4):
        ascending_num.append(find_lowest(num))
        num = str(num).replace(str(find_lowest(num)), "", 1)
    num = "".join(map(str, ascending_num))
    return num

print("-KAPREKAR'S CONSTANT TESTER-")
while True:
    try:
        num = int(input("Enter a 4-digit number (digits can't all be the same): "))
    except ValueError:
        print("Incorrect input")
        continue
    if len(str(num)) != 4:
        print("Incorrect length")
        continue
    if len(set(str(num))) == 1:
        print("All digits are the same")
        continue
    else:
        break

print("")
step = 0
while num != "6174":
    step += 1
    num1 = int(rearrange_descending(num))
    num2 = int(rearrange_ascending(num))
    num = str(num1 - num2).zfill(4)
    print(f"Step {step}: {num1} - {num2} = {num}")
    descending_num.clear()
    ascending_num.clear()

print(f"\nIt took {step} iterations to reach Kaprekar's constant ({num})")

