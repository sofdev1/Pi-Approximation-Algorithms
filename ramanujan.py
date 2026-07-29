def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Ramanujan pi approximation' + Format.end)
    k = int(input('Enter the number of terms(System can handle value of k till 39 only): '))
    constant = (2 * math.sqrt(2)) / 9801
    total = 0.0
    for i in range(0, k):
        summation1 = (math.factorial(4 * i) * (1103 + 26390 * i)) / ((math.factorial(i) ** 4) * ((396) ** (4 * i)))
        print('For k equals ', i, 'Pi is ', (constant * summation1) ** (-1))
        total += summation1
    calculated = (constant * total) ** (-1)
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
