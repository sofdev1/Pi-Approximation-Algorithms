def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Ramanujan\'s Continued Fractions Series for Pi' + Format.end)
    n = int(input('Enter the number of fractional terms you want: '))
    lem = 2.62205755
    term = (2 * n) - 1
    first = (term ** 2) + 4
    while term != 3:
        a = ((term - 2) ** 2) / first
        b = a + 4
        first = b
        term = term - 2
    calculated = (lem ** 2) / (2 + 1 / first)
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
