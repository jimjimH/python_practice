class Cars:
    def __init__(self, weight):
        print('=init start=')
        self.weight = weight  # 呼叫setter
        print('=init end=')

    # getter, __weight就是property
    @property
    def weight(self):
        print('=in property=')
        return self.__weight

    # setter, 意思就是告訴類別(Class)當來源端要設定屬性(property)值時，要呼叫這個方法(Method)
    @weight.setter
    def weight(self, value):
        print('=in_setter=')
        if value <= 0:
            raise ValueError("Car weight cannot be 0 or less.")
        self.__weight = value


mazda = Cars(100)
print(dir(mazda))
print(mazda.__dict__)
print(mazda.weight)


mazda.weight = 90
print(mazda.__dict__)
print(mazda.weight)


# 汽車類別
class Cars1:
    door = 4  # Class Attribute，所有instance共用，可更改

    def __init__(self, color, seat):
        # Instance Attribute，各個instance獨立擁有
        self.color = color
        self.seat = seat
        self.weight = 140
