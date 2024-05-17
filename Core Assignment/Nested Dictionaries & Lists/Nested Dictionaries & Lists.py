x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    "soccer": [{"name": "Lionel Messi", "age": 29}],
    "basketball": [{"name": "Steph Curry", "age": 34}],
    "baseball": [{"name": "Mike Trout", "age": 31}]
}
sports_directory["soccer"][0]["name"] = "Lionel Andres"
print(sports_directory)

z = [[10, 20, 30], [40, 50, 60]]
z[0][1] = 30
print(z)

x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

students = [{'first_name': 'Michael', 'last_name': 'Jordan', 'age': 58}, {'first_name': 'LeBron', 'last_name': 'James', 'age': 36}]
students[0]['last_name'] = 'Bryant'
print(students)

#Student :

def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"Key: {key}, Value: {value}")

# Example usage:
some_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
iterateDictionary(some_list)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

# Example usage:
students = [{'first_name': 'Alice', 'age': 30}, {'first_name': 'Bob', 'age': 25}]
iterateDictionary2('first_name', students)

students = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'LeBron', 'last_name': 'James'}, {'first_name': 'Kobe', 'last_name': 'Bryant'}, {'first_name': 'Magic', 'last_name': 'Johnson'}, {'first_name': 'Shaquille', 'last_name': 'ONeal'}, {'first_name': 'Kareem', 'last_name': 'Abdul-Jabbar'}, {'first_name': 'Wilt', 'last_name': 'Chamberlain'}, {'first_name': 'Bill', 'last_name': 'Russell'}, {'first_name': 'Larry', 'last_name': 'Bird'}, {'first_name': 'Tim', 'last_name': 'Duncan'}, {'first_name': 'Hakeem', 'last_name': 'Olajuwon'}, {'first_name': 'David', 'last_name': 'Robinson'}, {'first_name': 'Karl', 'last_name': 'Malone'}, {'first_name': 'Charles', 'last_name': 'Barkley'}, {'first_name': 'Patrick', 'last_name': 'Ewing'}, {'first_name': 'Clyde', 'last_name': 'Drexler'}, {'first_name': 'Isiah', 'last_name': 'Thomas'}, {'first_name': 'John', 'last_name': 'Stockton'}, {'first_name': 'Scottie', 'last_name': 'Pippen'}, {'first_name': 'Kevin', 'last_name': 'Garnett'}, {'first_name': 'Dirk', 'last_name': 'Nowitzki'}, {'first_name': 'Steve', 'last_name': 'Nash'}, {'first_name': 'Allen', 'last_name': 'Iverson'}, {'first_name': 'Dwyane', 'last_name': 'Wade'}, {'first_name': 'Ray', 'last_name': 'Allen'}, {'first_name': 'Reggie', 'last_name': 'Miller'}, {'first_name': 'Gary', 'last_name': 'Payton'}, {'first_name': 'Dennis', 'last_name': 'Rodman'}, {'first_name': 'Dominique', 'last_name': 'Wilkins'}, {'first_name': 'Chris', 'last_name': 'Webber'}, {'first_name': 'Vlade', 'last_name': 'Divac'}, {'first_name': 'Alonzo', 'last_name': 'Mourning'}, {'first_name': 'Mitch', 'last_name': 'Richmond'}, {'first_name': 'Chris', 'last_name': 'Mullin'}, {'first_name': 'Tim', 'last_name': 'Hardaway'}, {'first_name': 'Kevin', 'last_name': 'Johnson'}, {'first_name': 'Mark', 'last_name': 'Price'}, {'first_name': 'Jeff', 'last_name': 'Hornacek'}, {'first_name': 'John', 'last_name': 'Starks'}, {'first_name': 'Derek', 'last_name': 'Harper'}, {'first_name': 'Hersey', 'last_name': 'Hawkins'}, {'first_name': 'Spud', 'last_name': 'Webb'}, {'first_name': 'Muggsy', 'last_name': 'Bogues'}, {'first_name': 'Manute', 'last_name': 'Bol'}, {'first_name': 'Shawn', 'last_name': 'Kemp'}, {'first_name': 'Dikembe', 'last_name': 'Mutombo'}, {'first_name': 'Alonzo', 'last_name': 'Mourning'}, {'first_name': 'Vlade', 'last_name': 'Divac'}, {'first_name': 'Mitch', 'last_name': 'Richmond'}, {'first_name': 'Chris', 'last_name': 'Mullin'}, {'first_name': 'Tim', 'last_name': 'Hardaway'}, {'first_name': 'Kevin', 'last_name': 'Johnson'}, {'first_name': 'Mark', 'last_name': 'Price'}, {'first_name': 'Jeff', 'last_name': 'Hornacek'}, {'first_name': 'John', 'last_name': 'Starks'}, {'first_name': 'Derek', 'last_name': 'Harper'}, {'first_name': 'Hersey', 'last_name': 'Hawkins'}, {'first_name': 'Spud', 'last_name': 'Webb'}, {'first_name': 'Muggsy', 'last_name': 'Bogues'}, {'first_name': 'Manute', 'last_name': 'Bol'}, {'first_name': 'Shawn', 'last_name': 'Kemp'}, {'first_name': 'Dikembe', 'last_name': 'Mutombo'}


