class FizzBuzz:
    def __init__(self,name: str):
        self.name = name
    
    def get_name(self)-> str:
        pass

fizzbuzzs = [
    FizzBuzz('Fizz'),
    FizzBuzz('Buzz'),
    FizzBuzz('FizzBuzz')
]

def get_fizzbuzz(fizzbuzz: list,n:int):
    for i in fizzbuzz:
        if n %3 == 0 and i.name == 'Fizz':
            return True
        elif n%5 ==0 and i.name == 'Buzz':
            return True
        elif n%5 ==0 and n%3 == 0 and i.name == 'FizzBuzz':
            return True
        else:
            return False

def prints():
    for i in range(1,20):
        print("{0} {1}".format(i,get_fizzbuzz(fizzbuzzs,i)))
        
prints()          
    