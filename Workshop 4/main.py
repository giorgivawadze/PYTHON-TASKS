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