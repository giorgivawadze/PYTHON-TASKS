
#9-1
class Restaurant: 
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = 0

    def describe_restaurant(self):
          return '{} {}'.format(self.restaurant_name, self.cuisine_type)
    def open_restaurant(self):
          return f'{self.restaurant_name} is open'
    def set_number_served(self, number):
         self.number_served = number

    def increment_number_served(self, number):
              self.number_served +=number


info = Restaurant("khinklis sakhli", "Italian restaurant")

print(info.describe_restaurant())
print(info.open_restaurant())

info.number_served = 10
print(f"{info.restaurant_name} has served {info.number_served} customers.")


info.set_number_served(20)
print(f"{info.restaurant_name} has served {info.number_served} customers.")


info.increment_number_served(15)
print(f"{info.restaurant_name} has served {info.number_served} customers.")

#9-6

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
          print('Our ice cream flavors are:')
          for flavor in self.flavors:
                print(flavor)


my_ice_cream_stand = IceCreamStand("Scoops", "ice cream", ["vanilla", "chocolate", "strawberry"])
my_ice_cream_stand.display_flavors()



#9-3
class User:
     def __init__(self, first_name, last_name, age, height, login_attempts=0) -> None:
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
          self.height = height
          self.login_attempts = login_attempts

     def greet_user(self):
           return  f'Hello {self.first_name }, {self.last_name}'
     
     def describe(self):
        return f"User information: \nFull name: {self.first_name}, {self.last_name}\nAge: {self.age}\nHeight: {self.height}"
      
     def increment_login(self):
           self.login_attempts += 1
     def reset_login_attempts(self):
           self.login_attempts = 0     



user1 = User("John", "Doe", 30, 180)
user1.increment_login()


print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)


from admin import Admin
my_admin = Admin("John", "Doe", 30, 180)
my_admin.privileges.show_privileges()





#9-13
import random
class Die:
      def __init__(self, sides=6) -> None:
            self.sides = sides
      def roll_die(self):
           print(random.randint(1, self.sides))


my_die = Die()
for i in range(10):
      my_die.roll_die()