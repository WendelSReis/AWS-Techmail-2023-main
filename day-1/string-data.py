"""
String Data
"""

# declarar uma variavel
myString = "This is a string."

# exibir valor da variavel
print(myString)

# tipo da variavel
print(type(myString))


# concatenacao
print(myString + " is of the data type " + str(type(myString)))


"""
This is a string.
<class 'str'>
This is a string. is of the data type <class 'str'>
"""

# concatenacao com variaveis
firstString = "water"
secondString = "fall"

# concatenar as variaveis para obter uma palavra
thirdString = firstString + secondString

# exibir concatenacao
print(thirdString)
print(firstString + secondString)

"""
waterfall
waterfall
"""