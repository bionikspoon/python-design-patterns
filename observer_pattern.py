#!/usr/bin/env python
# coding=utf-8
from weakref import WeakSet


class Subject(object):
    def __init__(self, name):
        self.name = name
        self._observers = WeakSet()

    def register_observer(self, observer):
        self._observers.add(observer)
        print('observer {0} now listening on {1}'.format(observer.name, self.name))

    def notify_observers(self, msg):
        print('{0} notifying observers about {1}'.format(self.__class__.__name__, msg))
        for observer in self._observers:
            observer.notify(self, msg)


class Observer(object):
    def __init__(self, name):
        self.name = name

    def start_observing(self, subject):
        subject.register_observer(self)

    def notify(self, subject, msg):
        print('{0} got message from {1} that {2}'.format(self.name, subject.name, msg))


if __name__ == '__main__':
    class_homework = Subject('class homework')
    student1 = Observer('student 1')
    student2 = Observer('student 2')

    student1.start_observing(class_homework)
    student2.start_observing(class_homework)

    class_homework.notify_observers('result is out')

    del student2

    class_homework.notify_observers('20/20 passed this semester')
