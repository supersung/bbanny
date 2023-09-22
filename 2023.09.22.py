""" def prt_func() :
    print("hello")
    
def callfunc(fx) :
    fx()
    
callfunc(prt_func)    """


""" def prt_func() :
    for i in range(0,5) :
        print("hello", i)

def callfunc(fx) :
    fx()
    
callfunc(prt_func)    """


""" def update_msg(name: str) -> list:
    msg = []
    msg.append("hello, " + name)
    return msg


def greeting(in_name :str) -> list :
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg

res = greeting("python")

for message in res:
    print(message) """


""" def fun(n) :
    if n == 5 :
        return
    
    print(1,n)
    fun(n+1)
    
fun(1) """


""" def ploop(n) :
    if n == 0:
        print("end")
        return 1
    else :
        print(n,n-1, "=", n + n-1)
        return n * ploop(n-1)
    
print(ploop(3)) """

""" def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res = ", res) """


import calc

""" print(dir(calc))

add_res = calc.add(8,4)
sub_res = calc.sub(8,4)
mul_res = calc.mul(8,4)
div_res = calc.div(8,4) """


import calc as cl
""" add_res2 = cl.add(10,20)

print(cl.add(100,4))
print(cl.sub(100,4))
print(cl.mul(100,4))
print(cl.div(100,4))
 """
 
 
""" import mod.circle_mod as cm

print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5))

def cutstr(st,wd, idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
rs = cutstr(url, "/", 4)
print(rs)

import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutstr(url, "/", 3)
print(res) """

import math
""" 
sq_res = math.sqrt(6)
print(sq_res)

sp_res = math.sin(math.pi/2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)


exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fc_res = math.factorial(4)
print(fc_res)

import mod.utils as mu

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi) """

import random as rd

res = rd.randint(1,100)
print(res)

my_list = ["apple", "banana", "cherry"]
ret = rd.choice(my_list)
print(ret)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres)