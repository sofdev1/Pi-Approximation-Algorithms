def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'Infinite Product Formulae by Euler' + Format.end)
    n = int(input('Enter the number of terms: '))
    choose = input('Enter "1" or "2" for different Infinite Product Series: ')

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_prime_numbers(number):
        prime_numbers = []
        num = 2
        while len(prime_numbers) < number:
            if is_prime(num):
                prime_numbers.append(num)
            num += 1
        return prime_numbers

    prime_list = generate_prime_numbers(n)
    if choose == '1':
        product = 1.0
        for j in range(1, n):
            product *= 1 + ((math.sin(0.5 * math.pi * prime_list[j])) / prime_list[j])
        calculated = 2 / product
    elif choose == '2':
        product = 1.0
        for j in range(1, n):
            product *= 1 + (((-1) ** ((prime_list[j] - 1) / 2)) / prime_list[j])
        calculated = 2 / product
    else:
        calculated = None
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
