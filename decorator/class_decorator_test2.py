class entryExit(object):

    def __init__(self, f):
        print("entry init enter")
        self.f = f
        print("entry init exit")

    def __call__(self, *args):
        print("Entering", self.f.__name__)
        r = self.f(*args)
        print("Exited", self.f.__name__)
        return r


print('decorator using')


@entryExit
def hello(a):
    print('inside hello')
    return "hello world " + a


print('test start')
print(hello('friends'))

"""
decorator using
entry init enter  --->裝飾時竟然就先執行__init__了...
entry init exit
test start
Entering hello
inside hello
Exited hello
hello world friends
"""
