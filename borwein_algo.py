def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + "Borwein's Algorithms" + Format.end)
    n = int(input('Enter the number of iterations: '))
    choose = input('''
Choose the following Convergences:-
1. Quadratic
2. Cubic
3. Quartic
4. Quintic
5. Nonic
''')
    if choose == '1':
        a0_1 = math.sqrt(2)
        b0_1 = 0
        p0_1 = 2 + math.sqrt(2)
        for _ in range(n):
            a_1_new = (math.sqrt(a0_1) + 1 / (math.sqrt(a0_1))) / 2
            b_1_new = ((1 + b0_1) * math.sqrt(a0_1)) / (a0_1 + b0_1)
            a0_1 = a_1_new
            b0_1 = b_1_new
            p_1_new = ((1 + a0_1) * p0_1 * b0_1) / (1 + b0_1)
            p0_1 = p_1_new
        result1 = p0_1
        calculated = result1
    elif choose == '2':
        a0_2 = 1 / 3
        s0_2 = (math.sqrt(3) - 1) / 2
        for i in range(0, n):
            deno = 1 + 2 * ((1 - s0_2 ** 3) ** (1 / 3))
            r_2_new = 3 / deno
            s_2_new = (r_2_new - 1) / 2
            s0_2 = s_2_new
            a_2_new = (r_2_new ** 2) * a0_2 - ((3 ** i) * ((r_2_new ** 2) - 1))
            a0_2 = a_2_new
        result2 = 1 / a0_2
        calculated = result2
    elif choose == '3':
        a0_3 = 2 * ((math.sqrt(2) - 1) ** 2)
        y0_3 = math.sqrt(2) - 1
        for i in range(0, n):
            num = 1 - ((1 - y0_3 ** 4) ** (1 / 4))
            deno = 1 + ((1 - y0_3 ** 4) ** (1 / 4))
            y_3_new = num / deno
            a_3_new = (a0_3 * (1 + y_3_new) ** 4) - (((2 ** (2 * i + 3)) * y_3_new) * (1 + y_3_new + (y_3_new ** 2)))
            y0_3 = y_3_new
            a0_3 = a_3_new
        result3 = 1 / a0_3
        calculated = result3
    elif choose == '4':
        a0_4 = 0.5
        s0_4 = 5 * (math.sqrt(5) - 2)
        for i in range(0, n):
            x_4_new = (5/s0_4) - 1
            y_4_new = ((x_4_new - 1) ** 2) + 7
            z_4_new = (0.5 * x_4_new * (y_4_new + math.sqrt((y_4_new ** 2 - 4 * (x_4_new ** 3))))) ** (1 / 5)
            a_4_new = (s0_4 ** 2) * a0_4 - ((5 ** i) * ((((s0_4 ** 2) - 5) / 2) + math.sqrt(s0_4 * ((s0_4 ** 2) -
                                                                                                    2 * s0_4 + 5))))
            a0_4 = a_4_new
            deno = (z_4_new + (x_4_new/z_4_new) + 1) ** 2
            s_4_new = 25 / (deno * s0_4)
            s0_4 = s_4_new
        result4 = 1/a0_4
        calculated = result4
    elif choose == '5':
        a0_5 = 1/3
        r0_5 = (math.sqrt(3) - 1) / 2
        s0_5 = (1 - (r0_5 ** 3)) ** (1/3)
        for i in range(0, n):
            t_5_new = 1 + 2 * r0_5
            u_5_new = (9 * r0_5 * (1 + r0_5 + (r0_5 ** 2))) ** (1/3)
            v_5_new = (t_5_new ** 2) + (t_5_new * u_5_new) + (u_5_new ** 2)
            w_5_new = (27 * (1 + s0_5 + (s0_5 ** 2))) / v_5_new
            a_5_new = w_5_new * a0_5 + (3 ** (2 * i - 1)) * (1 - w_5_new)
            s_5_new = ((1 - r0_5) ** 3) / ((t_5_new + 2 * u_5_new) * v_5_new)
            r_5_new = (1 - (s_5_new ** 3)) ** (1/3)
            s0_5 = s_5_new
            r0_5 = r_5_new
            a0_5 = a_5_new
        result5 = 1/a0_5
        calculated = result5
    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")
