""" for i in reversed(range(1,6)):
    print(i * "*")
    

for i in range(1,6):
    print((i * "*"))
    
for i in range(1,6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i -1)
    print(spaces + stars)
    
    
for i in range(6,0,-1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i -1)
    print(spaces + stars)
    

num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
    



""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = [] """
    
    
""" import random

choices = [1,2,3]

user_choice = input("가위,바위,보 중에 하나를 선택하세요: ").lower()
computer_choice = random.choice(choices)

print(f"사용자:{user_choice}")
print(f"컴퓨터: {computer_choice}")

if user_choice == computer_choice:
    print("무승부")
    
elif(
    (user_choice == 1 and computer_choice == 3) or
    (user_choice == 2 and computer_choice == 1) or
    (user_choice == 3 and computer_choice == 2)
) : 
    print("사용자 승")
    
else :
    print("컴퓨터승")1
     """
    
    
    
""" import random

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    
    if user_choice == pcnum :
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or 
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else :
        print("패")
        return
    
print("1: 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")

chnum = input()

determine_winner(chnum) """


""" file = open("temp.txt", "w")
file.close() """

""" file = open("temp.txt", 'a')
file.close() """

""" file = open("temp.txt", 'a')

file.write("banny!!!. \n")
file.write("qownstjdl") """

""" f = open("C:\\Users\\Catholic\\temp.txt", "w")
for i in range(100) :
    f.write(f"{i}\n")
    
f.close() """

""" file = open("C:\\Users\\Catholic\\temp.txt", "a")

file.write("hello\n")
file.write("world")

file.close() """

""" f = open("C:\\Users\\Catholic\\temp.txt", "r")
res = f.read()
print(res)

f.close()
 """
""" file = open("C:\\Users\\Catholic\\temp.txt", "r")

for i in range(110) :
    res = file.readline()
    print(res)

file.close() """


""" file = open("C:\\Users\\Catholic\\temp.txt", "r")

res = file.readlines()
print(res)

file.close() """



""" file = open("C:\\Users\\Catholic\\temp.txt", "r")
line = file.readlines()
for l in line :
    print(l)
    
file.close() """


file = open("C:\\Users\\Catholic\\temp.txt", "r")
for line in file :
    print(line)
    
    
file.close()