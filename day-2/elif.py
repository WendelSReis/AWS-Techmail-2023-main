"""
Condicional com elif
Papelaria
"""

# solicitar que o usuario forneca a opcao
userReply = input("Enter stamps, envelope, or copy: ")

# condicionais
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    # soliciar ao usuario a quantidade de copias
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
# se nao satisfez as opcoes anteriores
else:
    print("Thank you, please come again.")
    
    
"""
Enter stamps, envelope, or copy: stamps
We have many stamp designs to choose from.
"""

"""
Enter stamps, envelope, or copy: envelope
We have many envelope sizes to choose from.
"""

"""
Enter stamps, envelope, or copy: copy
How many copies would you like? (Enter a number) 5
Here are 5 copies.
"""