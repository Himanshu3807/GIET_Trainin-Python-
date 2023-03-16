'''def isPal(n):

	for i in range(len(n) // 2):
		if (n[i] != n[-1 - i]):
			return False
	return True
def convert(num):
	Snum = str(num)
	return Snum
def cPal(num):
	a= num - 1
	while (not isPal(convert(abs(a)))):
		a-= 1
	b= num + 1
	while (not isPal(convert(b))):
		b+= 1
	if (abs(num -a) > abs(num -b)):
		return b
	else:
		return a
if __name__ == '__main__':

	num = 99

	print(cPal(num))
'''
import sys
def next_smallest(num):
    for i in range (num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print (next_smallest(99))
print(next_smallest(1221))
