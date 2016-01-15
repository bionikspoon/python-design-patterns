#!/usr/bin/env python
# coding=utf-8

import six


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit
class AlooDish(object):
    def get_ingredients(self):
        self.ingredients = {}

    def prepare_vegetables(self):
        for item in six.iteritems(self.ingredients):
            print('Take {item[0]} {item[1]} and cut into smaller pieces'.format(item=item))
            print('cut all vegetables in small pieces')

    def fry(self):
        print('fry for 5 minutes')

    def serve(self):
        print('Dish is ready to be served')

    def cook(self):
        self.get_ingredients()
        self.prepare_vegetables()
        self.fry()
        self.serve()


# noinspection PyAttributeOutsideInit
class AlooMatar(AlooDish):
    def get_ingredients(self):
        self.ingredients = {'aloo': '1 Kg', 'matar': '1/2 kg'}

    def fry(self):
        print('wait 10 min')


# noinspection PyAttributeOutsideInit
class AlooPyaz(AlooDish):
    def get_ingredients(self):
        self.ingredients = {'aloo': '1 Kg', 'pyaz': '1/2 kg'}


if __name__ == '__main__':
    aloo_matar = AlooMatar()
    aloo_pyaz = AlooPyaz()

    print('  Aloo Matar Cook  '.center(80, '*'))
    aloo_matar.cook()
    print('  Aloo Pyaz Cook  '.center(80, '*'))
    aloo_pyaz.cook()
