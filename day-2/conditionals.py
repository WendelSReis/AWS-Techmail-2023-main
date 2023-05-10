"""
Working with Conditionals
"""

# requisitar dado do usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# condicional
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
"""
Do you need to ship a package? (Enter yes or no) no
--------
Do you need to ship a package? (Enter yes or no) no
Please come back when you need to ship a package. Thank you.
"""

"""
Do you need to ship a package? (Enter yes or no) yes
We can help you ship that package!
"""