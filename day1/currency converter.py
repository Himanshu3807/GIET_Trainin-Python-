'''n=float(input("Amount you want to convert= "))
currency = input("Enter your amount currency: ")
if(currency == 'Euro'):
    print("Amount in Indian Rupees: ",n*0.01417)
elif(currency == 'British Pound'):
    print("Amount in Indian Rupees: ",n*0.0100)
elif(currency == 'Australian Dollar'):
    print("Amount in Indian Rupees: ",n*0.02140)
elif(currency == 'Canadian Dollar'):
    print("Amount in Indian Rupees: ",n*0.02027)'''

def currencycal(n,curr):
    if curr=="Euro":
        print(n*0.01417)
    elif curr=="British Pound":
        print(n*0.0100)
    elif curr=="Australian Dollar":
        print(n*0.02140)
    elif curr=="Canadian Dollar":
        print(n*0.02027)

currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian Dollar")
currencycal(300,"Canadian Dollar")
