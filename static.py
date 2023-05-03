class person(object):
    population = 50 # Class variable

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name}, {self.age}"
    
    @classmethod
    def getPopulation(cls): # Passes class as variable
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, ' is ', self.age, ' years old')

p1 = person('Ian', 57)
print(p1)
print(person.getPopulation())
print(person.isAdult(9))
print(person.isAdult(21))
print(person.isAdult(p1.age))