# multiple inheritances

class papa:
    a=100
    def med1(self):
        print("papa in instance")

class mama:
    b=200
    def med2(self):
        print("mama in instance method")

class nephew(papa,mama):
    c=300
    def med3(self):
        print("im nephew in instance method")

obj = nephew()
obj.med3()
obj.med2()
obj.med1()

print(obj.a)  # accessing clss variable out side class with obj .classvariable
print(obj.b)
print(obj.c)