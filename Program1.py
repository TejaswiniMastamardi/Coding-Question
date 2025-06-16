class Calculator:
    def __init__(self,a : float, b : float ,opr : str):
        self.a=a
        self.b=b
        self.opr=opr

    def calculate(self):
        if self.opr=='+':
            return self.a + self.b
        elif self.opr=='-':
            return self.a-self.b
        elif self.opr=='*':
            return self.a*self.b
        elif self.opr=='/':
            if self.b != 0:
                return self.a/self.b
            else:
                return "Indefinite"
        else:
            return "Invalid operation"
    
    
    
a=float(input("Enter first value : "))
b=float(input("Enter second value : "))
opr=str(input("Enter operation (+,-,*,/) : "))

calc=Calculator(a,b,opr)
result=calc.calculate()
print("result is ",result)
