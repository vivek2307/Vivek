"Program for Calculator using OOPS"
#BLL
class Calci:
    def __init__(self):
        self.no1=0
        self.no2=0
        self.res=0
    def add(self):
        self.res=self.no1+self.no2
    def sub(self):
        self.res=self.no1-self.no2
    def mul(self):
        self.res=self.no1*self.no2
    def div(self):
        self.res=self.no1/self.no2
#PL
while(1):
    cal=Calci()
    cal.no1=int(input("Enter First No:"))
    cal.no2=int(input("Enter Second No:"))
    ch=input("Enter Choice +,-,*,/  :")
    if(ch=="+"):
        cal.add()
        print("Result:",cal.res)
    elif (ch == "-"):
        cal.sub()
        print("Result:", cal.res)
    elif (ch == "*"):
        cal.mul()
        print("Result:", cal.res)
    elif (ch == "/"):
        cal.div()
        print("Result:", cal.res)
    else:
        print("Incorrect Choice")