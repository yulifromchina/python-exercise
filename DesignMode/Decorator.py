# -*- coding:utf-8 -*-
#装饰器模式

from functools import wraps

HOST_DOCKER = 0

def docker_host_required(f):
    """
    装饰器
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(args[0])
        print(type(args[0]))
        if args[0].type != HOST_DOCKER:
            raise Exception('Not docker yet.')
        else:
            return f(*args, **kwargs)
    return wrapper


class Host(object):
    """
    host类
    """

    def __init__(self, type):
        self.type = type

    @docker_host_required
    def create_container(self):
        print('create container')


if __name__ == '__main__':
    host = Host(HOST_DOCKER)
    host.create_container()
    print(" ")
    host=Host(1)
    host.create_container()

