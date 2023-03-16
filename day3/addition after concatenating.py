# input string
a= "3,2,6,5,1,4,8,9"
# convert input string to list of integers
b= [int(n) for n in a.split(',')]
# find positions of 5 and 8
pos_5 = b.index(5)
pos_8 = b.index(8)
# calculate sum of num1
num1 = sum(b[:pos_5]) + sum(b[pos_8+1:])
# calculate value of num2
num2 = int(''.join(map(str,b[pos_5:pos_8+1])))
# output sum of num1 and num2
print(num1+num2)
