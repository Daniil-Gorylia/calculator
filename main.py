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


if counter.is_integer() == True:
    print(int(counter))
else:
    print(float(counter))

print(operations.word[int(counter)])


