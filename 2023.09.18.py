''' num = input("숫자를 입력하세요")
print("number", int(num))

a = 12.01
print(type(a))

a = "abcd"
print(type(a))

a = "65"
print(int(a))
print(str(a))
print(hex(a))
print(ord(a))

print(pow(2,2))
print(pow(2,6))

print(divmod(10,3)) '''

''' a = (3,5,7)
b = list(a)
c = tuple(b)

print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) '''

''' for i in range(2,7):
    print(i)
    
for i in range(1,20,3):
    print(i) '''

#max, min, sum
''' a = [3,5,6,9]
print(max(a))
print(min(a))
print(sum(a))  '''

#abs
''' print(abs(-3))
print(abs(-3000))
print(abs(-3,0)) '''

''' a= [5,3,1,9,4]
print(sorted(a))
print(sorted(a,reverse = True)) '''

#enumerate

''' a= [5,3.14,False, 9, "string"]
print(enumerate(a))
print(*enumerate(a))
 '''

#zip

''' a= [1,2,3]
b= [4,5,6]

print(*zip(a,b))  '''

#any,all

''' a= [True, True, False]
print(any(a))
print(all(a)) '''

#format

''' a= 20
b = 23
c= "a는 {}, b는 {}, format(a,b)"

print(c) '''

''' a= 3
print(globals(a))
print(locals(a)) '''

''' a=3
print(dir(a))

print(callable(a)) '''

''' add = lambda a, b : a + b

print(add(2,3)) '''


''' add = lambda a,b : a + b
print(add(2,3))

sub = lambda a,b : a - b
print(sub(10,2))

mul = lambda a,b : a * b
print(mul(2,5))

na = lambda a,b : a / b
print(na(10,2)) '''

''' def add_numbers(x,y) :
    return x + y
result = add_numbers(4,5)
print(result)  '''


''' def greet(name):
    print(name)
    print("hello", + name + "how are you?")
    
greet("배준성") '''

''' def add(a, b) :
    print(a+b)
    
add(3,6)

def sub(a,b) :
    return a - b

def mul() :
    return 2 + 4

def div() :
    print(4/2)
    
print(sub(3,5))
print(mul())
div() '''

''' def aa(a) :
    if a/2 == 1 :
        print("홀수")
    else : 
        print("짝수")

num = input("숫자를 입력하세요 : ")
aa(int(a)) '''

''' def reverse_string(msg):
    return msg[::-1]

in_str = input("문자열 : ")
print(reverse_string(in_str))  '''

''' def calcu(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
calcu(10,3)

def chong(a,b,c,d,e):
    print(a+b+c+d+e)
chong(1,2,3,4,5) '''

''' def hap(num) :
    return sum(num)
nums = []

for i in range(1,6) :
    innum = int(input(f"{i}번째 숫자 입력 : "))
    nums.append(innum)
    
print(hap(nums)) '''