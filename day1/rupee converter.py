n=float(input("Amount you want to convert= "))
currency = input("Enter your amount currency: ")
if(currency == 'Euro'):
    print("Amount in Indian Rupees: ",n*0.01417)
elif(currency == 'British Pound'):
    print("Amount in Indian Rupees: ",n*0.0100)
elif(currency == 'Australian Dollar'):
    print("Amount in Indian Rupees: ",n*0.02140)
elif(currency == 'Canadian Dollar'):
    print("Amount in Indian Rupees: ",n*0.02027)
