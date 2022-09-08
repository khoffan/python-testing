class FizzBuzz:
    def __init__(self):
        self.num = 0
    def add_number(self,num):
        self.num += num   
    
        
class Get_fizzbuzz(FizzBuzz):
    def get_fizzBuzz(self):
        if self.num % 9 == 0 and self.num % 25 == 0:
            return 'FizzFizzBuzzBuzz'
        if self.num % 3 == 0 and self.num % 5 == 0:
            return 'FizzBuzz'
        elif self.num % 9 == 0:
            return 'FizzFizz'
        elif self.num % 3 == 0:
            return 'Fizz'
        elif self.num % 25 == 0:
            return 'BuzzBuzz'
        elif self.num % 5 == 0:
            return 'Buzz'
        else:
            return 'NoFizzBuzz'

def show_fizzbuzz(n: int):
    show = Get_fizzbuzz()
    show.add_number(n)
    return show.get_fizzBuzz()

# def prints():
#     for i in range(1,100):
#         if show_fizzbuzz(i) == 'FizzBuzz':
#             print("{0}: {1}".format(i,show_fizzbuzz(i)))

# prints()


# def superFizzBuzz(n):
#     if n % 3 == 0:
#         return 'Fizz'
#     elif n % 5 == 0:
#         return 'Fizz'
#     elif n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     if n % 9 == 0:
#         return 'FizzFizz'
#     elif n % 25 == 0:
#         return 'BuzzBuzz'
#     elif n % 9 == 0 and n % 25 == 0:
#         return 'FizzFizzBuzzBuzz'
#     elif n % 3 and n % 5 and n % 9 and n % 25:
#         return 'NoFizzBuzz'