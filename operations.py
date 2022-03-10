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
    n22 = n % 100
    n4 = n2 % 1000
    n44 = n % 1000
    d23 = n44 - n22
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
    elif 100 < n < 1000:
        if n3 >0 and n1 == 0:
            return number4[int(d1)] + ' ' + number2[int(n3 / 10)]
        elif 10 < n22 < 20:
            return number4[int(d1)] + ' ' + number3[int(n22 - 10)]
        elif n22 > 20:
            return number4[int(d1)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
        elif n1 > 0:
            return number4[int(d1)] + ' ' + number1[n1]
    elif 1000 <= n < 10000 and d2.is_integer() and number5[int(d2)] in number5:
        return number5[int(d2)]
    elif 1000 < n < 10000:
        if n1 == 0 and d23 < 100:
            return number5[int(d2)] + ' ' + number2[int(n3 / 10)]
        elif 10 < n22 < 20 and d23 < 100:
            return number5[int(d2)] + ' ' + number3[int(n22 - 10)]
        elif n22 > 20 and d23 < 100:
            return number5[int(d2)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
        elif n1 > 0 and d23 < 100:
            return number5[int(d2)] + ' ' + number1[n1]
        elif n44 >= 100 and n1 == 0 and n22 ==0:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)]
        elif n1 ==0 and n22 >= 10:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)]
        elif 10 < n22 < 20:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number3[int (n22 - 10)]
        elif n22 > 20:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number2[int(n3 / 10)] + ' ' + number1[n1]
        elif n1 > 0:
            return number5[int(d2)] + ' ' + number4[int(n4 / 100)] + ' ' + number1[n1]
    else:
        print('Извините, но калькулятор пока что не может вывести текстом запрашиваемый результат')

