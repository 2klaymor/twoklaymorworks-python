from math import *
from decimal import *


def drawMultiplicationTable(a, b, x, y):

    """
    Draws a multiplication table in the terminal

    :param a: Starting number in the range of first multipliers
    :param b: Last number in the range of first multipliers
    :param x: Starting number in the range of second multipliers
    :param y: Last number in the range of first multipliers
    """

    for multiplier2 in range(x, y+1):
        print(f'\t{multiplier2}', end='')

    for multiplier1 in range(a, b+1):
        print(f'\n{multiplier1}', end='')
        for multiplier2 in range(x, y+1):
            answer = multiplier1 * multiplier2
            print(f'\t{answer}', end='')


def roundToNearestMultiple(number, multiple=5, direction='higher', threshold=0.5):

    """
        Rounds the number to the nearest higher (by default) number multiple
        by 5 (by default)

        :param number: the number that is being rounded.
        :param multiple: the multiple of the nearest number to which the number
        being rounded.
        :param direction: direction of the rounding, higher by default, can be
        specified to round to the lower number or in both directions
        depending on the specified threshold. possible values: 'higher',
        'lower', 'threshold'.
        :param threshold: threshold from which the number starts to
        round to a higher number, switching direction.
    """

    numberFraction = round(number - int(number), 2)
    fractionExponent = -Decimal('{:.2f}'.format(number)).as_tuple().exponent
    fractionInteger = int(numberFraction * 10 ** fractionExponent)

    if direction == 'threshold':
        if numberFraction > threshold:
            fractionInteger = multiple * ceil(fractionInteger / multiple)
        else:
            fractionInteger = multiple * trunc(fractionInteger / multiple)
    elif direction == 'lower':
        fractionInteger = multiple * trunc(fractionInteger / multiple)
    else:
        fractionInteger = multiple * ceil(fractionInteger / multiple)

    numberFraction = round(fractionInteger * 10 ** -fractionExponent, 2)
    number = int(number) + numberFraction

    return number


def caesarCipher(string, shift):

    lettersLowercase = 'abcdefghijklmnopqrstuvwxyz'
    lettersUppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = ' -=_+.,~!:@#$%^&*()[]{}\'\"<>:;/\\|'
    newString = ''

    for letter in string:

        if letter in lettersLowercase:
            startSymbolIndex = lettersLowercase.index(letter)
            newSymbolIndex = (startSymbolIndex + shift) % 26
            newString += lettersLowercase[newSymbolIndex]

        elif letter in lettersUppercase:
            startSymbolIndex = lettersUppercase.index(letter)
            newSymbolIndex = (startSymbolIndex + shift) % 26
            newString += lettersUppercase[newSymbolIndex]

        elif letter in symbols:
            newString += letter

    return newString


def ordinalDate(dd, mm, yyyy):

    monthDayCount = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

    if mm > 2 and yyyy % 4 == 0 or yyyy % 100 == 0 and yyyy % 400 == 0:
        return monthDayCount[mm-1] + dd + 1
    else:
        return monthDayCount[mm-1] + dd
