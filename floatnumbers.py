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
    float_numbers = { 0.1 : 'одна десятая', 0.2 : 'две десятых', 0.3 : 'три десятых', 0.4 : 'четыре десятых', 0.5 :
                      'пять десятых', 0.6 : 'шесть десятых', 0.7 : 'семь десятых', 0.8 : 'восемь десятых', 0.9 :
                      'девять десятых'}
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
    elif 100.0 <= n < 1000.0 and d1.is_integer() and n1 ==0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' целых ' + float_numbers[float_number2]
    elif 100.0 < n < 110.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 110.0 < n < 200.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 110] + ' целых ' + float_numbers[float_number2]
    elif 110.0 <= n < 200.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 120.0 < n < 200.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 200.0 < n < 210.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 210.0 < n < 300.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 210] + ' целых ' + float_numbers[float_number2]
    elif 210.0 <= n < 300.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 220.0 < n < 300.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 300.0 < n < 310.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 310.0 < n < 400.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 310] + ' целых ' + float_numbers[float_number2]
    elif 310.0 <= n < 400.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 320.0 < n < 400.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 400.0 < n < 410.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 410.0 < n < 500.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 410] + ' целых ' + float_numbers[float_number2]
    elif 410.0 <= n < 500.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 420.0 < n < 500.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 500.0 < n < 510.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 510.0 < n < 600.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 510] + ' целых ' + float_numbers[float_number2]
    elif 510.0 <= n < 600.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 520.0 < n < 600.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 600.0 < n < 610.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 610.0 < n < 700.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 710] + ' целых ' + float_numbers[float_number2]
    elif 610.0 <= n < 700.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 620.0 < n < 700.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 700.0 < n < 710.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 710.0 < n < 800.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 710] + ' целых ' + float_numbers[float_number2]
    elif 710.0 <= n < 800.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 720.0 < n < 800.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 800.0 < n < 810.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 810.0 < n < 900.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 810] + ' целых ' + float_numbers[float_number2]
    elif 810.0 <= n < 900.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 820.0 < n < 900.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 900.0 < n < 910.0:
        return number4[int(d1)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 910.0 < n < 1000.0 and n3 < 20 and n1 != 0:
        return number4[int(d1)] + ' ' + number3[int(int_number) - 910] + ' целых ' + float_numbers[float_number2]
    elif 910.0 <= n < 1000.0 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 920.0 < n < 1000.0:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' \
               + float_numbers[float_number2]
    elif 1000.0 <= n < 10000 and d2.is_integer() and number5[int(d2)] in number5:
        return number5[int(d2)] + ' целых ' + float_numbers[float_number2]
    elif 1000.0 < n < 1010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 1010.0 < n < 1020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 1010] + ' целых ' + float_numbers[float_number2]
    elif 1010.0 <= n < 1100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 1020.0 < n < 1100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1100.0 < n < 1110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1110.0 < n < 1120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1110 <= n < 1200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1120 < n < 1200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1200.0 < n < 1210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1210.0 < n < 1220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1210 <= n < 1300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1220 < n < 1300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1300.0 < n < 1310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1310.0 < n < 1320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1310 <= n < 1400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1320 < n < 1400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1400.0 < n < 1410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1410.0 < n < 1420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1410 <= n < 1500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1420 < n < 1500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1500.0 < n < 1510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1510.0 < n < 1520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1510 <= n < 1600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1520 < n < 1600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1600.0 < n < 1610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1610.0 < n < 1620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1610 <= n < 1700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1620 < n < 1700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1700.0 < n < 1710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1710.0 < n < 1720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1710 <= n < 1800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1720 < n < 1800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1800.0 < n < 1810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1810.0 < n < 1820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1810 <= n < 1900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1820 < n < 1900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 1900.0 < n < 1910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1910.0 < n < 1920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 1910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1910 <= n < 2000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 1920 < n < 2000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2000.0 < n < 2010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 2010.0 < n < 2020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 2010] + ' целых ' + float_numbers[float_number2]
    elif 2010.0 <= n < 2100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 2020.0 < n < 2100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2100.0 < n < 2110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2110.0 < n < 2120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2110 <= n < 2200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2120 < n < 2200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2200.0 < n < 2210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2210.0 < n < 2220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2210 <= n < 2300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2220 < n < 2300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2300.0 < n < 2310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2310.0 < n < 2320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2310 <= n < 2400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2320 < n < 2400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2400.0 < n < 2410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2410.0 < n < 2420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2410 <= n < 2500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2420 < n < 2500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2500.0 < n < 2510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2510.0 < n < 2520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2510 <= n < 2600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2520 < n < 2600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2600.0 < n < 2610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2610.0 < n < 2620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2610 <= n < 2700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2620 < n < 2700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2700.0 < n < 2710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2710.0 < n < 2720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2710 <= n < 2800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2720 < n < 2800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2800.0 < n < 2810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2810.0 < n < 2820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2810 <= n < 2900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2820 < n < 2900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 2900.0 < n < 2910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2910.0 < n < 2920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 2910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2910 <= n < 3000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 2920 < n < 3000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3000.0 < n < 3010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 3010.0 < n < 3020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 3010] + ' целых ' + float_numbers[float_number2]
    elif 3010.0 <= n < 3100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 3020.0 < n < 3100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3100.0 < n < 3110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3110.0 < n < 3120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3110 <= n < 3200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3120 < n < 3200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3200.0 < n < 3210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3210.0 < n < 3220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3210 <= n < 3300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3220 < n < 3300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3300.0 < n < 3310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3310.0 < n < 3320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3310 <= n < 3400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3320 < n < 3400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3400.0 < n < 3410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3410.0 < n < 3420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3410 <= n < 3500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3420 < n < 3500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3500.0 < n < 3510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3510.0 < n < 3520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3510 <= n < 3600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3520 < n < 3600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3600.0 < n < 3610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3610.0 < n < 3620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3610 <= n < 3700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3620 < n < 3700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3700.0 < n < 3710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3710.0 < n < 3720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3710 <= n < 3800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3720 < n < 3800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3800.0 < n < 3810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3810.0 < n < 3820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3810 <= n < 3900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3820 < n < 3900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 3900.0 < n < 3910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3910.0 < n < 3920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 3910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3910 <= n < 4000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 3920 < n < 4000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4000.0 < n < 4010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 4010.0 < n < 4020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 4010] + ' целых ' + float_numbers[float_number2]
    elif 4010.0 <= n < 4100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 4020.0 < n < 4100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4100.0 < n < 4110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4110.0 < n < 4120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4110 <= n < 4200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4120 < n < 4200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4200.0 < n < 4210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4210.0 < n < 4220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4210 <= n < 4300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4220 < n < 4300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4300.0 < n < 4310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4310.0 < n < 4320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4310 <= n < 4400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4320 < n < 4400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4400.0 < n < 4410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4410.0 < n < 4420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4410 <= n < 4500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4420 < n < 4500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4500.0 < n < 4510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4510.0 < n < 4520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4510 <= n < 4600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4520 < n < 4600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4600.0 < n < 4610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4610.0 < n < 4620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4610 <= n < 4700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4620 < n < 4700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4700.0 < n < 4710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4710.0 < n < 4720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4710 <= n < 4800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4720 < n < 4800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4800.0 < n < 4810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4810.0 < n < 4820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4810 <= n < 4900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4820 < n < 4900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 4900.0 < n < 4910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4910.0 < n < 4920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 4910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4910 <= n < 5000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 4920 < n < 5000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5000.0 < n < 5010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 5010.0 < n < 5020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 5010] + ' целых ' + float_numbers[float_number2]
    elif 5010.0 <= n < 5100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 5020.0 < n < 5100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5100.0 < n < 5110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5110.0 < n < 5120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5110 <= n < 5200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5120 < n < 5200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5200.0 < n < 5210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5210.0 < n < 5220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5210 <= n < 5300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5220 < n < 5300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5300.0 < n < 5310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5310.0 < n < 5320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5310 <= n < 5400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5320 < n < 5400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5400.0 < n < 5410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5410.0 < n < 5420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5410 <= n < 5500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5420 < n < 5500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5500.0 < n < 5510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5510.0 < n < 5520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5510 <= n < 5600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5520 < n < 5600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5600.0 < n < 5610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5610.0 < n < 5620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5610 <= n < 5700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5620 < n < 5700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5700.0 < n < 5710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5710.0 < n < 5720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5710 <= n < 5800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5720 < n < 5800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5800.0 < n < 5810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5810.0 < n < 5820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5810 <= n < 5900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5820 < n < 5900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 5900.0 < n < 5910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5910.0 < n < 5920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 5910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5910 <= n < 6000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 5920 < n < 6000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6000.0 < n < 6010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 6010.0 < n < 6020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 6010] + ' целых ' + float_numbers[float_number2]
    elif 6010.0 <= n < 6100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 6020.0 < n < 6100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6100.0 < n < 6110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6110.0 < n < 6120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6110 <= n < 6200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6120 < n < 6200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6200.0 < n < 6210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6210.0 < n < 6220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6210 <= n < 6300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6220 < n < 6300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6300.0 < n < 6310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6310.0 < n < 6320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6310 <= n < 6400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6320 < n < 6400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6400.0 < n < 6410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6410.0 < n < 6420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6410 <= n < 6500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6420 < n < 6500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6500.0 < n < 6510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6510.0 < n < 6520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6510 <= n < 6600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6520 < n < 6600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6600.0 < n < 6610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6610.0 < n < 6620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6610 <= n < 6700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6620 < n < 6700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6700.0 < n < 6710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6710.0 < n < 6720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6710 <= n < 6800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6720 < n < 6800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6800.0 < n < 6810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6810.0 < n < 6820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6810 <= n < 6900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6820 < n < 6900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 6900.0 < n < 6910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6910.0 < n < 6920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 6910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6910 <= n < 7000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 6920 < n < 7000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7000.0 < n < 7010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 7010.0 < n < 7020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 7010] + ' целых ' + float_numbers[float_number2]
    elif 7010.0 <= n < 7100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 7020.0 < n < 7100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7100.0 < n < 7110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7110.0 < n < 7120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7110 <= n < 7200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7120 < n < 7200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7200.0 < n < 7210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7210.0 < n < 7220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7210 <= n < 7300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7220 < n < 7300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7300.0 < n < 7310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7310.0 < n < 7320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7310 <= n < 7400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7320 < n < 7400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7400.0 < n < 7410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7410.0 < n < 7420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7410 <= n < 7500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7420 < n < 7500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7500.0 < n < 7510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7510.0 < n < 7520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7510 <= n < 7600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7520 < n < 7600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7600.0 < n < 7610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7610.0 < n < 7620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7610 <= n < 7700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7620 < n < 7700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7700.0 < n < 7710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7710.0 < n < 7720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7710 <= n < 7800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7720 < n < 7800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7800.0 < n < 7810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7810.0 < n < 7820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7810 <= n < 7900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7820 < n < 7900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 7900.0 < n < 7910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7910.0 < n < 7920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 7910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7910 <= n < 8000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 7920 < n < 8000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8000.0 < n < 8010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 8010.0 < n < 8020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 8010] + ' целых ' + float_numbers[float_number2]
    elif 8010.0 <= n < 8100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 8020.0 < n < 8100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8100.0 < n < 8110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8110.0 < n < 8120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8110 <= n < 8200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8120 < n < 8200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8200.0 < n < 8210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8210.0 < n < 8220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8210 <= n < 8300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8220 < n < 8300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8300.0 < n < 8310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8310.0 < n < 8320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8310 <= n < 8400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8320 < n < 8400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8400.0 < n < 8410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8410.0 < n < 8420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8410 <= n < 8500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8420 < n < 8500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8500.0 < n < 8510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8510.0 < n < 8520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8510 <= n < 8600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8520 < n < 8600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8600.0 < n < 8610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8610.0 < n < 8620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8610 <= n < 8700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8620 < n < 8700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8700.0 < n < 8710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8710.0 < n < 8720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8710 <= n < 8800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8720 < n < 8800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8800.0 < n < 8810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8810.0 < n < 8820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8810 <= n < 8900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8820 < n < 8900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 8900.0 < n < 8910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8910.0 < n < 8920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 8910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8910 <= n < 9000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 8920 < n < 9000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9000.0 < n < 9010.0:
        return number5[int(d2)] + ' ' + number1[int(n1)] + ' целых ' + float_numbers[float_number2]
    elif 9010.0 < n < 9020.0 and n3 < 20 and n1 != 0:
        return number5[int(d2)] + ' ' + number3[int(int_number) - 9010] + ' целых ' + float_numbers[float_number2]
    elif 9010.0 <= n < 9100.0 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' целых ' + float_numbers[float_number2]
    elif 9020.0 < n < 9100.0:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9100.0 < n < 9110.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9110.0 < n < 9120.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9110)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9110 <= n < 9200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9120 < n < 9200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9200.0 < n < 9210.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9210.0 < n < 9220.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9210)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9210 <= n < 9300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9220 < n < 9300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9300.0 < n < 9310.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9310.0 < n < 9320.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9310)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9310 <= n < 9400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9320 < n < 9400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9400.0 < n < 9410.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9410.0 < n < 9420.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9410)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9410 <= n < 9500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9420 < n < 9500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9500.0 < n < 9510.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9510.0 < n < 9520.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9510)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9510 <= n < 9600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9520 < n < 9600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9600.0 < n < 9610.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9610.0 < n < 9620.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9610)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9610 <= n < 9700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9620 < n < 9700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9700.0 < n < 9710.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9710.0 < n < 9720.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9710)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9710 <= n < 9800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9720 < n < 9800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9800.0 < n < 9810.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9810.0 < n < 9820.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9810)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9810 <= n < 9900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9820 < n < 9900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    elif 9900.0 < n < 9910.0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[int(n1)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9910.0 < n < 2920.0 and n1 != 0:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int(int_number - 9910)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9910 <= n < 10000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' целых ' + \
               float_numbers[float_number2]
    elif 9920 < n < 10000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[int(n1)] + \
               ' целых ' + float_numbers[float_number2]
    else:
        print('Извините, но калькулятор пока что не может вывести текстом запрашиваемый результат')