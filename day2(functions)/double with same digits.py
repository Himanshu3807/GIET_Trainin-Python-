'''def check_double(number):
    num2=number*2
    if(len(str(num2))==len(str(number))) and (str(num)==str(num2)):
       return True
    else:
        return False
    
print(check_double("125874"))'''
def check_double(number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
    if count==len(number):
        return True
print(check_double(245))
print(check_double(125874))
