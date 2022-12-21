# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos


# Kitų failų ir žemiau esančio kodo nekeiskite
# * a = addition(one, four);
# * b = divivsion(four, two);
# * c = substraction(three, two);
# * d = multiplication(five, two);

# * print(a);
# * print(b);
# * print(c);
# * print(d);


#! Sprendimas
#!------------------------------------------------------------------------------


from modules.math.composition import composition as addition
from modules.math.division import division as divivsion
from modules.math.multiplication import multiplication
from modules.math.subtraction import substraction
from modules.numbers.numbers import one, two, three, four, five


a = addition(one, four)
b = divivsion(four, two)
c = substraction(three, two)
d = multiplication(five, two)

print(a)
print(b)
print(c)
print(d)
