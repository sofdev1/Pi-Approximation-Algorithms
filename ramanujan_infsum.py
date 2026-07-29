def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Infinite Sum Series by Ramanujan' + Format.end)
    n = int(input('Enter the number of terms: '))
    total = 0.0
    for i in range(0, n):
        binomial_coefficient = math.factorial(2 * i) / (math.factorial(i) ** 2)
        num = 42 * i + 5
        deno = 2 ** (12 * i + 4)
        total += (binomial_coefficient ** 3) * (num / deno)
    calculated = 1 / total
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
