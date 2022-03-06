# Основной функционал калькулятора находится в данном файле, разобраться в нем проще простого,
# учитывайте что калькулятор не может выводить текстом значения выше 9999
import floatnumbers
import operations
number_1 = float(input('Введите любое первое число'))
my_operators = input('Введите оператор (+, -, /, *, mod, pow, div)')
number_2 = float(input('Введите любое второе число'))
counter = 0

if my_operators == '+':
    counter = number_1 + number_2
elif my_operators == '-':
    counter = number_1 - number_2
elif my_operators == '/':
    counter = number_1 / number_2
elif my_operators == '*':
    counter = number_1 * number_2
elif my_operators == 'mod':
    counter = number_1 % number_2
elif my_operators == 'pow':
    counter = pow(number_1, number_2)
elif my_operators == 'div':
    counter = number_1 // number_2

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

