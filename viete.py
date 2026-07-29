def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Viete\'s Formula for Pi approximation' + Format.end)
    n = int(input('Enter the number of terms: '))
    product = 1.0
    for i in range(1, n + 1):
        product *= math.cos(math.pi / (2 ** (i + 1)))

    calculated = 2 / product
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
