#global and local variable
x = [1,2,3]
def test():
    global x # 直接指定x就是global
    x = x + [10] # 所以可以assignment新值給x
    print(x)
    
if __name__ == "__main__":
    test() # [1, 2, 3, 10]
    print(x) # [1, 2, 3, 10]


#練習local variable scope in a function
squares_1 = []
for x in range(5):
    squares_1.append(lambda: x**2)
print(squares_1[1]()) #16  因為lambda內使用的x是外面globla的值，當程式執行至此行時，global x 已經是4了
print(squares_1[2]()) #16

squares_2 = []
for x in range(5):
    squares_2.append(lambda n=x : n**2) #這邊多建立一個local variable n，來儲存每個loop裡面global x的值
print(squares_2[1]()) #1
print(squares_2[2]()) #4

#closure裡面，因為 captured variable 在 Python 中既不是 local 也不是 global 所以只能用 nonlocal 去 access
def dog():
    height = 40
    def grow_up():
        nonlocal height
        height = height + 1
        print("Thanks for making me growing up. I'm now {} meters !!!!".format(height))
    print(height)
    return grow_up 

if __name__ == "__main__":
    dog_grow_up = dog()
    dog_grow_up()
    #40 --> 外面function的height不受影響
    #Thanks for making me growing up. I'm now 41 meters !!!! -->裡面的height變成41

'''
# 當引數是immutable時，會是 pass by value
# 當引數是mutable時，會是 pass the object
def updateNumber(n):
    print(id(n))
    n = n + 10
    print(n)
    print(id(n))

b = 5
print(id(b))         # 4461538336
updateNumber(b)      
# 4461538336
# 15
# 4461538656  變了，另外新建一個local n，並把n+10的結果15assign給它
print(b)             # 5 不變
'''