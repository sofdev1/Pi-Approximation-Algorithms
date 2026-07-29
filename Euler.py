def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Euler\'s Approximation' + Format.end)
    k = int(input('Enter the number of terms: '))

    even_sum1 = odd_diff1 = 0
    even_sum2 = odd_diff2 = 0
    even_sum3 = odd_diff3 = 0
    even_sum4 = odd_diff4 = 0
    even_sum5 = odd_diff5 = 0
    even_sum6 = odd_diff6 = 0
    for i in range(0, k):
        summation1 = ((64 ** i) * (1 + 4 * i)) ** (-1)
        summation2 = ((64 ** i) * (1 + 2 * i)) ** (-1)
        summation3 = ((64 ** i) * (3 + 4 * i)) ** (-1)
        summation4 = ((1024 ** i) * (1 + 4 * i)) ** (-1)
        summation5 = ((1024 ** i) * (1 + 2 * i)) ** (-1)
        summation6 = ((1024 ** i) * (3 + 4 * i)) ** (-1)

        if i % 2 == 0:
            even_sum1 += summation1
            even_sum2 += summation2
            even_sum3 += summation3
            even_sum4 += summation4
            even_sum5 += summation5
            even_sum6 += summation6
        else:
            odd_diff1 -= summation1
            odd_diff2 -= summation2
            odd_diff3 -= summation3
            odd_diff4 -= summation4
            odd_diff5 -= summation5
            odd_diff6 -= summation6

    calculated = (2 * (even_sum1 + odd_diff1) + 0.5 * (even_sum2 + odd_diff2) + 0.25 * (even_sum3 + odd_diff3)) + \
                 (0.5 * (even_sum4 + odd_diff4) + 0.0625 * (even_sum5 + odd_diff5) + 0.015625 * (even_sum6 + odd_diff6))
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
