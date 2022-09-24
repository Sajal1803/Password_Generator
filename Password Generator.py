import random as x

def Generate_Pass(l=8):
    l1=["@","#","$","%","&","*","!"]
    upper = chr(x.randint(65,90))
    lower = chr(x.randint(97,122))
    special = x.choice(l1)
    digit1 = str(x.randint(10000,99999))
    digit2 = str(x.randint(1000,9999))

    Password = upper + lower + special + digit1 + digit2
    l2 = x.sample(Password,l)
    Password = ("").join(l2)
    return Password

num = int(input("Enter Password length(max:-12:)"))
Pass = Generate_Pass(num)
print(Pass)
