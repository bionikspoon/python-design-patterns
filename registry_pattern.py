#!/usr/bin/env python
# coding=utf-8


class ConverterError(Exception):
    pass


class Converter(object):
    def __init__(self):
        self.__registry = {}

    def to_object(self, data_dict):
        d_type = data_dict.get('type', None)

        if d_type is None:
            raise ConverterError('cannot create object, type not defined')

        if d_type not in self.__registry:
            raise ConverterError('cannot convert, type not registered')

        _converter = self.__registry[d_type]
        return _converter.to_python(data_dict['data'])

    def register(self, _converter):
        i_converter = _converter()
        self.__registry[i_converter.d_type] = i_converter


converter = Converter()


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<{self.__class__.__name__} ({self.name}, {self.age})>'.format(self=self)


@converter.register
class PersonConverter(object):
    def __init__(self):
        self.d_type = 'person'

    @staticmethod
    def to_python(data):
        p = Person(data['name'], data['age'])
        return p


if __name__ == '__main__':
    print(converter.to_object({  # :off
        'type': 'person',
        'data': {
            'name': 'Joe Sixpack',
            'age': 45
        }
    }))  # :on
