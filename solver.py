BBLUE = '\033[94m'
GREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def solve(a, b, c):
    if a == 0 and b == 0:
        solve_zero(c)
    elif a == 0:
        solve_linear(b, c)
    else:
        solve_quadratic(a, b, c)


def solve_zero(c):
    if c == 0:
        exp = 'True for all X'
    else:
        exp = 'X = 0'
    output_result(0, '', exp)


def solve_linear(b, c):
    res = -c / b
    exp = f"x = - c / b = ({-c} / {b}) = " + str(res)
    output_result(1, res, solve=exp)


def solve_quadratic(a, b, c):
    D = b * b - 4 * a * c
    exp = f'D = b * b - 4 * a * c = {b} * {b} - 4 * {a} * {c} = {D}'
    if D > 0:
        x1 = (-b + (D ** .5)) / (2 * a * c)
        x2 = (-b - (D ** .5)) / (2 * a * c)
        exp += ', D > 0, two real roots'
        res = f'{x1}, {x2}'
    elif D == 0:
        res = -b / 2 * a
        exp += f', D = 0, one real root\nX = -b / 2 * a = {-b} / 2 * {a} = {res}'
    else:
        real = -b / 2 * a
        im = ((4 * a * c - b * b) ** 0.5) / 2 * a
        exp += f', D < 0, two imaginary roots\nX1 = -b / 2 * a ± (((4 * a * c - b * b) ^ 0.5) / 2) * i =  {real} ± {im}i'
        res = f'{real} + {im}i, {real} - {im}i'
    output_result(2, res, solve=exp)


def output_result(degree, res, solve=''):
    print(f'{BOLD}Polynomial degree: {degree}{ENDC}\n{solve}\n{BOLD}The solution is: {ENDC}\n{res}')
