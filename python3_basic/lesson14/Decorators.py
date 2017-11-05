#!/usr/bin/env python3

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Call")
        result = func(*args, **kwargs)
        print("After Call")
        return result
    return wrapper


@my_decorator
def add(a,b):
    print(a+b)

add(1,2)
