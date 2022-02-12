# 想要用class decorator去裝飾function，但又想讓function保持原本呼叫方式
# -->加上 __call__() method


class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        # We can add some code
        # before function call
        self.function()
        # We can also add some code
        # after function call.

# adding class decorator to the function


@MyDecorator
def function():
    print("GeeksforGeeks")


function()  # 可直接呼叫～
# > GeeksforGeeks
# https: // www.geeksforgeeks.org/class-as-decorator-in-python/
