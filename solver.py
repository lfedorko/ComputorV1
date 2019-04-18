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
        exp = 'There is no solution!'
    output_result(0, exp)


def solve_linear(b, c):
    res = -c / b
    exp = f"X = - c / b = ({-c} / {b}) = {res}\n"
    output_result(1, res, solve=exp)


def solve_quadratic(a, b, c):
    D = b * b - 4 * a * c
    exp = f'D = b * b - 4 * a * c = {b} * {b} - 4 * {a} * {c} = {D}'
    if D > 0:
        x1 = (-b + (D ** .5)) / (2 * a)
        x2 = (-b - (D ** .5)) / (2 * a)
        exp += ', D > 0, two real roots\n'
        exp += f'X1 = (-b + D ^ 1/2) / 2 * a = {-b} - {D ** .5} / {2 * a} = {x1}\n' \
            f'X2 = (-b + D ^ 1/2) / 2 * a = {-b} + {D ** .5} / {2 * a} = {x2}\n'
        res = f'{x1}, {x2}'
    elif D == 0:
        res = -b / (2 * a)
        exp += f', D = 0, one real root\nX = -b / 2 * a = {-b} / 2 * {a} = {res}\n'
    else:
        real = (-b) / (2 * a)
        print(b/(2*a))
        print(f'a = {a} b={b / (2 * a)} c={c}')
        im = ((4 * a * c - b * b) ** 0.5) / (2 * a)
        exp += f', D < 0, two imaginary roots\nX1 = -b / 2 * a ± (((4 * a * c - b * b) ^ 0.5) / 2) * i =  {real} ± {im}i\n'
        res = f'{real} + {im}i, {real} - {im}i'
    output_result(2, res, solve=exp)


def output_result(degree, res, solve=''):
    print(f'{BOLD}Polynomial degree: {ENDC} {degree}\n{solve}{BOLD}The solution is: {ENDC}\n{res}')
