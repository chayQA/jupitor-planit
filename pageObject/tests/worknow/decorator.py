# decorator 
# adding a functionality 2 a existing functionwith out modifing the actual function.
class deco:

     def func(*args,**kwargs):
         return args

         func(1,2,3,4,5,6,7,8,9)
f = deco()
f.func()

# creating a decorator for this function

def even_only(func):  # even_only is the name of the decorator, (func) is name of the method, takes as a argument.
    def inner(*args, **kwargs): # main func arguments taken arguments for inner 
        l = []
        for i in args:
            if i%2 ==0:
                l.append(i)
        return func(*l, **kwargs)

    return inner 

@even_only
def func(*args, **kwargs):
    return args 

func (1,2,3,4,5,6,7,8,9)

