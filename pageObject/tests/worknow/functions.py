a=10
# a is global
#
#
#non local
#nested function 

def func():
    a = 10
    def inner():
        nonlocal a

        print(a)
        a += 1
        print(a)
    return inner()

#func()

def main_funct():
    a =15
    def inner():
        b = 30
        return(b)
    return inner()
print(main_funct())


        