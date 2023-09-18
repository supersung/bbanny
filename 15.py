x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)
print(x is z)
print(x is not y)

a = 5
b = 5

print(a is not b)
print(a is b)

3 == 3.0
3 is 5.0

a = 3
b = 3.0

print(a == b)
print(a is b)
print(a is not b)

a = [3,5,1]
b = a

print(a[0])
a[0] = 2
print(a)
print(b)
print(a, b)

x = 2 ** 3 ** 2
print(x)

x = 2 + 3 * 4
print(x)

x = 10 / 5 / 2
print(x)

x = 2 ** 3 ** 2
print(x)

x = 10 % 3 % 2
print(x)

x = 1 + 2 > 3 and 4 - 1 < 2
print(x)


x = not false and true
print(x)

x= not true or false and True
print(x)

x = 1 & 2 | 3 ^ 4
print(x)

x = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(x)

x = 2 * -3 // 2
print(x)

x = 1 == 2 != 3
print(x)

x = 10
if x > 0 :
    print("x is positive") 

x = -4
if x > 0:
    print("x is positive") 
elif x < 0 :
    print("x is negative")
    
x = 0
if x > 0 :
     print("x is positive")
elif x < 0 :
     print( "x is negative")
else :
     print( "x is zero")

num = 3
if num % 2 == 0 :
    print( "짝수") 
else: 
    print("홀수")
    
a = 3 , b = 5
if a == b :
    print("같다")
else :
    print("다르다")
    
"문자" = a

if "문자" == a :
    print("a이다")
elif  "문자" == b :
    print("b이다")  
else : 
    print( "a도 b도 아니다")

fruits = ["apple", "banana", "cherry"]

for i in fruits :
    print(i)
    
my_list = [[1,2,3], [4,5,6], [7,8,9]]

for row in my_list:
    for num in row:
        print(num)
        
###

for i in range(10):
     print(i)
            
       
for char in "python":
    print(char)

fruits = ["apple", "banana", "cherry"]
for i in reversed(fruits):
    print(i)
 
for i in sorted(fruits):
     print(i)
        
for i in range(1,10):
    for j in range(1,10):
        print(i, "x", j, "=", i*j)
        
rang = [5,8,3,1,6]
 
for i in rang:
    print("element :", i)
else :
    print("end process")

""""""


for i in range(10) :
    if i == 7:
        print("break",i)
        break
    elif i == 1:
        print("continue",1)
        continue
    else:
        print("pass",i)
        pass
    
    print(i)   
    
i = 1

while i <=5:
    print(i)
    i += 1        

i = 1
while i <= 9 :
    print(i)


str_word = "python"
i = 0 

while i < len(str_word) :
    print(str_word[i])
    i += 1  
    
sum = 0
i =1
 
while i <= 10:
    sum += i
    i += 1
    
print(sum)

i = 1
while i<= 100:
    if i %2 ==0:
        print("짝수 : ", i)
    elif 1 %2 == 1:
        print("홀수 : ", i)
    i += 1
    
i = 1
while i<= 100:
    if i % 7 ==0 :
        print(i)
    i += 1               



    
         
    
    