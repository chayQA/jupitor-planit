class Test:
    
    @staticmethod
    def static_method():
        print("im static")

    def instance_method(self):
        print(self)
        self.static_method()
        Test.static_method()

    @classmethod
    def class_methods(cls):
        print(cls)
        Test.static_method()
        cls.static_method()

obj = Test()
obj.static_method()
obj.instance_method()
obj.class_methods()


