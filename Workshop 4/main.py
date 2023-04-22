# task 6-1
character = {'name': 'Peter', 'lastname':'Griffin', 'age': 46, 'city': 'Quahog' }


print(character)




# task 6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 12,
    'David': 22,
    'Eve': 3,
}

for name, number in favorite_numbers.items():
    print(name + "'s favorite number is " + str(number) + ".")


# task 6-3



keys: list = ['Ten', 'Twenty', 'Thirty']
values: list = [10, 20, 30]

nums = dict(zip(keys, values))
print (nums)



dict1 = {'Ten':10, 'Twenty':20, 'Thirty': 30}
dict2 = {'Thirty':30, 'Fourty':40, 'Fifty':50}


dict1.update(dict2)

print(dict1)



# 6-4


# 6-5

rivers = {'nile':'egypt', 'amazon':'brazil', 'yangtze':'china'}

# 1
for key,  value in rivers.items():
    print('The', key, 'runs through', value)

# 2
for river in rivers.keys():
    print(river)   

# 3 
for country in rivers.values():
    print(country)


#6-6

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

person = ['jen','sarah','edward','phil','john','peter' ]

for people in person:
    if people in favorite_languages.keys():
        print(f'Thank you, {people.title()}, for taking the poll!')
    else:
        print(f"{people.title()}, we invite you to take our favorite languages poll.")    




# 6-7
character1 = {'name': 'Peter', 'lastname':'Griffin', 'age': 46, 'city': 'Quahog' }
character2 = {'name': 'Elliot', 'lastname':'Alderson', 'age': 28, 'city': 'New York City'}
character3 = {'name': 'Walter', 'lastname':'White', 'age': 52, 'city': 'Albuquerque'}

people = { 
  'character1': character1,
  'character2':character2,
  'character3':character3
}

print (people ['character1'])
print (people ['character2'])
print (people ['character3'])



# 6-8


pets = [
    {'species':'dog', 'owner':'george'},
    {'species':'cat', 'owner':'jack'},
    {'species':'parrot','owner':'elliot'}
]

for pet in pets:
    print(f"{pet['owner']}'s pet is a {pet['species']}.")



# 6-9
favorite_places = {'george':'gym', 'nick':'school', 'jake': 'university'}


for person, place in favorite_places.items():
   print(f"{person}'s favorite place is {place}.")



#6-12






#7-4

toppings = []


while True:
   topping = {input('Enter a pizza topping (enter "quit" to finish):')}

   if topping== "quit":
       break
   toppings.append(topping)
   print(f"adding {topping} to your pizza...")

   print("Your pizza is ready with the following toppings:")
for topping in toppings:
    print(f"- {topping}")
    


#7-7
nums = 1

while nums > 0:
    print(nums)
    nums +=1



# 7-8

sandwich_orders = ["tuna_sandwich", "cheese_sandwich", "ham_sandwich"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"{sandwich.title()}is done.")


# 7-10
poll_response = {}

while True:
    user = input("What is your name? (Enter 'quit' to exit poll.)")

    if user == 'quit':
     break
    response = input("If you could visit one place in the world, where would you go? ")
    poll_response[user]= response
print("Poll results:")
for user, response in poll_response.items():
    print(f"{user} would like to visit {response}.")


# 8-1

def display_message():
    print("In this chapter, we're learning about functions in Python.")

display_message()


# 8-2

def favorite_book(title):
   print(" One of my favorite books is Alice in Wonderland.") 

favorite_book("Alice_in_Wonderland")   

# 8-3

def make_shirt(size, text):
   print(f"A {size}-sized shirt will be made with the message: {text}")

make_shirt("medium", "Hello, World!")

make_shirt(size="large", text="Python is awesome!")


# 8-5
def describe_city(city, country="georgia"):
    print(f"{city} is in {country}")

describe_city("tbilisi")
describe_city("rome","Italy")
describe_city("reykjavik", "Iceland")


# other tasks


sampleDict = {
    "class": {
    "student": {
    "name":"Mike",
    "marks":{
    "physics":70,
    "history":80
    }
  }
 }
}

history_marks = sampleDict['class'] ['student'] ['marks'] ['history']
print(history_marks)    




inputYourInfo = {
     "name": "",
     "surname": "",
     "age": "",
     "country": "",
     "capital": ""
}

for key in inputYourInfo:
    value = input(f"Enter your {key}: ")
    inputYourInfo[key] = value.capitalize()

print(inputYourInfo)



cities = [ {'name':'City1', 'population':1793230, },
           {'name':'City1', 'population':179340, },
           {'name':'City1', 'population': 2503, },
           {'name':'City1','population': 1, },
           {'name':'City1', 'population':1}
          
          
          ]



smallest_cities = []
largest_cities = []
min_pop = float('inf')
max_pop = float('-inf')

for city in cities:
    pop = city["population"]
    if pop < min_pop:
        smallest_cities = [city["name"]]
        min_pop = pop
    elif pop == min_pop:
        smallest_cities.append(city["name"])
    if pop > max_pop:
        largest_cities = [city["name"]]
        max_pop = pop
    elif pop == max_pop:
        largest_cities.append(city["name"])


print(f"The smallest cities are: {', '.join(smallest_cities)} (population: {min_pop})")
print(f"The largest cities are: {', '.join(largest_cities)} (population: {max_pop})")









employee = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    employee.pop(key)

print(employee)    









employees = [{'name':'kelly'}, {'name':'Emma'}, {'name':'John'}]
defaults = {'designation': 'Application Developer', 'salary': 8000 }

for employee in employees:
     employee.update(defaults)

print(employees)










#challenge 1


room = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 5, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

robot = (1, 1)

def is_empty_drawer(room, row, col):
    return room[row][col] == 0


for row in range(len(room)):
    for col in range(len(room[0])):
      
        if is_empty_drawer(room, row, col):
         
            room[row][col] = 2
          
            robot = (row, col)


room[1][1] = 5


print(room)









cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
 if car == 'bmw':
    print(car.upper())
else:
    print(car.title())