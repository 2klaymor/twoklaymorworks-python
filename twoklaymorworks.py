from math import *
from decimal import *


def drawmultiplicationtable(a, b, x, y):

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


def roundtonearestmultiple(number, multiple=5, direction='higher', threshold=0.5):

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

    number_fraction = round(number - int(number), 2)
    fraction_exponent = -Decimal('{:.2f}'.format(number)).as_tuple().exponent
    fraction_integer = int(number_fraction * 10 ** fraction_exponent)

    if direction == 'threshold':
        if number_fraction > threshold:
            fraction_integer = multiple * ceil(fraction_integer / multiple)
        else:
            fraction_integer = multiple * trunc(fraction_integer / multiple)
    elif direction == 'lower':
        fraction_integer = multiple * trunc(fraction_integer / multiple)
    else:
        fraction_integer = multiple * ceil(fraction_integer / multiple)

    number_fraction = round(fraction_integer * 10 ** -fraction_exponent, 2)
    number = int(number) + number_fraction

    return number


def caesar_code(text, shift):

    letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = ' -=_+.,~!:@#$%^&*()[]{}\'\"<>:;'
    numbers = '0123456789'
    length = len(letters_lowercase)
    error_count = 0
    shift_isnumber = 0
    shift_counter = 0
    minus_catched = False
    new_text = ''

    if len(text) > 0:
        for letter in text:
            if letter in letters_lowercase:
                start_letter_index = letters_lowercase.index(letter)
                new_letter_index = (start_letter_index + shift) % length
                new_text += letters_lowercase[new_letter_index]

            elif letter in letters_uppercase:
                start_letter_index = letters_uppercase.index(letter)
                new_letter_index = (start_letter_index + shift) % length
                new_text += letters_uppercase[new_letter_index]

            elif letter in symbols:
                new_text += letter

            else:
                unsupported_symbol = letter
                error_count += 1
    else:
        new_text = 'Error: empty string.'

    if 0 < error_count <= 1:
        new_text = f'\nError: {unsupported_symbol} - symbol is not supported.'
    elif error_count > 1:
        new_text ='\nError: Unsupported symbols present in the string.'

    return new_text
