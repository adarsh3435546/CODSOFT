import random
import string
print("*PASSWORD GENERATOR*")
upper=string.ascii_uppercase
lower=string.ascii_lowercase
number=string.digits
special="!@#$%^&*"
character=lower+upper+number+special
while True:
    len=int(input("enter the length of the pass word:"))
    if len>10:
        print("password must be less that 10 numbers:")
    else:
        password=""
        for i in range(len):
            password="".join([password,random.choice(character)])
        print("your requried password:",password)
        print("password is sucessfully generated")
    repeat = input("Do you want to generate another password [yes/no]: ")
    if (repeat == "no"):
        break
           
