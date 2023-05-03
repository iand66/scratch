class Person:
    def __init__(self, name, age, gender) -> None:
        self.__name = name # Private Attributes
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

p1 = Person("Ian", 57, 'M')
print(p1.Name)