from math import *
def float_number_to_words(n):
    number1 = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
    number2 = (None, 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
               'девяносто')
    number3 = (None, 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
               'семнадцать', 'восемнадцать', 'девятнадцать')
    number4 = (None, 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
               'девятьсот')
    number5 = (None, 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч',
               'семь тысяч', 'восемь тысяч', 'девять тысяч')
    float_numbers = { 0.1 : 'одна десятая', 0.2 : 'две десятых', 0.3 : 'три десятых', 0.4 : 'четыре десятых', 0.5 :
                      'пять десятых', 0.6 : 'шесть десятых', 0.7 : 'семь десятых', 0.8 : 'восемь десятых', 0.9 :
                      'девять десятых'}
    a = modf(n)
    float_number = a[0]
    int_number = a[1]
    float_number2 = round(float_number, 1)

    n1 = int_number % 10
    n2 = int_number - n1
    n3 = n2 % 100
    n4 = n2 % 1000
    d = int_number / 10
    d1 = int_number / 100
    d2 = int_number / 1000


    if 0.0 < n < 10.0:
        return number1[int(int_number)] + ' целых ' + float_numbers[float_number2]
    elif 10.0 < n < 20.0 and n1 != 0:
        return number3[int(int_number - 10)] + ' целых ' + float_numbers[float_number2]
    elif 10.0 < n < 100.0 and n1 == 0 and number2[int(d)] in number2:
        return number2[int(d)] + ' целых ' + float_numbers[float_number2]
    elif 20.0 < n < 100.0:
        return number2[int(d)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 100.0 <= n < 1000.0 and number2[int(d1)] not in number2 and n1 ==0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' целых ' + float_numbers[float_number2]
    elif 100.0 < n < 110.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 110.0 < n < 200.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 110] + ' целых ' + float_numbers[float_number2]
    elif 110.0 <= n < 200.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 120.0 < n < 200.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 200.0 < n < 210.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 210.0 < n < 300.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 210] + ' целых ' + float_numbers[float_number2]
    elif 210.0 <= n < 300.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 220.0 < n < 300.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 300.0 < n < 310.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 310.0 < n < 400.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 310] + ' целых ' + float_numbers[float_number2]
    elif 310.0 <= n < 400.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 320.0 < n < 400.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 400.0 < n < 410.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 410.0 < n < 500.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 410] + ' целых ' + float_numbers[float_number2]
    elif 410.0 <= n < 500.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 420.0 < n < 500.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 500.0 < n < 510.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 510.0 < n < 600.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 510] + ' целых ' + float_numbers[float_number2]
    elif 510.0 <= n < 600.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 520.0 < n < 600.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 600.0 < n < 610.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 610.0 < n < 700.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 710] + ' целых ' + float_numbers[float_number2]
    elif 610.0 <= n < 700.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 620.0 < n < 700.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 700.0 < n < 710.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 710.0 < n < 800.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 710] + ' целых ' + float_numbers[float_number2]
    elif 710.0 <= n < 800.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 720.0 < n < 800.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 800.0 < n < 810.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 810.0 < n < 900.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 810] + ' целых ' + float_numbers[float_number2]
    elif 810.0 <= n < 900.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 820.0 < n < 900.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 900.0 < n < 910.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 910.0 < n < 1000.0 and n3 < 20:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 910] + ' целых ' + float_numbers[float_number2]
    elif 910.0 <= n < 1000.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 920.0 < n < 1000.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]

