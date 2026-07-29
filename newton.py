def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Newton\'s Formula using Geometric Construction' + Format.end)
    n = int(input('Enter the number of terms: '))
    total = 0.0
    m = 0
    for i in range(1, n + 1):
        power = 2 * i + 3
        total += 1 / ((2 ** power) * power * (2 ** m))
        m += 2
    calculated = (3 * math.sqrt(3) / 4) + (24 * ((1 / 12) - total))
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
