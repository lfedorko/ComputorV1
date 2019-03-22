import re
from sys import argv
from solver import solve

GREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

pattern = re.compile(r'((([+-]?)\d+((\.\d+)?)\*)?)X\^\d+')


def msg_error(msg):
    print(BOLD + BRED + "ERROR: " + ENDC + msg)
    exit(1)


def check_degree(_dict):
    for key, value in _dict.items():
        if -1 < key > 2 and value != 0:
            msg_error(f"Polynomial degree:{key}")
            msg_error("The polynomial degree is stricly greater than 2.")


def show_reduced_form(_dict):
    res = f'{BOLD}Reduced form:{ENDC}'
    for key, value in _dict.items():
        sign = ''
        if value > 0:
            sign = '+'
        if str(value) != '0':
            res += f"{sign} {value} * X ^ {key}"
    print(res + " = 0")


def validate(equ):
    equ = equ.replace(" ", "")
    if not re.fullmatch(r'[X.^\d+*-]{1,}=[X.^\d+*-]{1,}', equ):
        msg_error("Incorrect symbol!")
    left_part, right_part = equ.split('=')
    coef = {0 : 0, 1:0 , 2:0}
    coef = find_monomial(left_part, 'left', coef)
    coef = find_monomial(right_part, 'right', coef)
    coef = dict(sorted(coef.items(), reverse=True))
    show_reduced_form(coef)
    check_degree(coef)
    return coef


def find_monomial(equ, word, list):
    match_len = 0
    sign = 1
    if equ == "0":
        return list
    else:
        for match in pattern.finditer(equ):
            coef, pow = match.group().split("*X^")
            pow = int(pow)
            if word == 'right':
                sign = -1
            if pow in list:
                list[pow] = list[pow] + sign * float(coef)
            else:
                list[pow] = sign * float(coef)
            match_len += len(match[0])
    if len(equ) != match_len:
        msg_error(f"Invalid {word} part of equation")
    print(list)
    return list


def reduce(equ):
    pass


if __name__ == '__main__':
    if len(argv) != 2:
        msg_error("Argument != 2")
    else:
        coef_of_equ = validate(argv[1])
        solve(coef_of_equ[2], coef_of_equ[1], coef_of_equ[0])
