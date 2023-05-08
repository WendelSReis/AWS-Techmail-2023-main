"""
Working with Lists, Tuples, and Dictionaries
"""

# LISTA

# criar nossa lista de dados
# myFruitList = ["apple", "banana", "cherry"]

# exibir dados da lista
# print(f'LISTA: {myFruitList}')

# exibir tipo do dados
# print(type(myFruitList))

# exibir apenas o dado na posicao desejada
# print(myFruitList[0])

"""
LISTA: ['apple', 'banana', 'cherry']
<class 'list'>
apple
"""

# alterar dado na posicao desejada
# dados mutavel // permite alterações

# myFruitList[2] = "Laranja"

# print(f'ALTERADO: {myFruitList}')

"""
LISTA: ['apple', 'banana', 'cherry']
<class 'list'>
apple
ALTERADO: ['apple', 'banana', 'Laranja']
"""


# TUPLA

# criar nossa tupla
#myFinalAnswerTuple = ("apple", "banana", "pineapple")

# exibir dados da tupla
#print(myFinalAnswerTuple)

"""
('apple', 'banana', 'pineapple')
"""

# acessar posicao na tupla
#print(myFinalAnswerTuple[1])

"""
('apple', 'banana', 'pineapple')
banana
"""

# TUPLA NAO PERMITE ALTERACAO DAS INFORMACOES DECLARADAS

# alterar valor da tupla
#myFinalAnswerTuple[2] = "Abacaxi"

# exibir alteracao
#print(myFinalAnswerTuple)

"""
('apple', 'banana', 'pineapple')
banana
Traceback (most recent call last):
  File "/home/ec2-user/environment/day-1/composite-data.py", line 61, in <module>
    myFinalAnswerTuple[2] = "Abacaxi"
TypeError: 'tuple' object does not support item assignment
"""


# DICIONARIO

# criar dicionario
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}

# exibir dados do dicionario
print(myFavoriteFruitDictionary)

"""
{'Akua': 'apple', 'Saanvi': 'banana', 'Paulo': 'pineapple'}
"""

# acessar valores atraves das chaves
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Paulo"])
print(myFavoriteFruitDictionary["Saanvi"])

"""
apple
pineapple
banana
"""
