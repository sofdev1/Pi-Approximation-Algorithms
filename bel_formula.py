def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Bellard\'s Formula 2.0' + Format.end)
    n = int(input('Enter the number of terms: '))
    total = 0.0
    for i in range(1, n):
        p = (-885673181 * (i ** 5)) + (3125347237 * (i ** 4)) - (2942969225 * (i ** 3)) + (1031962795 * (i ** 2)) - \
            (196882274 * i) + 10996648
        binomial_coefficient = math.factorial(7 * i) / (math.factorial(2 * i) * math.factorial(5 * i))
        total += (3 * p) / (binomial_coefficient * (2 ** (i - 1)))
    calculated = (1 / 740025) * (total - 20379280)

    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
