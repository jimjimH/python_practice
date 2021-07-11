# https://dev.to/apcelent/python-decorator-tutorial-with-example-529f
# https://blog.apcelent.com/python-decorator-tutorial-with-example.html
from functools import wraps
import time


print("===Function Decorator===")


def timetest(input_func):
    def timed(*args, **kwargs):
        start_time = time.time()
        end_time = time.time()
        print(
            "Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
                input_func.__name__,
                args,
                kwargs,
                end_time - start_time
            )
        )
        result = input_func(*args, **kwargs)
        return result
    return timed


@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print("inside foobar")
    print(args, kwargs)


foobar(["hello, world"], foo=2, bar=5)


print("===Method Decorator===")


def method_decorator(method):
    def inner(city_instance):
        if city_instance.name == "SFO":
            print("Its a cool place to live in.")
        else:
            method(city_instance)
    return inner


class City(object):
    def __init__(self, name):
        self.name = name

    @method_decorator
    def print_test(self):
        print(self.name)


p1 = City("SFO1")
p1.print_test()


print("===Class Decorator===")


class decoclass(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print('class decoration initialised')  # before f actions
        self.f(*args, **kwargs)
        print('class decoration terminated')  # after f actions


@decoclass
def klass():
    print('klass~~~')


klass()


print("===Function Decorator with Arguments===")


def decorator(arg1, arg2):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(vars())
            print(f"Arguments passed to decorator: {arg1} and {arg2}")
            function(*args, **kwargs)
        return wrapper
    return inner_function


@decorator("a", "b")
def print_args(*args):
    for arg in args:
        print(arg)


print(print_args(1, 2, 3))


print("===Class Decorator with Arguments===")


class ClassDecorator(object):
    def __init__(self, arg1, arg2):
        print("Arguements passed to decorator %s and %s" % (arg1, arg2))
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, foo, *args, **kwargs):
        def inner_func(*args, **kwargs):
            print("Args passed inside decorated function .%s and %s" %
                  (self.arg1, self.arg2))
            return foo(*args, **kwargs)
        return inner_func


@ClassDecorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3)


print('===Order of Decorator===')


def makebold(f):
    return lambda: "<b>" + f() + "</b>"


def makeitalic(f):
    return lambda: "<i>" + f() + "</i>"


@makebold
@makeitalic
def say():
    return "Hello"


print(say())


'''
https://stackoverflow.com/questions/3888158/making-decorators-with-optional-arguments
參數可傳可不傳

from functools import wraps

def foo_register(method_name=None):
    """Does stuff."""
    def decorator(method):
        if method_name is None:
            method.gw_method = method.__name__
        else:
            method.gw_method = method_name
        @wraps(method)
        def wrapper(*args, **kwargs):
            method(*args, **kwargs)
        return wrapper
    return decorator
Example: The following decorates my_function with foo_register instead of ever making it to decorator.

@foo_register
def my_function():
    print('hi...')
Example: The following works as expected.

@foo_register('say_hi')
def my_function():
    print('hi...')
'''
