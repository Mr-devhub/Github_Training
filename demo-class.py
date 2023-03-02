class A:
    def __init__(self):
        print("This will print default constructor")

    def __init__(self,a,b,c):
        print("Invoking parameterized constructor")
        self.a = a
        self.b = b
        self.c = c
    

    def total(self) -> int:
        tot = self.a + self.b + self.c
        return int(tot)
    
# obj1 = A()
obj2 = A(1,2,3)

print(obj2.total())