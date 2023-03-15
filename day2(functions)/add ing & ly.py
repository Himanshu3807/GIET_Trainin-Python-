def function1(str):
    if len(str)<3:
        return str
    elif(str[-3:]=="ing"):
        str+="ly"
        return str
    else:
        str+="ing"
        return str
print(function1("sleep"))
print(function1("amazing"))
print(function1("is"))
