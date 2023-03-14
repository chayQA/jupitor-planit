class Test:
    def __init__(self):
        self.a=12
        print(self.a)
        self.a +=1
        print(self.a)
        self.s=22
        print(self.s)

    def instance_variable(self):
        self.a=30
        print(self.a)
        self.a +=1
        print(self.a)
        self.b=35
        self.b +=1
        print(self.b)
        del self.b 


obj = Test()
obj.instance_variable()
print(obj.__dict__)
del obj.s
print(obj.__dict__)
