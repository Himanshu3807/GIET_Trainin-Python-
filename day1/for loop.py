#For loop
#range function
#numbers between 1 to 100
for i in range(0,101):
    #range(start,end,step)
    print(i,end=" ")
print("\nEven Numbers")    
#even number between 0 to 100
for i in range(0,101,2):
    print(i,end=" ")
print()
print("Odd Numbers")
#odd numbers between 0 to 100
for i in range(1,101,2):
    print(i,end=" ")
print()
print("Reverse Number")
#reverse order
for i in range(100,0,-1):
    print(i,end=" ")
