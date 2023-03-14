class Test:
    def __init__(self):
        self.a=100
        print(self.a)
        print("im a const")


    def instance_method(self):
        self.b=200

obj = Test()
print(obj.__dict__)

obj.instance_method()
print(obj.__dict__)

obj.c=300
#print(obj.__dict__)
