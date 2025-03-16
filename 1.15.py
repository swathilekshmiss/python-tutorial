def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primes():
    for num in range(2, 1000):
        if prime(num):
            print(num, end=" ")
            primes()
