class A:
    pass
    # def process(self):
    #     print('A process()')

class B:
    pass
    # def process(self):
    #     print('B process()')

class C(A, B):
    pass
    # def process(self):
    #     print('C process()')

class F:
    def process(self):
        print('F process()')


class D(C, F):
    pass
    # def process(self):
    #     print('D process()')



obj = D()
obj.process()
print(D.mro())
# F process()
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.F'>, <class 'object'>]
# D --> C --> A --> B --> F 

