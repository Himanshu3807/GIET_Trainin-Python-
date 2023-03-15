#categories of function
#based on arguments
#positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,200,300,400)
function1(1,2,3,4)

#keyword arguments

def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num3=20,num1=30,num2=40)

#default arguments
def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("aditya",11,"CSE")
function3("shekhar",11,"CST")
function3("mayank",13,"CST")
function3("kumar",14,"CST")

def function4(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function4("aditya",11)
function4("shekhar",11,"CST")
function4("mayank",13,"ECE")
function4("kumar",14)

#variable no of arguments
def function5(*var): #tuple=
    for i in var:
        print(i,end=" ")
function5(10,20)
print()
function5(10,20,30,40)
print()
function5(10,20,30,40,50,60)

#function overloading
#addition using functions
def add(*var): #tuple=
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))















    
    
