def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input("Enter number N: "))
primes = [i for i in range(2, N+1) if is_prime(i)]
print("Prime numbers:", primes)