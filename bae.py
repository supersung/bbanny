my_set = set([5,8,3,7,1,"h"])
print(my_set)
set_tmp = set("hello")
print(set_tmp)
my_set = {5,8,3,7,1,"h"}
set_item = {7,8,4,2,"h"}
print(my_set | set_item)
print(my_set.union(set_item))
print(my_set - set_item)
print(my_set.difference(set_item))
print(my_set & set_item)
print(my_set)
my_set.add(9)
print(my_set)
my_set = {5,8,3,7,1,"h"}
my_set.clear()
print(my_set)
my_set = {5,8,3,7,1,"h"}
my_set.discard(2)
print(my_set)
my_set.difference_update(set_item)
print(my_set)
my_int = 10
my_str = str(my_int)
type(my_int)
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)
print(my_str + "hello")

my_str = '10'
my_int = int(my_str)
print(my_int)
type(my_int)

my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int('10')
print(my_int2)

a = 10
b = 3
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a//b
print(c)
c = a%b
print(c)
c = a**b
print(c)

a = 2
print(a)

a += 2
print(a)

a -= 1
print(a)

a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a*=4
print(a)

a /= 2
print(a)

a **= 3
print(a)

a = 10
b = 4

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

a = 1
b = 0

print(a and b)
print(a or b)
print(not b)

x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)

a = 10
b = 3

print(a & b)
print(a ^ b)
print(~a)
print(a << b)
print(a >>b)

my_list = [9,4,3,7,8,'hi']
print(4 in my_list)
print(2 in my_list)
print(2 not in my_list)

my_dic = {"key":"v1", "k2" : "v2"}
print("k2" in my_dic)

