def superFizzBuzz(n):
    if n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Fizz'
    elif n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 9 == 0:
        return 'FizzFizz'
    elif n % 25 == 0:
        return 'BuzzBuzz'
    elif n % 9 == 0 and n % 25 == 0:
        return 'FizzFizzBuzzBuzz'
    elif n % 3 and n % 5 and n % 9 and n % 25:
        return 'NoFizzBuzz'