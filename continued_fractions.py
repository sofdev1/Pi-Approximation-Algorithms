def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Euler\'s Continued Fractions Series for Pi' + Format.end)
    n = int(input('Enter the number of fractional terms you want: '))
    term = (2 * n) - 1
    first = (term ** 2) + 2
    while term != 3:
        first = (((term - 2) ** 2) / first) + 2
        term -= 2
    calculated = 4 / (1 + 1 / first)
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
