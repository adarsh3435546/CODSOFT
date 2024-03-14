def add(a, b):
    c = a + b
    print(c)

def sub(a, b):
    c = a - b
    print(c)

def mul(a, b):
    c = a * b
    print(c)

def div(a, b):
    c = a / b
    print(c)

def rem(a, b):
    c = a % b
    print(c)

def exp(a, b):
    c = a ** b
    print(c)

def sqrt(a):
    c = a ** 0.5
    print(c)

while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print("1. Add\n2. Subtract\n3. Multiplication\n4. Division\n5. Remainder\n6. Exponentiation\n7. Square Root\n")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)
    elif choice == 5:
        rem(a, b)
    elif choice == 6:
        exp(a, b)
    elif choice == 7:
        sqrt(a)
    else:
        print("Enter a valid number:")
        
        
    repeat = input("You need to continue [yes/no]: ")
    if (repeat == "no"):
        break