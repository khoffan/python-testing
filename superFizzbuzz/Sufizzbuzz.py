class FizzBuzz:
    def __init__(self):
        self.num = 0
    def add_number(self,num):
        self.num += num 
    def get_fizzBuzz(self):
        pass
    
        
class Get_fizzbuzz(FizzBuzz):
    def get_fizzBuzz(self):
        if self.num % 3 == 0 and self.num % 5 == 0:
            return 'FizzBuzz'
        elif self.num % 3 == 0:
            return 'Fizz'
        elif self.num % 5 == 0:
            return 'Buzz'
        else:
            return 'NoFizzBuzz'


# class Get_fizzbuzzsuper(FizzBuzz):
#     def get_fizzBuzzsuper(self):
#         if self.num % 9 == 0 and self.num % 25 == 0:
#             return 'FizzFizzBuzzBuzz'
#         elif self.num % 9 == 0:
#             return 'FizzFizz'
#         elif self.num % 25 == 0:
#             return 'BuzzBuzz'
#         else:
#             return 'NoFizzBuzz'

def show_fizzbuzz(n: int):
    show = FizzBuzz()
    show.add_number(n)
    return show.get_fizzBuzz()


print("show_fizzBuzz {0}".format(show_fizzbuzz(25)))
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