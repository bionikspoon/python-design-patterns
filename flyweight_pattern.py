#!/usr/bin/env python
# coding=utf-8
from weakref import WeakValueDictionary


class Link(object):
    def __init__(self, ref, text, image_path=None):
        self.ref = ref
        self.text = text
        if image_path:
            self.image = BrowserImage(image_path)
        else:
            self.image = None

    def __str__(self):
        if not self.image:
            return '<{self.__class__.__name__} ({self.text})>'.format(self=self)
        else:
            return '<{self.__class__.__name__} ({self.text}, {self.image})>'.format(self=self)


class BrowserImage(object):
    _resources = WeakValueDictionary()

    def __new__(cls, location):
        image = BrowserImage._resources.get(location, None)
        if not image:
            image = object.__new__(cls)
            BrowserImage._resources[location] = image
            image.__init(location)

    def __init(self, location):
        self.location = location

    def __str__(self):
        return '<{self.__class__.__name__} ({self.location})'.format(self=self)


if __name__ == '__main__':
    icon = Link(  # :off
        'www.python.org',
        'python logo',
        'https://www.python.org/static/img/python-logo.png'
    )  # :on
    footer_icon = Link(  # :off
        'www.python.org/#header',
        'python header logo',
        'https://www.python.org/static/img/python-logo.png'
    )  # :on
    twitter_top_header_icon = Link(  # :off
        'www.twitter.com/python',
        'python twitter link',
        'https://www.python.org/static/img/python-logo.png'
    )  # :on

    print(icon)
    print(footer_icon)
    print(twitter_top_header_icon)
