import math


C = 262537412640768000
A0 = 13591409
A_COEFF = 545140134


def compute_chudnovsky_denominators(terms):
    denominators = []
    denominator = float(A0)
    a_prev = float(A0)

    for i in range(terms):
        denominators.append(denominator)
        if i == terms - 1:
            break

        i_next = i + 1
        a_next = A_COEFF * i_next + A0
        numerator_factor = (
            (6 * i_next - 5)
            * (6 * i_next - 4)
            * (6 * i_next - 3)
            * (6 * i_next - 2)
            * (6 * i_next - 1)
            * (6 * i_next)
        )
        denominator_factor = (
            (3 * i_next - 2)
            * (3 * i_next - 1)
            * (3 * i_next)
            * (i_next ** 3)
        )
        denominator *= numerator_factor * (a_next / a_prev) / denominator_factor / (-C)
        a_prev = a_next

    return denominators


def f():
    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Chudnovsky Pi Approximation Algorithm' + Format.end)
    k = int(input('Enter the number of terms (system can handle till 22): '))
    numerator = 426880 * math.sqrt(10005)

    denominators = compute_chudnovsky_denominators(k)
    total_denominator = sum(denominators)
    for i, denominator in enumerate(denominators):
        print('For k equals ', i, 'Pi is ', (numerator / denominator))

    calculated = (numerator / total_denominator)
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
