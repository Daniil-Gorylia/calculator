# Здесь содержится информация о прописных числах, но только целых, принцип действия тот же как и в floatnumbers,
# по существу функционал их заключается только в выводе текста, и открывать данные файлы не имеет значения

def number_to_words(n):
    number1 = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
    number2 = (None, 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
               'девяносто')
    number3 = (None, 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
               'семнадцать', 'восемнадцать', 'девятнадцать')
    number4 = (None, 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
               'девятьсот')
    number5 = (None, 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч',
               'семь тысяч', 'восемь тысяч', 'девять тысяч')
    n1 = n % 10
    n2 = n - n1
    n3 = n2 % 100
    n4 = n2 % 1000
    d = n / 10
    d1 = n / 100
    d2 = n / 1000
    if n < 10:
        return number1[n]
    elif 10 < n < 20:
        return number3[n - 10]
    elif 10 <= n < 100 and d.is_integer() and number2[int(d)] in number2:
        return number2[int(d)]
    elif 20 < n < 100:
        return number2[int(n2 / 10)] + ' ' + number1[n1]
    elif 100 <= n < 1000 and d1.is_integer() and number4[int(d1)] in number4:
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
    elif 1000 <= n < 10000 and d2.is_integer() and number5[int(d2)] in number5:
        return number5[int(d2)]
    elif 1000 < n < 1010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 1010 < n < 1020:
        return number5[int(d2)] + ' ' + number3[n - 1010]
    elif 1010 <= n < 1100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 1020 < n < 1100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1100 < n < 1110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1110 < n < 1120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1110]
    elif 1110 <= n < 1200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1120 < n < 1200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1200 < n < 1210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1210 < n < 1220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1210]
    elif 1210 <= n < 1300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1220 < n < 1300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1300 < n < 1310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1310 < n < 1320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1310]
    elif 1310 <= n < 1400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1320 < n < 1400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1400 < n < 1410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1410 < n < 1420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1410]
    elif 1410 <= n < 1500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1420 < n < 1500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1500 < n < 1510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1510 < n < 1520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1510]
    elif 1510 <= n < 1600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1520 < n < 1600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1600 < n < 1610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1610 < n < 1620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1610]
    elif 1610 <= n < 1700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1620 < n < 1700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1700 < n < 1710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1710 < n < 1720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1710]
    elif 1710 <= n < 1800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1720 < n < 1800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1800 < n < 1810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1810 < n < 1820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1810]
    elif 1810 <= n < 1900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1820 < n < 1900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1900 < n < 1910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 1910 < n < 1920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1910]
    elif 1910 <= n < 2000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 1920 < n < 2000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 1099 < n < 2000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 2000 < n < 2010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 2010 < n < 2020:
        return number5[int(d2)] + ' ' + number3[n - 1010]
    elif 2010 <= n < 2100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 2020 < n < 2100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2100 < n < 2110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2110 < n < 2120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2110]
    elif 2110 <= n < 2200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2120 < n < 2200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2200 < n < 2210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2210 < n < 2220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2210]
    elif 2210 <= n < 2300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2220 < n < 2300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2300 < n < 2310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2310 < n < 2320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2310]
    elif 2310 <= n < 2400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2320 < n < 2400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2400 < n < 2410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2410 < n < 2420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2410]
    elif 2410 <= n < 2500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2420 < n < 2500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2500 < n < 2510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2510 < n < 2520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2510]
    elif 2510 <= n < 2600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2520 < n < 2600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2600 < n < 2610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2610 < n < 2620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2610]
    elif 2610 <= n < 2700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2620 < n < 2700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2700 < n < 2710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2710 < n < 2720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2710]
    elif 2710 <= n < 2800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2720 < n < 2800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2800 < n < 2810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2810 < n < 2820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2810]
    elif 2810 <= n < 2900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2820 < n < 2900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2900 < n < 2910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 2910 < n < 2920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 2910]
    elif 2910 <= n < 3000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 2920 < n < 3000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 2099 < n < 3000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 3000 < n < 3010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 3010 < n < 3020:
        return number5[int(d2)] + ' ' + number3[n - 3010]
    elif 3010 <= n < 3100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 3020 < n < 3100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3100 < n < 3110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3110 < n < 3120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3110]
    elif 3110 <= n < 3200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3120 < n < 3200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3200 < n < 3210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3210 < n < 3220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3210]
    elif 3210 <= n < 3300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3220 < n < 3300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3300 < n < 3310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3310 < n < 3320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3310]
    elif 3310 <= n < 3400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3320 < n < 3400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3400 < n < 3410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3410 < n < 3420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3410]
    elif 3410 <= n < 3500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3420 < n < 3500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3500 < n < 3510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3510 < n < 3520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3510]
    elif 3510 <= n < 3600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3520 < n < 3600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3600 < n < 3610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3610 < n < 3620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3610]
    elif 3610 <= n < 3700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3620 < n < 3700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3700 < n < 3710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3710 < n < 3720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3710]
    elif 3710 <= n < 3800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3720 < n < 3800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3800 < n < 3810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3810 < n < 3820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 3810]
    elif 3810 <= n < 3900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3820 < n < 3900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3900 < n < 3910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 3910 < n < 3920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1910]
    elif 3910 <= n < 4000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 3920 < n < 4000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 3099 < n < 4000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 4000 < n < 4010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 4010 < n < 4020:
        return number5[int(d2)] + ' ' + number3[n - 4010]
    elif 4010 <= n < 4100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 4020 < n < 4100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4100 < n < 4110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4110 < n < 4120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4110]
    elif 4110 <= n < 4200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4120 < n < 4200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4200 < n < 4210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4210 < n < 4220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4210]
    elif 4210 <= n < 4300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4220 < n < 4300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4300 < n < 4310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4310 < n < 4320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4310]
    elif 4310 <= n < 4400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4320 < n < 4400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4400 < n < 4410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4410 < n < 4420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4410]
    elif 4410 <= n < 4500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4420 < n < 4500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4500 < n < 4510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4510 < n < 4520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1510]
    elif 4510 <= n < 4600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4520 < n < 4600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4600 < n < 4610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4610 < n < 4620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4610]
    elif 4610 <= n < 4700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4620 < n < 4700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4700 < n < 4710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4710 < n < 4720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4710]
    elif 4710 <= n < 4800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4720 < n < 4800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4800 < n < 4810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4810 < n < 4820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 4810]
    elif 4810 <= n < 4900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4820 < n < 4900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4900 < n < 4910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 4910 < n < 4920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1910]
    elif 4910 <= n < 5000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 4920 < n < 5000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 4099 < n < 5000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 5000 < n < 5010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 5010 < n < 5020:
        return number5[int(d2)] + ' ' + number3[n - 5010]
    elif 5010 <= n < 5100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 5020 < n < 5100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5100 < n < 5110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5110 < n < 5120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1110]
    elif 5110 <= n < 5200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5120 < n < 5200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5200 < n < 5210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5210 < n < 5220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5210]
    elif 5210 <= n < 5300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5220 < n < 5300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5300 < n < 5310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5310 < n < 5320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5310]
    elif 5310 <= n < 5400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5320 < n < 5400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5400 < n < 5410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5410 < n < 5420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 1410]
    elif 5410 <= n < 5500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5420 < n < 5500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5500 < n < 5510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5510 < n < 5520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5510]
    elif 5510 <= n < 5600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5520 < n < 5600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5600 < n < 5610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5610 < n < 5620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5610]
    elif 5610 <= n < 5700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5620 < n < 5700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5700 < n < 5710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5710 < n < 5720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5710]
    elif 5710 <= n < 5800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5720 < n < 5800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5800 < n < 5810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5810 < n < 5820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5810]
    elif 5810 <= n < 5900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5820 < n < 5900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5900 < n < 5910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 5910 < n < 5920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 5910]
    elif 5910 <= n < 6000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 5920 < n < 6000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 5099 < n < 6000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 6000 < n < 6010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 6010 < n < 6020:
        return number5[int(d2)] + ' ' + number3[n - 6010]
    elif 6010 <= n < 6100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 6020 < n < 6100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6100 < n < 6110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6110 < n < 6120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6110]
    elif 6110 <= n < 6200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6120 < n < 6200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6200 < n < 6210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6210 < n < 6220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6210]
    elif 6210 <= n < 6300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6220 < n < 6300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6300 < n < 6310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6310 < n < 6320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6310]
    elif 6310 <= n < 6400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6320 < n < 6400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6400 < n < 6410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6410 < n < 6420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6410]
    elif 6410 <= n < 6500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6420 < n < 6500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6500 < n < 6510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6510 < n < 6520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6510]
    elif 6510 <= n < 6600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6520 < n < 6600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6600 < n < 6610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6610 < n < 6620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6610]
    elif 6610 <= n < 6700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6620 < n < 6700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6700 < n < 6710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6710 < n < 6720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6710]
    elif 6710 <= n < 6800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6720 < n < 6800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6800 < n < 6810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6810 < n < 6820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6810]
    elif 6810 <= n < 6900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6820 < n < 6900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6900 < n < 6910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 6910 < n < 6920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 6910]
    elif 6910 <= n < 7000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 6920 < n < 7000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 6099 < n < 7000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 7000 < n < 7010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 7010 < n < 7020:
        return number5[int(d2)] + ' ' + number3[n - 7010]
    elif 7010 <= n < 7100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 7020 < n < 7100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7100 < n < 7110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7110 < n < 7120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7110]
    elif 7110 <= n < 7200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7120 < n < 7200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7200 < n < 7210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7210 < n < 7220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7210]
    elif 7210 <= n < 7300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7220 < n < 7300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7300 < n < 7310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7310 < n < 7320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7310]
    elif 7310 <= n < 7400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7320 < n < 7400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7400 < n < 7410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7410 < n < 7420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7410]
    elif 7410 <= n < 7500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7420 < n < 7500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7500 < n < 7510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7510 < n < 7520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7510]
    elif 7510 <= n < 7600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7520 < n < 7600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7600 < n < 7610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7610 < n < 7620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7610]
    elif 7610 <= n < 7700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7620 < n < 7700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7700 < n < 7710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7710 < n < 7720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7710]
    elif 7710 <= n < 7800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7720 < n < 7800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7800 < n < 7810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7810 < n < 7820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7810]
    elif 7810 <= n < 7900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7820 < n < 7900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7900 < n < 7910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 7910 < n < 7920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 7910]
    elif 7910 <= n < 8000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 7920 < n < 8000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 7099 < n < 8000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 8000 < n < 8010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 8010 < n < 8020:
        return number5[int(d2)] + ' ' + number3[n - 8010]
    elif 8010 <= n < 8100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 8020 < n < 8100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8100 < n < 8110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8110 < n < 8120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8110]
    elif 8110 <= n < 8200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8120 < n < 8200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8200 < n < 8210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8210 < n < 8220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8210]
    elif 8210 <= n < 8300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8220 < n < 8300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8300 < n < 8310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8310 < n < 8320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8310]
    elif 8310 <= n < 8400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8320 < n < 8400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8400 < n < 8410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8410 < n < 8420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8410]
    elif 8410 <= n < 8500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8420 < n < 8500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8500 < n < 8510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8510 < n < 8520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8510]
    elif 8510 <= n < 8600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8520 < n < 8600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8600 < n < 8610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8610 < n < 8620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8610]
    elif 8610 <= n < 8700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8620 < n < 8700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8700 < n < 8710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8710 < n < 8720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8710]
    elif 8710 <= n < 8800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8720 < n < 8800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8800 < n < 8810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8810 < n < 8820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8810]
    elif 8810 <= n < 8900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8820 < n < 8900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8900 < n < 8910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 8910 < n < 8920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 8910]
    elif 8910 <= n < 9000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 8920 < n < 9000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 8099 < n < 9000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    elif 9000 < n < 9010:
        return number5[int(d2)] + ' ' + number1[n1]
    elif 9010 < n < 9020:
        return number5[int(d2)] + ' ' + number3[n - 9010]
    elif 9010 <= n < 9100 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
    elif 9020 < n < 9100:
        return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9100 < n < 9110:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9110 < n < 9120:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9110]
    elif 9110 <= n < 9200 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9120 < n < 9200:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9200 < n < 9210:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9210 < n < 9220:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9210]
    elif 9210 <= n < 9300 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9220 < n < 9300:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9300 < n < 9310:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9310 < n < 9320:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9310]
    elif 9310 <= n < 9400 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9320 < n < 9400:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9400 < n < 9410:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9410 < n < 9420:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9410]
    elif 9410 <= n < 9500 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9420 < n < 9500:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9500 < n < 9510:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9510 < n < 9520:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9510]
    elif 9510 <= n < 9600 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9520 < n < 9600:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9600 < n < 9610:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9610 < n < 9620:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9610]
    elif 9610 <= n < 9700 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9620 < n < 9700:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9700 < n < 9710:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9710 < n < 9720:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9710]
    elif 9710 <= n < 9800 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9720 < n < 9800:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9800 < n < 9810:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9810 < n < 9820:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9810]
    elif 9810 <= n < 9900 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9820 < n < 9900:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9900 < n < 9910:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    elif 9910 < n < 9920:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[n - 9910]
    elif 9910 <= n < 10000 and n1 == 0 and number5[int(d2)] in number5:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
    elif 9920 < n < 10000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
    elif 9099 < n < 10000:
        return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
    else:
        print('Извините, но калькулятор пока что не может вывести текстом запрашиваемый результат')
