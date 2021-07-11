# -*- coding: utf-8 -*-
"""
Python尋找property的順序：
1. 先尋找instance __dict__
2. 如果沒有則到產生該instance的class __dict__裡面尋找
3. 如果沒有則到試著呼叫__getattr__()來傳回
4. 如果沒有定義 __getattr__()方法，則會引發AttributeError
https://openhome.cc/Gossip/Python/PropertyNameSpace.html

如果你在定義類別時希望某個函式，完全不要作為實例的綁定方法，也就是不要將第一個參數綁定為所建立的實例，則可以使用@staticmethod加以修飾
雖然你可以透過實例來呼叫@staticmethod所修飾的靜態方法，建議透過類別名稱來呼叫。類似的，建議透過實例來呼叫實例的綁定方法
# https://openhome.cc/Gossip/Python/StaticClassMethod.html
"""


class Some:
    const = 'const'

    def __init__(self, x):
        self.__x = x

    def instance_service(self, y):
        print('do service...', self.__x + y)

    # 如果你在定義類別時希望某個函式，完全不要作為實例的綁定方法，也就是不要將第一個參數綁定為所建立的實例，則可以使用@staticmethod加以修飾
    # 雖然你可以透過實例來呼叫@staticmethod所修飾的靜態方法，建議透過類別名稱來呼叫。類似的，建議透過實例來呼叫實例的綁定方法
    # https://openhome.cc/Gossip/Python/StaticClassMethod.html
    @staticmethod
    def static_service(x, y):
        print('do service...', x + y)

    @classmethod
    def class_service(clz, y):
        print('do service...', clz, y)

    def service(x):
        print('do service...', x)


class Other:
    pass


s = Some(10)
print(s.__dict__)
print(s._Some__x)  # name mangling

print(s.const)  # s沒有const, 所以嘗試尋找Some.const去執行, id(const)一樣不會變

# <bound method Some.instance_service of <__main__.Some object at 0x10a6d5130>>
print(s.instance_service)
s.instance_service(20)
test_service1 = s.instance_service
test_service1(20)
test_service2 = Some.instance_service
test_service2(s, 20)  # 把instance傳進去

# <function Some.static_service at 0x10a76b670>
print(s.static_service)  # id 不變
print(Some.static_service)  # id 不變
# s沒有static_service()的綁定方法（因為static_service被@staticmethod修飾），所以嘗試尋找Some.static_service()去執行。id(static_service)一樣不會變
s.static_service(1, 2)

# <bound method Some.class_service of <class '__main__.Some'>>
print(s.class_service)
s.class_service(20)

s.var = 10  # 增加property
print(s.__dict__)  # {'_Some__x': 10, 'var': 10}
del s.var  # 減少property
print(s.__dict__)  # {'_Some__x': 10}


print()

print(Some.__dict__)
print(Some.const)
print(Some.__dict__['const'])
Some.class_service(25)
Some.static_service(5, 10)

# 特例，平常不會這樣用
other_s = Other()
other_s._Some__x = 99
Some.instance_service(other_s, 1)
