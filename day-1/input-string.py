"""
Input Data String
"""

# solicitar dados ao usuario
# funcao input()

# criar variavel para armazenar o dado do usuario
name = input("What is your name? ")

"""
What is your name? 
"""

# exibir o nome do usuario
#print(name)

"""
What is your name? Danilo
Danilo
"""

"""
Formatando saida de Strings
"""

# declarar variaveis que vao receber dados dos usuarios
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

# concatenar os valores
#"texto1" + "texto2" + "texto3"
#format()
print("{}, you like a {} {}!".format(name, color, animal))

"""
What is your name? Danilo
What is your favorite color?  Azul
What is your favorite animal?  Cachorro
Danilo, you like a Azul Cachorro!
"""