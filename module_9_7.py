def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        for i in range(2, a // 2):
            if a % i == 0:
                print(f'Простое')
            else:
                print(f'Составное')
            return a
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)