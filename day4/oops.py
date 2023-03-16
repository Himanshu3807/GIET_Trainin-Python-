'''class Employee:
    def __init__(self):
        self.employee_id = None
    def check_eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benfits")
        else:
            print("The employee is not eligible for special benefits")

emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()
emp2=Employee()
emp2.employee_id=4500

class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())


class Customer:
    def __init__(self,id):
        self.id=100
c1=Customer(200)
print(c1.id)




class Book:
    def init(self):
        self.title=None

my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"

print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)


class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "Shoe with price:" +str(self.price)+ " \nMaterial:" +str(self.material)
s1=Shoe(2000,"Canvas")
#print("The unique id of the object is ",id(s1))
print(s1)
#print(s1.price,s1.material)


class Mobile:
    def display(self):
        print("Displaying details")

    def purchase(self):
        self.display()
        print("Calculating Price")
Mobile().purchase()


class Mobile:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price
        self.total_price = None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price = self.price - self.price*(discount/100)
        print("Total price of", self.brand, "mobile is", self.total_price)
    def amount_returned(self):
        return (self.price - self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())

#__function name() is treated as private
#function name() is treated as public
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance
    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is ", self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()


class Dam:
    def __init__(self, name, length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam", 3.5)
print("Dam name:", dam1.name)
print("Dam Length", dam1.length())


class Table:
    def init(self):
        self.no_of_legs=4
        self._glass_top=None
        self._wooden_top=None
    def assign_data(self, glass_top,wooden_top):
        self._glass_top=glass_top
        self._wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self._glass_top==True):
            rate=20000
        elif(self._wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate (False, True)
print(rate)

class Table:
    def __init__(self):
        self.no_of_legs=4
        self._glass_top=None
        self._wooden_top=None
dining_table = Table()
back_table = Table()
front_table = back_table
back_table  = dining_table
print(dining_table, back_table, front_table )'''
