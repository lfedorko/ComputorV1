import re
from sys import argv
from solver import solve

GREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'


def msg_error(msg):
    print(BOLD + BRED + "ERROR: " + ENDC + msg)
    exit(1)


def find_monomial(equ, word, list_of_coef):
    pattern = r'((^(\+|-)?(\d+((\.\d+)?)\*)?((X|x)(\^\d+)?))(\+|\-|$))'
    pattern_for_digit = r'(^((\+|-)?\d+((\.\d+)*))(\+|-|$))'
    while len(equ) > 0:
        if re.match(pattern, equ):
            size = re.match(pattern, equ)
            monomial_len = re.match(pattern, equ).group(2)
            equ = equ[len(monomial_len):]
            if size.group(3) and size.group(3) == '-':
                mon_sign = -1
            else:
                mon_sign = 1
            if size.group(7):
                if size.group(9):
                    pow = int(size.group(9)[1:])
                else:
                    pow = 1
            if size.group(4):
                coef = mon_sign * float(size.group(4)[:-1])
            else:
                coef = mon_sign * 1
        elif re.match(pattern_for_digit, equ):
            size = re.match(pattern_for_digit, equ)
            monomial_len = size.group(2)
            pow = 0
            if size.group(2):
                coef = float(size.group(2))
            equ = equ[len(monomial_len):]
        else:
            msg_error(f"Invalid {word} part of equation")
        if word == 'right':
            sign = -1
        else:
            sign = 1
        if pow in list_of_coef:
            list_of_coef[pow] = list_of_coef[pow] + sign * coef
        else:
            list_of_coef[pow] = sign * coef
    return list_of_coef


def check_degree(_dict):
    for key, value in _dict.items():
        if -1 < key > 2 and value != 0:
            msg_error(f"Polynomial degree:{key}")
            msg_error("The polynomial degree is greater than 2.")


def show_reduced_form(_dict):
    res = ''
    for key, value in _dict.items():
        sign = ''
        if value > 0:
            sign = '+'
        if value != 0:
            res += f" {sign} {value} * X ^ {key}"
    if not res:
        res = "0"
    print(f'{BOLD}Reduced form:{ENDC} {res} = 0')


def validate(equ):
    equ = equ.replace(" ", "")
    if not re.fullmatch(r'[Xx.^\d+*-]{1,}=[Xx.^\d+*-]{1,}', equ):
        msg_error("Incorrect symbol!")
    left_part, right_part = equ.split('=')
    coef = {0 : 0, 1 : 0, 2: 0}
    coef = find_monomial(left_part, 'left', coef)
    coef = find_monomial(right_part, 'right', coef)
    coef = dict(sorted(coef.items(), reverse=True))
    show_reduced_form(coef)
    check_degree(coef)
    return coef


if __name__ == '__main__':
    graphics = False
    if len(argv) < 2:
        msg_error("Argument < 2")
    else:
        for i in range(1, len(argv)):
            if '-g' in argv[i]:
                graphics = True
            else:
                print(BOLD + GREEN + "THE EQUATION #" + str(i) + ENDC)
                coef_of_equ = validate(argv[i])
                solve(coef_of_equ[2], coef_of_equ[1], coef_of_equ[0], graphics)

