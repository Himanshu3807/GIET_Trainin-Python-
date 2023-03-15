array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
result=[array[i:j+1] for i in range(len(array))
        for j in range(i,len(array))]
print(result)
