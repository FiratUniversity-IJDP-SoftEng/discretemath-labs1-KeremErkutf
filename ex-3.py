def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_prime():
    limit = 100
    prime_nums = []

    for i in range(2, limit + 1):
        if is_prime(i):
            prime_nums.append(i)

    return prime_nums

def change_list():
    prime_nums = list_prime()
    for i in range(len(prime_nums)):
        prime_nums[i] = ((2**prime_nums[i]) - 1)
    return prime_nums

numbers = change_list()
print(numbers)
