# parameters in function
def function_name(para1,para2,para3):
    print(para1,para2,para3)
    para1 +=20
    print(para1)

#function_name(10,20,3)
#function_name(10,4,33)



def function_default(para1,para3,para2=11):

    print(para1,para2,para3)

#function_default(10,12,13)

def fun_multi_argmnr(*args):
    print(args)

#fun_multi_argmnr(11,12,12,13,14)

def fun_muti_keywords(**kwargs):
    print(kwargs)

#fun_muti_keywords(a=1,z=2,x=3)


def fun2(a,l=[]):
    print(a)
    l.append(a)
    print(l)

fun2(10)
fun2(11)
fun2((113,14))