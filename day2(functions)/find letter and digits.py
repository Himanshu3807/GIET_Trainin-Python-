#isaplha-->checks the available alphabets on a string
#isdigit-->checks the available digits on the string
def function(str1):
    lcount=0
    dcount=0
    for i in str1:
        if i.isalpha():
            lcount+=1
        elif i.isdigit():
            dcount+=1
        else:
            continue
    return[lcount,dcount]
print(function("Infosys 123"))
print(function("Alpha 1"))
print(function("GIETU NH33"))
print(function("Mission i3d4 235"))
