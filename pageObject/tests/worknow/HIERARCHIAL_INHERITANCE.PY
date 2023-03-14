# hierarchal inheritance

class people():

    a = 10

    def pub(self):
        print("instance method on hierarchal intertance")

class people1(people):
    b = 20

    def pub2(self):
        print("instance method pub 2 with hieraechal ")

class people2(people):

    c = 30

    def pub3(self):
        print("instance method pub 3 with hierachal")

class people3(people):
    d=33
    def __init__(self):
        print("constructor ")
obj = people2()
# obj = people3()
obj.pub3()
# obj.pub3()
print(obj.c)

