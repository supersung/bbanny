""" class MyClass:
    count = 0
    
    def __init__(self, num):
        self.count = num
        
    def clsMethod(cls):
        cls.count += 1
        print(f"cls count = {cls.count}")
        
        
    def instMethod(self):
        self.count += 1
        print(f"instance = {self.count}")
        
        
MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
 """

""" class 챔피언:
    def __init__(self, 이름, 체력=100, 레벨=1, 스피드=300, 공속=1.0, 스킬=""):
        self.이름 = 이름
        self.체력 = 체력
        self.레벨 = 레벨
        self.스피드 = 스피드
        self.공속 = 공속
        self.스킬 = 스킬

    def 업뎃공속(self, 증가분):
        self.공속 += 증가분

    def 업뎃스피드(self, 증가분):
        self.스피드 += 증가분

    def 업뎃스킬(self, 스킬명):
        self.스킬 = 스킬명

    def 업뎃레벨(self, 증가분=1):
        self.레벨 += 증가분
        self.체력 += 20 * 증가분  


에쉬 = 챔피언("에쉬", 140)
미포 = 챔피언("미포", 220)


에쉬 = 챔피언("에쉬", 140)  
에쉬.업뎃레벨(4)  

print(f"에쉬의 이름: {에쉬.이름}")
print(f"에쉬의 체력: {에쉬.체력}")
print(f"에쉬의 레벨: {에쉬.레벨}")
print(f"에쉬의 스피드: {에쉬.스피드}")
print(f"에쉬의 공속: {에쉬.공속}")
print(f"에쉬의 스킬: {에쉬.스킬}") """

""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
        
yasuo = Yasuo("Yasuo")

yasuo.getName()

yasuo.attck("Q")

yasuo.getLevel()

yasuo.levelup()
yasuo.getLevel() """


""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)


class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return


class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return


yasuo = Yasuo("Yasuo")
garen = Garen("Garen")


yasuo.attck("Q")

yasuo.levelup()

yasuo.getLevel()


garen.attck("R")

garen.levelup()

garen.getLevel()
 """
 
 
""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())


sett = [circ, rect]

for st in sett :
    print(st.area()) """
    
    
""" class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
        
      
person = Person("Alice", 30, 12345)


print(person.name)  
print(person.age)  


person.name = "Bob"  
person.age = 25  


print(person.name) 
print(person.age)  """



""" class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()



person = Person("John", 25, 123)


student = Student("Alice", 20, 456)
teacher = Teacher("Mr. Smith", 35, 789)


print(getPersonName(person))  
print(getPersonName(student)) 
print(getPersonName(teacher))  
 """
class Person:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.number = num

    def getName(self):
        return self.name

    def setName(self, new):
        self.name = new

    def getNumber(self):
        return self.number

    def setNumber(self, newNum):
        self.number = newNum

p1 = Person("John", 30, "123456789")
p2 = Person("Alice", 25, "987654321")


print(p1.getNumber())  
print(p2.getNumber()) 


p1.setNumber("11111111111")  
print(p1.getNumber())  

p1.setNumber("22222222222")  
print(p1.getNumber())  




