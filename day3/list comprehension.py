#list comprehension
#for loop version
result=[]
for i in range(11):#(0 to 10)
    result.append(i)
print(result)
#list compehension version
print([i for i in range(11)])
'''
'''
#for loop version(odd numbers)-->
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
#list compehension version
print([i for i in range(11)if i%2!=0])
print([i if i%2!=0 else i**2 for i in range(11)])

#for loop version(even numbers)-->
result=[]
for i in range(11):
    if i%2==0:
        result.append(i)
print(result)
#list compehension version
print([i for i in range(11)if i%2==0])

#for loop (odd---> square)
#even---> (cube)
#list comprehension method
result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
list1 = sum(mat, [])
for i in list1:
    if i%2!=0:
        result.append(i**3)
    else:
        result.append(i**2)
print(list1)
print(result)

#for loop method
#odd-->square
#even-->cube
#in a given matrix
result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)
#list copmprehension
print([ele**2 if ele%2!=0 else ele**3 for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])























