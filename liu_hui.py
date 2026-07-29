def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Liu-Hui\'s Algorithm for Pi' + Format.end)
    iterations = int(input('Enter the number of iterations: '))
    radius = int(input('Enter the radius of the circle: '))
    length = radius
    n = 6                                                               # hexagon
    for _ in range(iterations):
        m = math.sqrt((length/2) ** 2 + (radius - math.sqrt(radius ** 2 - (length/2) ** 2)) ** 2)
        length = m
        n = n*2
        area = (n/2) * m * radius
    calculated = area / (radius ** 2)
    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")
