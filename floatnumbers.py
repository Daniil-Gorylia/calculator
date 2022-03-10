# Здесь содержится вся информация о прописных числах, и написана функция которая оказалась большой т.к я использовал
# кортежи, и поэтому мне понадобились более точные диапазоны в условиях, если бы я использовал словарь во всех числах,
# а не только числах после запятой, то количество строк можно было уменьшить вдвое


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
    float_numbers = {0.0: 'ноль десятых', 0.1 : 'одна десятая', 0.2 : 'две десятых', 0.3 : 'три десятых',
                     0.4 : 'четыре десятых', 0.5 : 'пять десятых', 0.6 : 'шесть десятых',
                     0.7 : 'семь десятых', 0.8 : 'восемь десятых', 0.9 : 'девять десятых'}
    # В строках ниже использован функционал modf(n) принадлежащий модулю math, для того чтобы отделить целые числа от
    # чисел после запятой, при этом приходится повторно округлять числа после запятой, т.к mod(f) выводит длинное
    # число после запятой, что нам в данной задаче не нужно
    a = modf(n)
    # Так как modf(n) выводит кортеж, я сделал float_number и int_number для отделения переменных и использования их
    # в последующем
    float_number = a[0]
    int_number = a[1]
    float_number2 = round(float_number, 1)
    # Данные операции служат исключительно для целых чисел, где n1, n2, n,3 n,4 выводит еденицы, десятки, сотни, и
    # тысячи соответственно, d, d1, d,2 мне понадобились для того, чтобы приводить десятки, сотни, тысячи в индексы
    n1 = int_number % 10
    n2 = int_number - n1
    n22 = n % 100
    n3 = n2 % 100
    n4 = n2 % 1000
    n44 = n % 1000
    d23 = n44 - n22
    d = int_number / 10
    d1 = int_number / 100
    d2 = int_number / 1000


    if -1 < n < 10.0:
        return number1[int(int_number)] + ' целых ' + float_numbers[float_number2]
    elif 10.0 < n < 20.0 and n1 != 0:
        return number3[int(int_number - 10)] + ' целых ' + float_numbers[float_number2]
    elif 10.0 < n < 100.0 and n1 == 0 and number2[int(d)] in number2:
        return number2[int(d)] + ' целых ' + float_numbers[float_number2]
    elif 20.0 < n < 100.0:
        return number2[int(d)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 100.0 <= n < 1000.0 and d1.is_integer() and n1 ==0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' целых ' + float_numbers[float_number2]
    elif 100 < n < 1000:
        if n3 >0 and n1 == 0:
            return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
        elif 10 < n22 < 20:
            return number4[int(d1)] + ' ' + number3[int(n22 - 10)] + ' целых ' + float_numbers[float_number2]
        elif n22 > 20:
            return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
                   + float_numbers[float_number2]
        elif n1 > 0:
            return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 1000 <= n < 10000 and d2.is_integer() and number5[int(d2)] in number5:
        return number5[int(d2)] + ' целых ' + float_numbers[float_number2]
    elif 1000 < n < 10000:
        if n1 == 0 and d23 < 100:
            return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
        elif 10 < n22 < 20 and d23 < 100:
            return number5[int(d2)] + ' ' + number3[int(n22 - 10)] + ' целых ' + float_numbers[float_number2]
        elif n22 > 20 and d23 < 100:
            return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
                   + float_numbers[float_number2]
        elif n1 > 0 and d23 < 100:
            return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
        elif n44 >= 100 and n1 == 0 and n22 ==0:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' целых ' + float_numbers[float_number2]
        elif n1 ==0 and n22 >= 10:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + \
                   ' целых ' + float_numbers[float_number2]
        elif 10 < n22 < 20:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int (n22 - 10)] + \
                   ' целых ' + float_numbers[float_number2]
        elif n22 > 20:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' \
                   + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
        elif n1 > 0:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + \
                   ' целых ' + float_numbers[float_number2]
    else:
        print('Извините, но калькулятор пока что не может вывести текстом запрашиваемый результат')
