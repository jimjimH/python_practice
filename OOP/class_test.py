class Person():
    count = 0
    def __init__(self, name):
        self.name = name
        self._foo = 'foo'
        self.__baz = 'baz'
        Person.count += 1

    def anounce(self):
        print('I am a good person!')

    @classmethod
    def how_many_people(cls, feeling):
        print(cls.count, feeling)
    
    @staticmethod
    def guess(guess):
        if guess == Person.count:
            print('Correct!')
        elif guess < Person.count:
            print('more than your guess')
        else:
            print('less than your guess')

class Man(Person):
    def __init__(self, name):
        super().__init__(name)
        self.gender = 'male'

    def __speak(self):
        print('I am a man')

    def anounce(self):
        super().anounce()
        print('And I am a man.')

class Test():
    pass


person = Person('person')
jim = Man('jim')
terrence = Man('terrence')

# instance method 只能被 instance 呼叫，不能被 class 呼叫
jim.anounce()
# Person.anounce()
# > TypeError: anounce() missing 1 required positional argument: 'self'

# class method可以被 class and instance 呼叫
jim.how_many_people('It is cool!')
Person.how_many_people('It is nice.')

# static method可以被 class and instance 呼叫
jim.guess(3)
Person.guess(123)

print(dir(person)) 
# ['_Person__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_foo', 'count', 'how_many_people', 'name', 'parent_func']
# print(person.__baz) # 這樣呼叫會報錯
# Traceback (most recent call last):
#   File "class_test.py", line 31, in <module>
#     print(person.__baz)
# AttributeError: 'Person' object has no attribute '__baz'
person._Person__baz = 'baz2'
print(person._Person__baz) # baz2 要這樣呼叫和修改才行

print(dir(jim)) 
# ['_Man__speak', '_Person__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_foo', 'child_func', 'count', 'gender', 'how_many_people', 'name', 'parent_func']
jim._Man__speak() # I am a man


'''
Testing of Changing the class attribute using the class name or the object name
Person.age = 19
jim.age = 19
print(jim.age)
print(terrence.age)
print(Person.age)
'''