def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Madhava-Leibniz series' + Format.end)
    terms = int(input('Enter the number of terms inside the bracket: '))
    even_sum = 0.0
    odd_diff = 0.0
    for index, i in enumerate(range(1, terms * 2, 2)):
        if index % 2 == 0:
            even_sum += 1 / i
        else:
            odd_diff -= 1 / i
    calculated = 4 * (even_sum + odd_diff)
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
