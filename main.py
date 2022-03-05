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


if counter.is_integer():
    print(int(counter))
    if counter < 0:
        print('минус ' + operations.number_to_words(int(counter * -1)))
    else:
        print(operations.number_to_words(int(counter)))
else:
   a = round(counter, 1)
   print(float(a))
   if counter < 0:
       print('минус ' + floatnumbers.float_number_to_words(a * -1))
   else:
       print(floatnumbers.float_number_to_words(a))

