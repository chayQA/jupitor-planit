class parent: #parent is clas name
    a = 10 # class variable

    def m1(self): # instance method
        print("parent class method")

class child(parent): # child is a class name nd inhertance concept
    pass


c = child() # c- is a object , chid is class name
c.m1()
c.a
print(c.a)
print(c.m1())



    