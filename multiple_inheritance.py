class A:
    arg1=200
    def __init__(self, var1):
        self.var1 = var1
        

    def method1(self):
        print("method1 calls")

class B:
    def __init__(self, var1, var2):
        self.var2 = var2

    def method2(self):
        print("method2 calls")

class C(A, B):
    def __init__(self, var1, var2, var3):
        super().__init__(var1)           
        B.__init__(self, var1, var2)      
        self.var3 = var3

    def method3(self):
        print("method3 calls")  

# Create object
obj1 = C(100, 200, 300)


obj1.method1()  
obj1.method2()  
obj1.method3() 

print(obj1.arg1)

 

print("var1 =", obj1.var1)
print("var2 =", obj1.var2)
print("var3 =", obj1.var3)
