print("Welcome to to do list")
print("1.Add tasks")
print("2.remove tasks")
print("3.show tasks")
print("4.Exit")

tasks=[]

while True:
    choice=input("1/2/3/4:")
    if choice=="1":
       task=input("what are your tasks:")
       tasks.append(task)
    elif choice=="2":
        task=input("which task to remove: ")
        tasks.remove(task)
    elif choice=="3":
         for task in tasks:
             print (task)
    elif choice=="4":
        break
    else:
        print("choose from 1/2/3/4")


