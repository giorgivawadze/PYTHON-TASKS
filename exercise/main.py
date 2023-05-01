
# 8-6

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))



# 8-7












class Dog:
    def __init__(self, name:str) -> None:
        
        """
        initializer / constructor
        
        dunder method / magic methods __method_name__
        """
        self.name = name


def sit(self) -> None:
    print(f"{self.name} is sitting")

def roll_over(self) -> None:
    print(f'{self.name} is rolling over')

# instance / object
dog_1: Dog = Dog("Jessy") #instantiation / object cretion

print(dog_1.name)
dog_1.sit()



class Tranport:
    def __init__(self, brand: str, modeL:str, year:int) -> None:
      self.brand = brand
      self.model = modeL
      self.year = year
        

# class Sedan(Tranport):
#   pass

# class Food:
#     def __init__(self, fruit:str, color:str, term:int) -> None:
#         self.fruit = fruit
#         self.color = color
#         self.term = term



# def fruit (self):
#     {f'{self.fruit} is trash'}

# apple: Food = Food('apple' ,'red', 2020)

# print(apple.fruit())

class Food:
    def __init__(self, fruit:str, color:str, term:int) -> None:
        self.fruit = fruit
        self.color = color
        self.term = term

    def is_trash(self):
        if self.term < 2022:
            return f'{self.fruit} is trash'
        else:
            return f'{self.fruit} is fresh'

apple: Food = Food('apple', 'red', 2020)

print(apple.is_trash()) 




class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 


emp_1 = Employee('Corey', 'Schafer' , 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())


print ('{} {}'.format(emp_1.first, emp_1.last))







class Dog:

 """A simple attempt to model a dog."""
 def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age
 def sit(self):
    """Simulate a dog sitting in response to a command."""
    (f"{self.name} is now sitting.")
def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")



my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")    
my_dog.sit()
my_dog.roll_over()











"""
f = open('./exercise/data.txt')

print(f.read())
f.close()

"""
with open ('./exercise/data.txt') as f:
    #  print(f.readlines())

    users = [
    user.strip()
    for user in f.readlines()
]
    print(users)
    print(f.read)
print(f.tell())
f.seek(22)

print(f.readlines())     

print(users)
print(f.read())










