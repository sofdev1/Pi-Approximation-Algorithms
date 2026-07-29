def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + "Plouffe's Formula" + Format.end)
    n = int(input('Enter the number of terms for each infinite series in the formula: '))
    first_total = 0.0
    second_total = 0.0
    third_total = 0.0
    for i in range(1, n):
        deno1 = i * (math.exp(i * math.pi) - 1)
        deno2 = i * (math.exp(2 * i * math.pi) - 1)
        deno3 = i * (math.exp(4 * i * math.pi) - 1)
        first_total += 1 / deno1
        second_total += 1 / deno2
        third_total += 1 / deno3
    calculated = 72 * first_total - 96 * second_total + 24 * third_total
    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")
