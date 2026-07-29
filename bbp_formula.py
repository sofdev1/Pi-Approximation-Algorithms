def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Bailey-Borwein-Plouffe (BBP) formula' + Format.end)
    k = int(input('Enter the number of terms: '))
    total = 0.0
    for i in range(0, k):
        total += (1 / (16 ** i)) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    calculated = total
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
