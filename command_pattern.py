#!/usr/bin/env python
# coding=utf-8

import threading
import time


class Chef(threading.Thread):
    def __init__(self, name):
        self.q = []
        self.done_q = []
        self.do_orders = True
        super(Chef, self).__init__()
        self.name = name
        self.start()

    def make_order(self, order):
        print('{self.name} Preparing menu :'.format(self=self))

        for item in order.items:
            print('cooking', item)
            time.sleep(1)
        order.completed = True
        self.done_q.append(order)

    def run(self):
        while self.do_orders:
            if self.q:
                order = self.q.pop(0)
                self.make_order(order)
                time.sleep(1)

    def work_on_order(self, order):
        self.q.append(order)

    def cancel(self, order):
        if order in self.q:
            if order.completed is True:
                print('cannot cancel, order completed')
                return

            index = self.q.index(order)
            del self.q[index]
            print('order cancelled {0}'.format(order))
            return

        if order in self.done_q:
            print('cannot cancel, order completed')
            return

        print('order not found')


class Check(object):
    def execute(self):
        raise NotImplementedError

    def cancel(self):
        raise NotADirectoryError


class MenuOrder(Check):
    def __init__(self, *items):
        self.items = items
        self.completed = False

    # noinspection PyMethodOverriding,PyAttributeOutsideInit
    def execute(self, chef):
        self.chef = chef
        chef.work_on_order(self)

    def cancel(self):
        if self.chef.cancel(self):
            print('order cancelled')

    def __str__(self):
        return ''.join(self.items)


if __name__ == '__main__':
    c = Chef('Hannibal')
    order1 = MenuOrder('John Smith', 'Jane Smith', 'Sara Smith')
    order2 = MenuOrder('Romeo', 'Juliet')
    order3 = MenuOrder('Will Graham')

    order1.execute(c)
    order2.execute(c)
    order3.execute(c)

    time.sleep(1)
    order3.cancel()
    time.sleep(9)
    c.do_orders = False
    c.join()
