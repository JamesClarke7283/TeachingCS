"""Decorators are a way to modify the behavior of a function
without changing the function itself."""

def trace_method(func: callable):
    def wrapper(*args, **kwargs):
        print("args:\t{},\tkwargs: {}".format(args, kwargs))
        func(*args, **kwargs)
    return wrapper


@trace_method
def say_something(name: str):
    print("Whee! {}".format(name))


say_something("James")