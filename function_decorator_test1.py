def decorator(func):
    def new_func(*arg, **kwarg): #接收引數
        print('- step1')
        print('Running function: ', func.__name__)
        print('positional args: ', arg)
        print('keyword args: ', kwarg)
        result = func(*arg, **kwarg) #呼叫傳進來的那個func #接收引數
        print (result)
        return result
    return new_func #先不呼叫function

def add_100(func):
    def new_func_add_100(*arg, **kwarg): #接收引數
        print('- step2: ---call_add_100---')
        result = func(*arg, **kwarg) # 呼叫傳進來的那個func #接收引數
        return result + 100
    return new_func_add_100


'''
裝飾順序：
1. 由內而外逐層裝飾，邏輯上則會先合併「最靠近」的 decorator、吐出新的 function 再由上面一個的 decorator 吃進去！
2. 執行是從外面開始執行進來，先執行最後一個 decorator 吐出來的 function，再執行前一個，依此類推
3. argument不會變、一直用下去
'''
@decorator
@add_100
def multi_ints1(a, b):
    print('- step3: ---call_multi_ints---')
    return a * b

print(multi_ints1(2, 5))
'''
- step1
Running function:  new_func_add_100
positional args:  (2, 5)
keyword args:  {}
- step2: ---call_add_100---
- step3: ---call_multi_ints---
110
110
'''

@add_100
@decorator
def multi_ints2(a, b):
    print('- step3: ---call_multi_ints---')
    return a * b    

print(multi_ints2(2, 5))
'''
- step2: ---call_add_100---
- step1
Running function:  multi_ints2
positional args:  (2, 5)
keyword args:  {}
- step3: ---call_multi_ints---
10
110
'''

def add_ints1(a, b):
    return a + b

cooler_add_ints = decorator(add_ints1) #manual decorator assignment
cooler_add_ints(3, 5)


@decorator #using decorator
def add_ints2(a,b):
    return a+b

add_ints2(3, 5)




