class FizzBuzz:
    def __init__(self,num):
        self.num = num
    
    # def add_number(self,num):
    #     self.num += num

    def get_Buzz(self):
        pass
    def get_fizz(self):
        pass
    def get_fizzBuzz(self):
        pass
    def get_allfizzbuzz(self):
        pass
        
class Get_fizz():
    def get_fizz(self):
        return 'Fizz'

class Get_Buzz():
    def get_Buzz(self):
        return 'Buzz'
        
class Get_FizzBuzz():
    def get_fizzBuzz(self):
        return 'FizzBuzz'


class Get_allFizzbuzz(FizzBuzz):
    def get_allfizzbuzz(self):
        if self.num % 3 == 0 and self.num % 5 == 0:
            fizzbuzz = Get_FizzBuzz()
            return fizzbuzz.get_fizzBuzz()
        elif self.num % 3 == 0:
            fizz = Get_fizz()
            return fizz.get_fizz()
        elif self.num % 5 == 0:
            buzz = Get_Buzz()
            return buzz.get_Buzz()
        else:
            return 'nofizzbuzz'
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
    show = Get_allFizzbuzz(n)
    # show.add_number(n)
    return show.get_allfizzbuzz()


print("show_fizzBuzz {0}".format(show_fizzbuzz(15)))
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