import importlib.util
from pathlib import Path

print('Welcome to Pi Approximation Methods')

location = Path(__file__).resolve().parent


def imp_algorithm(module_name):
    module_path = location / f'{module_name}.py'
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f'Unable to load algorithm module: {module_name}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, 'f'):
        module.f()


algorithm_map = {
    1: 'chudnovsky',
    2: 'madhava_leibniz',
    3: 'ramanujan',
    4: 'Madhava',
    5: 'Euler',
    6: 'viete',
    7: 'bbp_formula',
    8: 'Euler_basel',
    9: 'bellard',
    10: 'borwein',
    11: 'gauss_legendre',
    12: 'leibniz',
    13: 'liu_hui',
    14: 'machin',
    15: 'wallis',
    16: 'Plouffe',
    17: 'Nilakantha',
    18: 'continued_fractions',
    19: 'ramanujan_cf',
    20: 'borwein_algo',
    21: 'plouffe_formula',
    22: 'inf_euler',
    23: 'ramanujan_infsum',
    24: 'bel_formula',
    25: 'abraham',
    26: 'newton',
    27: 'nested_radicals',
    28: 'j_mun'
}

while True:
    algorithms = input('''
Choose the method (enter the number), You can also enter several numbers separated by a ',':-
1. Chudnovsky pi approximation
2. Madhava-Leibniz pi approximation
3. Ramanujan-Sato series 
4. Madhava approximation
5. Euler's Approximation
6. Viete's Formula
7. Bailey-Borwein-Plouffe (BBP) Formula
8. Euler's Approach via Basel Problem
9. Bellard's Formula
10. Borwein's Series
11. Gauss-Legendre Algorithm
12. Leibniz Series
13. Liu-Hui's Algorithm
14. Machin-Like Formulae
15. Wallis Product
16. Plouffe Series
17. Nilakantha Series
18. Euler's Continued Fractions Series for Pi
19. Ramanujan's Continued Fractions Series for Pi
20. Borwein's Algorithms
21. Plouffe's Formula
22. Infinite Product Formulae by Euler
23. Infinite Sum Series by Ramanujan
24. Bellard's Formula 2.0
25. Infinite Sum Series of Abraham Sharp
26. Newton's Formula using Geometric Construction
27. Viete's Nested Radicals Formula for Pi
28. J. Munkhammar's Method
    ''')

    for algorithm in algorithms.split(','):
        algorithm = algorithm.strip()
        if algorithm.isdigit():
            algorithm_number = int(algorithm)
            module_name = algorithm_map.get(algorithm_number)
            if module_name is not None:
                imp_algorithm(module_name)
            else:
                print('Invalid algorithm number:', algorithm)
        else:
            print('Invalid algorithm number:', algorithm)

    c = input('Do you want to use another method? (Y/N): ').strip().upper()
    if c == 'N':
        print('Have a nice day!')
        break
