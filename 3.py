lst=[]
n=int(input("enter a number: "))
for i in range(n):
  a=(input("enter the task: "))
  lst.append(a)
print("The tasks are: ",lst)
while True:
      print("1.display the task",end="\n")
      print("2. remove a task",end="\n")
      print("3. add a task",end="\n")
      b=int(input("enter the choice: "))
      if b==1:
        print("the total number of task = ",lst)
      elif b==2:
        c=(input("enter the task you want to remove: "))
        if c in lst:
            lst.remove(c)
            print("the task sucessfully removed: ")
        else:
            print("invalid choice: ")
      elif b==3:
        c=(input("enter the task you want to add in your list: "))
        lst.append(c)
        print("the given task is sucessfully added: ")
      else:
          print("invalid choice: ")
      repeat = input("Do u want to continue [yes/no]: ")
      if (repeat == "no"):
        break