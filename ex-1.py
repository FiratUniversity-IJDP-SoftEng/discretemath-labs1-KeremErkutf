# 1.  Write a function that determines if a positive integer is prime.

def is_Positive(num):
    if num > 0:
        return True

def is_Prime(num):
    if is_Positive(num):
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    return False

print(is_Prime(6)) # False
print(is_Prime(5)) # True