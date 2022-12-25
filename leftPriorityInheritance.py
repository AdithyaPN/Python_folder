class A:

    def __init__(self):
        print('from class A, parent ')

    def fun1(self):
        print('from class A')
objA = A()

class B():
    def __init__(self):
        print('from class B, child ')

    def fun2(self):
        print('from class B')
objB = B()

class C(A,B):

    def __init__(self):
        print('from class c, child of B and grand child of A ')
        super().__init__()

    def fun3(self):
        print('from class C')

objC = C()
# objC.__init__()