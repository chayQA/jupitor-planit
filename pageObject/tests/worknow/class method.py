class Test:

    @classmethod
    def class_method(cls):
        print("im the cls method")


    def instance_method(self):
        print("im in instance method in class deco") 
        Test.class_method()

obj =Test()
#obj.class_method()
#obj.instance_method()
Test.class_method()
