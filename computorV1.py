import re
from sys import argv

BBLUE = '\033[94m'
BGREEN = '\033[92m'
BRED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

pattern = re.compile(r'((([+-]?)\d+((\.\d+)?)\*)?)X\^\d+')


def msg_error(msg):
    print(BOLD + BRED + "ERROR: " + ENDC + msg)
    exit(1)


def check_degree(dict):
        pass

def validate(equ):
    equ = equ.replace(" ", "")
    if not re.fullmatch(r'[X.^\d+*-]{1,}=[X.^\d+*-]{1,}', equ):
        msg_error("Incorrect symbol!")
    left_part, right_part = equ.split('=')
    dict = {}
    dict = find_monomial(left_part, 'left', dict)
    dict = find_monomial(right_part, 'right', dict)
    check_degree(dict)


def change_sign(coef):
    if coef[0] == '-':
        return(float(coef[1:]))
    else:
        return -float(coef[0:])



def find_monomial(equ, word, list):
    match_len = 0
    sign = 1
    if equ == "0":
        return list
    else:
        for match in pattern.finditer(equ):
            coef, pow = match.group().split("*X^")
            if word == 'right':
                sign = -1
            if pow in list:
                list[pow] = list[pow] + sign * float(coef)
            else:
                list[pow] = sign * float(coef)
            match_len += len(match[0])
    if len(equ) != match_len:
        msg_error("Invalid  " + word + " part of equation")
    print(list)
    return list

def reduce(equ):
    pass


if __name__ == '__main__':
    if len(argv) != 2:
        msg_error("Argument != 2")
    else:
        validate(argv[1])
