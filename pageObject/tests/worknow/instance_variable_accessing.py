class Test:

    def __init__(self): #constructor
        self.a=111
        print(self.a)
        print("im a constructor where u can call instance variable")

    def instance_method(self): # instance variable can created in instance method and constructor only
        self.b=112
        print(self.b)
        print("im a instance method- u can create instance variable ")

obj = Test()
obj.instance_method()
print(obj.__dict__)
print(obj.__set__)