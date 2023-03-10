# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]


#! Sprendimas
#! -----------------------------------------------------------------------------------------------


# * Pirma uzduotis
# * -----------------------------------------------------------------------------------------------


def get_User_Average_Age(users):
    total_age = 0
    for user in users:
        total_age += user["age"]
    return total_age / len(users)


print(get_User_Average_Age(users))


# * Antra uzduotis
# * -----------------------------------------------------------------------------------------------


def get_Users_Names(array_input):
    users_names = [x["name"] for x in array_input]
    user_names_sorted = sorted(users_names)
    return user_names_sorted


print(get_Users_Names(users))
