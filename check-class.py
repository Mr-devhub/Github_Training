class A:
    def __init__(self) -> None:
        pass
    
    def display(self):
        print("Class A")


class B(A):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Class B")
        return super().display()
        
class C(B):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Class c")
        return super().display()

obj1 = C()
print(obj1.display())