class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap')

class Person:
    def quack(self):
        print('I am quacking like a duck')

    def fly(self):
        print('I am flapping my arms')

def quackfly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

d = Duck()
quackfly(d)

p = Person()
quackfly(p)