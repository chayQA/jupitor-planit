class Test:

    #instance method
    def instance_method(self):
        print("im accessing instance methos with self ")
        print(self)
        #Test.instance_method()
    

    def code_reuse(self):
        print("i can call instance method to the call")
        self.instance_method()
        print("called the instance method")
        #Test.instance_method()
obj = Test()
obj.instance_method()
obj.code_reuse()