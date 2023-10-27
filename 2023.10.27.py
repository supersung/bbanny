""" class Person :
	name = "python"
	age = 23
	number = "01012345678"
 
def getIntroduce(self):
		return f"My name is {self.name}"

print(getIntroduce(Person))
 
 
p = Person()
print(p.name)
print(p.age)
print(p.number)
print(getIntroduce(Person)) """

""" class Person :
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
        
p = Person("hello", 24,'01111111111')
print(p.name)
print(p.age)
print(p.number)


p1 = Person("he", 21, "0100")

print(p1.name)
print(p1.age)
print(p1.number) """

class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count
p = Person("hello", 24, "01087654321")
print(p.name)
print(p.getCount())
p1 = Person("he", 21,"0108")
print(p1.name)
print(p1.getCount())
p2 = Person("hee", 24, "028333821")
print(p2.name)
print(p2.getCount())