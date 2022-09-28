class FizzBuzz:
    def __init__(self , *divid):
        self.divid = divid

    def call_divition(self , num: int):
        for division in self.divid:
            if num % division != 0:
                return None
        return self.get_fizzbuzz()

    def get_fizzbuzz(self):
        return 'NoFizzBuzz'
        
class Get_fizz(FizzBuzz):
    def __init__(self):
        super().__init__(3)
    def get_fizzbuzz(self):
        return 'Fizz'

class Get_Buzz(FizzBuzz):
    def __init__(self):
        super().__init__(5)
    def get_fizzbuzz(self):
        return 'Buzz'
        
class Get_FizzBuzz(FizzBuzz):
    def __init__(self):
        super().__init__(3,5)

    def get_fizzbuzz(self):
        return 'FizzBuzz' 

class Get_FizzFizz(FizzBuzz):
    def __init__(self):
        super().__init__(9)

    def get_fizzbuzz(self):
        return 'FizzFizz'

class Get_BuzzBuzz(FizzBuzz):
    def __init__(self):
        super().__init__(25)

    def get_fizzbuzz(self):
        return 'BuzzBuzz'      

class Get_FizzFizzBuzzBuzz(FizzBuzz):
    def __init__(self):
        super().__init__(9,25)
        
    def get_fizzbuzz(self):
        return 'FizzFizzBuzzBuzz'      


def super_fizzbuzz(n: int) -> str:
    shows : list[FizzBuzz] = [
        Get_FizzFizzBuzzBuzz(),
        Get_FizzFizz(),
        Get_BuzzBuzz(),
        Get_FizzBuzz(),
        Get_fizz(), 
        Get_Buzz(),
        FizzBuzz(1)
    ] 
    for show in shows:
        fizzbuzz = show.call_divition(n)
        if not fizzbuzz is None:
            return fizzbuzz
