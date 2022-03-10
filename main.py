# Основной функционал калькулятора находится в данном файле, разобраться в нем проще простого,
# учитывайте что калькулятор не может выводить текстом значения выше 9999
import floatnumbers
import operations

counter_for_while = 1
print('Этот калькулятор версии 1.5 выводит целые и вещественные цифры текстом, при этом он ограничен в выводе'
           '\n до 9999 и 9999.9, он может слаживать (+), отнимать (-), делить (/), умножать (*).\n А так же производить'
          ' взятие остатка от деления (mod), возведение в степень (pow), и целочисленное деление (div).\nКалькулятор'
          ' работает бесконечно и считает количество проводимых операций, для того чтобы остановить работу '
          '\n введите на любом этапе вычисления слово (stop)')

while True:


    a = input('Введите любое первое число')
    if a == 'stop':
        print(f'Количество выполненных операций:{counter_for_while}')
        break
    else:
        try:
            number_1 = float(a)
        except ValueError:
            print("Недопустимое значение, введите цифру с точкой или 'stop'")
            continue
    my_operators = input('Введите оператор (+, -, /, *, mod, pow, div)')
    if my_operators == 'stop':
        print(f'Количество выполненных операций:{counter_for_while}')
        break
    b = input('Введите любое второе число')
    if b == 'stop':
        break
    else:
        try:
            number_2 = float(b)
        except ValueError:
            print("Недопустимое значение, введите цифру с точкой или 'stop'")
            continue
    counter = 0

    if my_operators == '+':
        counter = number_1 + number_2
    elif my_operators == '-':
        counter = number_1 - number_2
    elif my_operators == '/':
        try:
            counter = number_1 / number_2
        except ZeroDivisionError:
            print('Деление на ноль')
            continue
    elif my_operators == '*':
        counter = number_1 * number_2
    elif my_operators == 'mod':
        try:
            counter = number_1 % number_2
        except ZeroDivisionError:
            print('Взятие нулевого остатка от деления')
            continue
    elif my_operators == 'pow':
        counter = pow(number_1, number_2)
    elif my_operators == 'div':
        try:
            counter = number_1 // number_2
        except ZeroDivisionError:
            print('Целочисленное деление на ноль')
            continue
    else:
        print('Вы ввели неверный оператор, повторите попытку')
        continue

    # Здесь происходит определение класса числа, для дальнейшего вывода текстом, если число является целым,
    # то выводится либо целое положительное, либо целое отрицательное число в зависимости от результата
    if counter.is_integer():
        print(int(counter))
        if counter < 0:
            print('минус ' + operations.number_to_words(int(counter * -1)))
        else:
            print(operations.number_to_words(int(counter)))
    else:
    # Все числа с запятой округляются до 0,1, здесь возможны погрешности в рассчетах, т.к не был использован модуль math,
    # в основном это сделано для вывода текста
       a = round(counter, 1)
       print(float(a))
       if counter < 0:
           print('минус ' + floatnumbers.float_number_to_words(a * -1))
       else:
           print(floatnumbers.float_number_to_words(a))

    print(f'Количество выполненных операций:{counter_for_while}')
    counter_for_while += 1
