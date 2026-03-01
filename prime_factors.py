
def is_whole_number(n):
    return isinstance(n, int) or (isinstance(n, float) and n.is_integer())

def smallest_prime(n):
    for num in range(int(n)):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                value = n / num
                if is_whole_number(value) == True:
                    return num

primes = []

def prime_factors(n):
    while is_whole_number(n) == True:
        try:
            primes.append(smallest_prime(n))
            n = int(n) / smallest_prime(int(n))
        except TypeError:
            primes.append(int(n))
            return ""

prime_factor_input = float(input("-PRIME FACTOR CALCULATOR- \nPlease enter a positive integer: "))
print(prime_factors(prime_factor_input))
primes.remove(None)
print(primes)




