import math


def compute_arctan_value(n, x):
    total = 0.0
    term = x
    for i in range(n):
        total += term / (2 * i + 1)
        term *= -x * x
    return total


def f():
    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Machin- like Formulae' + Format.end)
    n = int(input('Enter the number of terms: '))
    methods = input('''
Enter the method you want to use (enter the number):-
1. Euler's
2. Hermann's
3. Vega's
4. Machin's
5. Hitachi Supercomputer
6. Jorg Uwe Arndt's
7. Hwang Chien-Lih's
''')
    if methods == '1':
        result = compute_arctan_value(n, 1 / 2) + compute_arctan_value(n, 1 / 3)
    elif methods == '2':
        result = 2 * compute_arctan_value(n, 1 / 2) - compute_arctan_value(n, 1 / 7)
    elif methods == '3':
        result = 2 * compute_arctan_value(n, 1 / 3) + compute_arctan_value(n, 1 / 7)
    elif methods == '4':
        result = 4 * compute_arctan_value(n, 1 / 5) - compute_arctan_value(n, 1 / 239)
    elif methods == '5':
        type = input('''
Enter the equation number:-
1. Takano
2. Stormer
''')
        if type == '1':
            result = 12 * compute_arctan_value(n, 1 / 49) + 32 * compute_arctan_value(n, 1 / 57) - 5 * compute_arctan_value(n, 1 / 239) + \
                     12 * compute_arctan_value(n, 1 / 110443)
        elif type == '2':
            result = 44 * compute_arctan_value(n, 1 / 57) + 7 * compute_arctan_value(n, 1 / 239) - 12 * compute_arctan_value(n, 1 / 682) + \
                     24 * compute_arctan_value(n, 1 / 12943)
        else:
            result = 0.0
    elif methods == '6':
        result = 36462 * compute_arctan_value(n, 1 / 390112) + 135908 * compute_arctan_value(n, 1 / 485298) + 274509 * compute_arctan_value(n, 1 / 683982) - \
                 39581 * compute_arctan_value(n, 1 / 1984933) + 178477 * compute_arctan_value(n, 1 / 2478328) - 114569 * compute_arctan_value(n, 1 / 3449051) - \
                 146571 * compute_arctan_value(n, 1 / 18975991) + 61914 * compute_arctan_value(n, 1 / 22709274) - 69044 * compute_arctan_value(n, 1 / 24208144) \
                 - 89431 * compute_arctan_value(n, 1 / 201229582) - 43938 * compute_arctan_value(n, 1 / 2189376182)
    elif methods == '7':
        result = 36462 * compute_arctan_value(n, 1 / 51387) + 26522 * compute_arctan_value(n, 1 / 485298) + 19275 * compute_arctan_value(n, 1 / 683982) - \
                 3119 * compute_arctan_value(n, 1 / 1984933) - 3833 * compute_arctan_value(n, 1 / 2478328) - 5183 * compute_arctan_value(n, 1 / 3449051) - \
                 37185 * compute_arctan_value(n, 1 / 18975991) - 11010 * compute_arctan_value(n, 1 / 22709274) + 3880 * compute_arctan_value(n, 1 / 24208144) - \
                 16507 * compute_arctan_value(n, 1 / 201229582) - 7476 * compute_arctan_value(n, 1 / 2189376182)
    else:
        result = 0.0
    calculated = 4 * result
    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")
