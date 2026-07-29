def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Madhava Approximation of Pi' + Format.end)
    k = int(input('Enter the number of terms: '))
    constant = math.sqrt(12)
    total = 0.0
    for i in range(0, k):
        total += ((-3) ** (-i)) / (2 * i + 1)
    calculated = constant * total
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
