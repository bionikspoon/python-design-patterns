#!/usr/bin/env python
# coding=utf-8

TAX_PERCENT = .12


class TaxIN(object):
    def __init__(self):
        self.country_code = 'IN'

    def __call__(self, bill_amount):
        return bill_amount * TAX_PERCENT


class TaxUS(object):
    def __init__(self):
        self.country_code = 'US'

    def __call__(self, bill_amount):
        if bill_amount < 500:
            return bill_amount * (TAX_PERCENT // 2)
        else:
            return bill_amount * TAX_PERCENT


class TaxCalculator(object):
    def __init__(self):
        self._implements = [TaxIN(), TaxUS()]

    def __call__(self, country, bill_amount):
        for implement in self._implements:
            if implement.country_code == country:
                return implement(bill_amount)
        else:
            return


def tax_simple(bill_amount):
    return bill_amount * TAX_PERCENT


def tax_actual(bill_amount):
    if bill_amount < 500:
        return bill_amount * (TAX_PERCENT // 2)
    else:
        return bill_amount * TAX_PERCENT


if __name__ == '__main__':
    # Global scope functions
    # ========================================================================
    print('Global scope functions')
    tax_calc = tax_simple
    print(tax_calc(400), tax_calc(700))

    tax_calc = tax_actual
    print(tax_calc(400), tax_calc(700))

    # Class scope
    # ========================================================================
    print('Class scope')
    tax_calc = TaxCalculator()
    print(tax_calc('IN', 400), tax_calc('IN', 700))
    print(tax_calc('US', 400), tax_calc('US', 700))
