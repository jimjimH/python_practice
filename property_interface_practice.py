import abc


class Dog(metaclass=abc.ABCMeta):

    def __init__(self):
        self.__food = 'meat'

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

    @property
    @abc.abstractmethod
    def skill(self):    # 希望subclass都有這個skill property
        pass

    @abc.abstractmethod
    def eat_food(self):
        pass

    @classmethod
    @abc.abstractmethod
    def pee(cls):          
        pass


class Shiba(Dog):
    def __init__(self, skill='being cute'):
        super().__init__()
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    def eat_food(self):
        print(f"I'm eating {self.food}") # 因為已設定了property，所以這裡是使用getter取得__food的

    @classmethod
    def pee(cls):
        print(f"{cls.__name__} is peeing........")


Bibo = Shiba('playing ball')

print(Bibo.food)  # meat
Bibo.eat_food()  # I'm eating meat

# change the property
Bibo.food = 'fish'
print(Bibo.food)  # fish
Bibo.eat_food()  # I'm eating fish

# test for abstract property method
print(f'I am good at {Bibo.skill}.')  # I am good at playing ball

Shiba.pee() # Shiba is peeing........
