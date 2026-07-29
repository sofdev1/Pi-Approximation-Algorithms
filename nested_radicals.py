def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + "Viete's Nested Radicals Formula for Pi" + Format.end)
    n = int(input('Enter the value of \'N\' (greater than 2) in the Formula: '))
    term = math.sqrt(2)
    for _ in range(n-3):
        term = term + 2
        term = term ** 0.5
    calculated = (2 ** (n-1)) * math.sqrt(2 - term)
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
