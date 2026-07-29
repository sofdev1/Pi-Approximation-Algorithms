def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Wallis Product' + Format.end)
    product = 1.0
    n = int(input('Enter the number of terms: '))
    for i in range(1, n):
        num = 4 * (i ** 2)
        deno = num - 1
        product *= num / deno
    calculated = 2 * product
    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")
