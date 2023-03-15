#Decision  making statements
#read a no -->print(multiple of that x number) -->else  print(invalid)
a=int(input('Enter a number='))
if(a%3==0 and a%5==0):
    print("Number is divisible by both 3 and 5")
elif(a%3==0):
    print("Number is divisible by 3")
elif(a%5==0):
    print("Number is divisible by 3")
else:
    print("Invalid input")
