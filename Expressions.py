class Expression:

    def __init__(self, num1, num2, num3):
        
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        print("Expression object created!")

    def addNumbers(self):
        
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")
        return result

    def __del__(self):
       
        print("Expression object deleted.")

        
        

if __name__ == '__main__':

    
    exp1 = Expression(5, 10, 20)
    exp1.addNumbers()

    print()

    
    exp2 = Expression(3, 7, 2)
    exp2.addNumbers()

    
    del exp1
    del exp2
