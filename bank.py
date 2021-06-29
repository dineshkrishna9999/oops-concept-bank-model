#parent class
class User:
    pass
    def __init__(self,name,age,gender):
          self.name = name
          self.age = age
          self.gender = gender
    def show_details(self):
          print("the name of the person is :",self.name)
          print("the age is :",self.age)
          print("gender:",self.gender)
#object
#p = User("ram",18,"male")
#p.show_details()
#child class
class bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("your account balance is :",self.amount)
    def withdraw(self,amount):
        self.amount= amount
        if self.amount > self.balance:
            print("insufficient balance! your account balance is :",self.balance)
        else:
            self.balance =  self.balance - self.amount
            print("after withdrawl your current acount balance is :",self.balance)

p = bank("kid",20,"female")
p.show_details()
p.deposit(5000000)
p.withdraw(100)
