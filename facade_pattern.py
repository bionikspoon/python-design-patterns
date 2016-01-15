#!/usr/bin/env python
# coding=utf-8

class Leg(object):
    def __init__(self, name):
        self.name = name

    def forward(self):
        print('{0},'.format(self.name), end=' ')


class WalkingDrone(object):
    def __init__(self, name):
        self.name = name
        self.front_right_leg = Leg('Front Right Leg')
        self.front_left_leg = Leg('Front Right Leg')
        self.back_right_leg = Leg('Back Right Leg')
        self.back_left_leg = Leg('Back Right Leg')

    def walk(self):
        print('\nmoving', end=' ')
        self.front_right_leg.forward()
        self.back_left_leg.forward()
        print('\nmoving', end=' ')
        self.front_left_leg.forward()
        self.back_right_leg.forward()

    def run(self):
        print('\nmoving', end=' ')
        self.front_right_leg.forward()
        self.front_left_leg.forward()
        print('\nmoving', end=' ')
        self.back_left_leg.forward()
        self.back_right_leg.forward()


if __name__ == '__main__':
    wd = WalkingDrone('RoboDrone')
    print('\nwalking')
    wd.walk()
    print('\n\nrunning')
    wd.run()
