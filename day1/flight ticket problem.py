'''a=int(input("Enter the number of Adults"))
c=int(input("Enter the number of Child"))
adult=(a*37550.0)
child=(c*37550.0/3)
service= (adult+child)*7/100
total= adult+child+service
discount=(adult+child+service)*10/100
final=(adult+child+service-discount)
print("Total amount for group:",final)'''


a=int(input("Enter the number of Adults"))
c=int(input("Enter the number of Child"))
print((((a*37750.0)+(c*37750.0/3))*1.07)*0.90)
