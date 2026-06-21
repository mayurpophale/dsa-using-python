""" class student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        print(self.name)
        a = (self.m1+self.m2+self.m3)//3
        print(a)


s1 = student("mayur",23,23,26)
s1.avg() """


class Acc:
    def __init__(self,bal,accno):
        self.balance = bal
        self.acc_no = accno

    def debit(self,amount):
        self.balance -= amount
        print(f"Rs.{amount} is debited")

    def credit(self,amount):
        self.balance += amount
        print(f"Rs.{amount} is credited")

    def bal(self):
        print("Balance of your account is",self.balance)

om = Acc(3000,320)
om.debit(1000)
om.credit(500)
om.bal()
