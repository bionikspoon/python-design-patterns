#!/usr/bin/env python
# coding=utf-8
from abc import ABCMeta, abstractmethod
from functools import partial

from six import with_metaclass


class Animal(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def sound(self):
        pass


class AnimalFactory(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def create_animal(self, name):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('bark bark')


class DogFactory(AnimalFactory):
    def create_animal(self, name):
        return Dog(name)


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('meow meow')


class CatFactory(AnimalFactory):
    def create_animal(self, name):
        return Cat(name)


class Animals(object):
    def __init__(self, factory):
        self.factory = factory

    def create_animal(self, name):
        return self.factory.create_animal(name)


if __name__ == '__main__':
    input_map = {  # :off
        'cat': partial(Animals, CatFactory()),
        'dog': partial(Animals, DogFactory()),
    }  # :on
    a_type = input('What animal [cat|dog] ? ').lower()
    animal = input_map[a_type]()
    a = animal.create_animal('shelli')
    a.sound()
