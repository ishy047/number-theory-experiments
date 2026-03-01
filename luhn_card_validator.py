num = int(input("-CREDIT CARD CHECKER-\nEnter your credit card number: "))
num = str(num)

#---LUHNS ALGORITHM-----------
alternate_digits = num[-2::-2] # starts at the 2nd to last digit, and steps every -2

doubled_digits = ""
for digit in alternate_digits:
    doubled_digits += str((int(digit)*2)) # gets each every other digit, multiplies them by 2, and adds them together

digits_sum = 0
for digit in doubled_digits: # for each digit in the doubled digits
    digits_sum += int(digit) # adds each digit together

other_digits = num[-1::-2] # all digits from original number that wasn't doubled
for digit in other_digits:
    digits_sum += int(digit) #adds each other digit to the current digit sum
#--------------------------------

if digits_sum % 10 == 0:
    if len(num) == 15 and (num[:2] == '34' or num[:2] == '37'):
        print("AMEX")
    elif len(num) == 16 and (num[:2] == '51' or num[:2] == '52' or num[:2] == '53' or num[:2] == '54' or num[:2] == '55'):
        print("MASTERCARD")
    elif (len(num) == 13 or len(num) == 16) and num[:1] == '4':
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")