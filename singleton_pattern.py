#!/usr/bin/env python
# coding=utf-8

from six import with_metaclass


class Singleton(type):
    _registry = {}

    def __call__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        if cls not in Singleton._registry:
            Singleton._registry[cls] = type.__call__(cls, *args, **kwargs)
        return Singleton._registry[cls]


class Me(with_metaclass(Singleton, object)):
    def __init__(self, data):
        print('init_ran', self.__class__.__name__, data)
        self.data = data


if __name__ == '__main__':
    m = Me(2)
    n = Me(3)
    print(m.data, n.data)

    n.data = 4
    print(m.data, n.data)
