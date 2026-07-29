def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Plouffe Series' + Format.end)

    k = int(input('Enter the number of terms: '))
    total = 0.0
    for i in range(1, k):
        num = i * ((2 ** i) * (math.factorial(i) ** 2))
        deno = math.factorial(2 * i)
        total += num / deno
    calculated = total - 3
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
