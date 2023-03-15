def fun(list,n):
    count=0
    for x in list:
        index=list.index(x)+1
        for y in range(index,len(list)):
            if x+list[y]==n:
                count+=1
    return count
list=[1,2,7,4,5,6,0,3]
n=6
print(fun(list,n))
