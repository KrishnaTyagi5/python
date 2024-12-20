print()
import os
os.system('cls')
print("Welcome to our list process")
print("We are providing these functions")
print("1. Add task")
print("2. Delete task")
print("3. show task")
print("4. Select complete task")
print("5. Exit")
print()
b=1
L=[]
while True:
    print("Select your function (1 to 5) = ",end=" ")
    ch=int(input())
    if ch==1:
        b=0
        print("enter your task = ",end=" ")
        task=input()
        L.append(task)
        print("your task "+task+" is added")
    elif ch==2:
        if b==1:
             print(" you have no task ")
        else:    
            for  i in L:
                print(i)
            print("Select task to be deleted = ",end=" ")
            str=input()
            L.remove(str)
            print("Sucessfully deleted "+str+" task")
    elif ch==3:
        if b==1:
            print("you have no task ")
        else:    
            for i in L:
                print(i+"❌")
    elif ch==4:
        if b==1:
            print("you have no task ")
        else:
            print("select the task to be done = ",end=" ")
            str2=input()
            for i in L:
                if str2==i:
                    print(i+"✅")
                else:
                    print(i+"❌")
    else:
        exit(0)                  
