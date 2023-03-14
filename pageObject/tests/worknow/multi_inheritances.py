class multi:

    a=11  # class variable

    def m1(self):
        print("im instance method")

class multi1(multi):

    b=12

    def m2(self):
        print("im instance mehod -2")

class multi2(multi1):

    c=13

    def m3(self):
        print("im instance method-3")

# obj = multi()
# print(obj.a)

# obj = multi1()
# print(obj.b)
# obj.m2

obj = multi2()
print(obj.c)
print(obj.b)
print(obj.a)

obj.m1()
obj.m2()
obj.m3()
