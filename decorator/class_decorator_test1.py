# Q: 為什麼function被class decorator修飾後，會像是被實例化一樣觸發__init__，就像物件一樣擁有class method and attribute?

# class Decorator，將function封裝到class
class Dog:
    def __init__(self, func):  # 注意：被裝飾的function會以參數func傳入
        self.age = 10
        self.talent = func

    def bark(self):
        print("Bark !!!")


# 使用class decorator 會實例化一個Dog instance
# 這是一個非常重要、靈活而優雅的技巧，將 function dog_can_pee 「封裝」到 class Dog 的一種寫法。
@Dog
def dog_can_pee():
    print("I can pee very hard......")


@Dog
def dog_can_jump():
    print("I can jump uselessly QQQ")


@Dog
def dog_can_poo():
    print("I can poo like a super pooping machine!")


if __name__ == "__main__":

    dog_1 = dog_can_pee
    print(dog_1.age)
    # > 10
    print(type(dog_1))
    # > <class '__main__.Dog'>
    dog_1.bark()
    # > Bark !!!
    dog_1.talent()
    # > I can pee very hard......

    dog_2 = dog_can_jump
    dog_2.talent()
    # > I can jump uselessly QQQ

    dog_3 = dog_can_poo
    dog_3.talent()
    # > I can poo like a super pooping machine!

    # Q: 如果不小心傳入引數給實例，talent()會壞掉，可是self.talent卻有值了lol...怪異
    # A: 一點都不怪，只是123被當成parameter 'func'而已
    dog_4 = Dog(123)
    print(type(dog_4))  # > <class '__main__.Dog'>
    print(dog_4.talent)  # > 123
    print(dog_4.talent())  # TypeError: 'int' object is not callable
