# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


#! Sprendimas
#! ----------------------------------------------------------------------------------------


def show_object_keys(obj):
    return list(obj.values())


print(show_object_keys(audi))
