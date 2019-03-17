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
	print(BOLD + BRED+ "ERROR: " + ENDC + msg)

class Monomial(object):

    def __init__(self, num=None, power=None):
        self.num = num
        self.power = power




def change_sign(equ):


def validate(equ):
	equ = equ.replace(" ", "")
	left_part, right_part = equ.split('=')
	if not re.fullmatch(r'[X.^\d+*-]{1,}=[X.^\d+*-]{1,}', equ):
		msg_error("Incorrect symbol!")
	left_part, right_part = equ.split('=')
	


def find_monomial(equ):
	match_len = 0
	for match in pattern.finditer(equ):
		print(match)
	if len(equ) == len(match_len)


def reduce(equ):
	pass

if __name__ == '__main__':
	if len(argv) != 2:
		msg_error("Argument != 2")
	else:
		validate(argv[1])
