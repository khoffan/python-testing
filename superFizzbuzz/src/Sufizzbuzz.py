class FizzBuzz:
    def __init__(self):
        self.num = 0

    def add_number(self,num):
        self.num += num       
    
        
class Get_fizzbuzz(FizzBuzz):
    def get_fizz(self):
        if self.num % 3 == 0 and self.num % 5 == 0:
            return 'FizzBuzz'
        elif self.num % 3 == 0:
            return 'Fizz'
        elif self.num % 5 == 0:
            return 'Buzz'

def show_fizzbuzz(n):
    show = Get_fizzbuzz()
    show.add_number(n)
    return show.get_fizz()





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