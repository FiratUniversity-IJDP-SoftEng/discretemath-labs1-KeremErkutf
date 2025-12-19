def take_int():
    while True:
        num = int(input("Please enter a positive integer: "))
        if num > 1:
            return num


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def list_prime():
    limit = take_int()
    prime_nums = []

    for i in range(2, limit + 1):
        if is_prime(i):
            prime_nums.append(i)

    for p in prime_nums:
        print(p)


list_prime()
