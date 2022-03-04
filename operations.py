def number_to_words(n):
    number1 = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
    number2 = (None, 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
               'девяносто')
    number3 = (None, 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
               'семнадцать', 'восемнадцать', 'девятнадцать')
    number4 = (None, 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
               'девятьсот')
    n1 = n % 10
    n2 = n - n1
    n3 = n2 % 100
    d = n / 10
    d1 = n / 100
    if n < 10:
        return number1[n]
    elif 10 < n < 20:
        return number3[n - 10]
    elif 10 <= n < 100 and d.is_integer() and number2[int(d)] in number2:
        return number2[int(d)]
    elif 20 < n < 100:
        return number2[int(n2 / 10)] + ' ' + number1[n1]
    elif n >= 100 and d1.is_integer() and number4[int(d1)] in number4:
        return number4[int(d1)]
    elif 100 < n < 110:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 110 < n < 120:
        return number4[int(d1)] + ' ' + number3[n - 110]
    elif 110 <= n < 200 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 120 < n < 200:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 200 < n < 210:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 210 < n < 220:
        return number4[int(d1)] + ' ' + number3[n - 210]
    elif 210 <= n < 300 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 220 < n < 300:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 300 < n < 310:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 310 < n < 320:
        return number4[int(d1)] + ' ' + number3[n - 310]
    elif 310 <= n < 400 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 320 < n < 400:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 400 < n < 410:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 410 < n < 420:
        return number4[int(d1)] + ' ' + number3[n - 410]
    elif 410 <= n < 500 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 420 < n < 500:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 500 < n < 510:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 510 < n < 520:
        return number4[int(d1)] + ' ' + number3[n - 510]
    elif 510 <= n < 600 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 520 < n < 600:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 600 < n < 610:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 610 < n < 620:
        return number4[int(d1)] + ' ' + number3[n - 710]
    elif 610 <= n < 700 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 620 < n < 700:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 700 < n < 710:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 710 < n < 720:
        return number4[int(d1)] + ' ' + number3[n - 710]
    elif 710 <= n < 800 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 720 < n < 800:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 800 < n < 810:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 810 < n < 820:
        return number4[int(d1)] + ' ' + number3[n - 810]
    elif 810 <= n < 900 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 820 < n < 900:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 900 < n < 910:
        return number4[int(d1)] + ' ' + number1[n1]
    elif 910 < n < 920:
        return number4[int(d1)] + ' ' + number3[n - 910]
    elif 910 <= n < 1000 and n1 == 0 and number4[int(d1)] in number4:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
    elif 920 < n < 1000:
        return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
