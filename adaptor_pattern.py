#!/usr/bin/env python
# coding=utf-8


def running_competition(*list_of_animals):
    if not list_of_animals:
        print('No one is running')
        return

    fastest_animal = list_of_animals[0]
    max_speed = fastest_animal.running_speed()

    for animal in list_of_animals[1:]:
        run_speed = animal.running_speed()
        if run_speed > max_speed:
            fastest_animal, max_speed = animal, run_speed

    print('winner is {0} with {1} Km/h'.format(fastest_animal.name, max_speed))


class Cat(object):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def running_speed(self):
        if self.legs > 4:
            return 20
        else:
            return 40


if __name__ == '__main__':
    running_competition(Cat('cat_a', 4), Cat('cat_b', 3))


class Fish(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim_speed(self):
        if self.age < 2:
            return 40
        else:
            return 60


class RunningFish(object):
    def __init__(self, fish):
        self.legs = 4
        self.fish = fish

    def running_speed(self):
        return self.fish.swim_speed()

    def __getattr__(self, item):
        return getattr(self.fish, item)


if __name__ == '__main__':
    running_competition(  # :off
        Cat('cat_a', 4),
        Cat('cat_b', 3),
        RunningFish(Fish('nemo', 3)),
        RunningFish(Fish('dollar', 1)),
    )  # :on
