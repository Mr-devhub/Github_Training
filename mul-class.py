class A:

    def __init__(self,a,b,c):
        print("Invoking parameterized constructor")
        self.a = a
        self.b = b
        self.c = c
    

    def total(self) -> int:
        tot = self.a * self.b * self.c
        return int(tot)
    

obj1 = A(10,20,30)

print(obj1.total())