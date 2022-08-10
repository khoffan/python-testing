def is_prime_list(number):
    for num in number:
        for n in range(2,num):
            if num % n == 0:
                return False
    return True
