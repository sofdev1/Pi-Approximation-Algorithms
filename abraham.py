def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Infinite Sum Series of Abraham Sharp' + Format.end)
    n = int(input('Enter the number of terms: '))
    total = 0.0
    for i in range(0, n):
        total += (2 * ((-1) ** i) * 3 ** (0.5 - i)) / (2 * i + 1)
    calculated = total
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
