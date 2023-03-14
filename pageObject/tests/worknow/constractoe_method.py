class Test:

    def __init__(self,a,b,c,name="jayasree",*args,**kwargs):
        self.a=a
        self.b=b
        self.c=c
        self.name=name
        self.args= args
        self.kwargs=kwargs

obj = Test(11,12,13,"jayasree",e=12,d=12)
print(obj.__dict__)

