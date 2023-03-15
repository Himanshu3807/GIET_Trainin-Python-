#list---> Ordered(default index)
#
list=[]
print(list,type(list))
list1=[10,20,30,40]
print(list1,type(list1))
list2=[10,20.2,30+3j,True,"Python"]
print(list2,type(list2))
list3=([100,200,300,400])
print(list3,type(list3))
list4=[101,201,301,401]
list4.append(501)
list4.extend([601,701,801])
list4.insert(0,51)#insert is used to insert in the address value(address,value)
list4.insert(4,351)
print(list4,type(list4))
list4.remove(801)
print(list4,type(list4))
del list4[1]
print(list4,type(list4))


