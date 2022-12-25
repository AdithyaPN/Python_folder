class A:

    def __init__(self):
        print('from class A, parent ')

    def fun1(self):
        print('from class A')

    def fun2(self):
        print('from class A')

    def fun3(self):
        print('from class A')

class B(A):
    def __init__(self):
        print('from class B, child ')
        super().__init__() #super() method to access parent's properties in a child

    def fun4(self):
        print('from class B')

    def fun5(self):
        print('from class B')

    def fun6(self):
        print('from class B')

#single inheritance
objB = B()
# objB.fun1()

class C(B):
    def __init__(self):
        print('from class c, child of B and grand child of A ')
        super().__init__() #super() method to access parent's properties in a child

    def fun7(self):
        print('from class C')

    def fun8(self):
        print('from class C')

    def fun9(self):
        print('from class C')

objC = C()
