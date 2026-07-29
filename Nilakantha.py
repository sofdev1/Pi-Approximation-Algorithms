def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Nilakantha Series' + Format.end)

    n = int(input('Enter the number of terms: '))
    total = 0.0
    for i in range(1, n):
        total += ((-1) ** (i + 1)) / (i * (i + 1) * (i + 2))
    calculated = total + 3
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
