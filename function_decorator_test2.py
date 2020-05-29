import time

def print_func_name(time): #帶入參數
    def decorator(func):
        def wrap(*args, **kwargs):
            print("Now use function '{}'".format(func.__name__))
            print("Now Unix time is {}.".format(int(time)))
            func(*args, **kwargs)
        return wrap
    return decorator


@print_func_name(time=(time.time())) #可以用positional or keyword arguments
def dog_bark(*args, **kwargs):
    print("Bark !!!")
    print(args)
    print(kwargs)


if __name__ == "__main__":
    dog_bark(10, owner='jim')