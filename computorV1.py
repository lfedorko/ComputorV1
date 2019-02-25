import re
from sys import argv


# \d+

# s = r''
# re.compile()
# print(re.compi==())


def validate(equ):
	equ = equ.replace(" ", "")

if __name__ == '__main__':
	if len(argv) != 2:
		print("Uncorrect amount of arguments!")
	else:
		validate(argv[1])
