"""

This is a very limited interpreter that can read a file that
contains the following commands:

quit										-Exit the REPL
input var 							-Prompt for and allow the user to enter a value for the variable
print val 							-Print the value val
var gets val 						-Variable var is assigned the value val
var adds val 						-Variable var has the value val added to it
 
WHERE:
var is always a variable name that contains only letters; and
val can be either:
	-A variable name that contains only letters; or
	-A natural number that contains only digits

To test the interpreter a file named 'apples.ad' has been provided.
"""


def checkNamespace(var):
	if var in functions:
		print(var, 'is a reserved keyword.')
		return False
	else:
		return True

def shutdown():
	global run
	print('Goodbye.')
	run = False

def inpt(var):
	if checkNamespace(var):
		global variables
		value = ''
		while value == '':
			print('Enter the value for ', var, ': ', end='', sep='')
			try:
				value = int(input())
				if value >= 0:
					variables[var] = value
				else:
					print('\nPlease enter a natural number.\n')
					value = ''
			except ValueError:
				print('\nPlease enter a natural number.\n')
				value = ''

def prnt(var):
	if checkNamespace(var):
		if var in variables:
			print(var, 'equals', variables[var])
		elif var.isdigit():
			print(int(var))
		else:
			print(var, 'is undefined.')

def gets(var, val):
	if checkNamespace(var) and checkNamespace(val):
		global variables
		if val.isdigit():
			variables[var] = int(val)
		elif val in variables:
			variables[var] = variables[val]
		else:
			print(val, 'is undefined.')

def adds(var, val):
	if checkNamespace(var) and checkNamespace(val):
		global variables
		if val.isdigit():
			variables[var] += int(val)
		elif val in variables:
			variables[var] += variables[val]
		else:
			print(val, 'is undefined.')



functions = {'quit' : shutdown, 'input' : inpt, 'print' : prnt, 'gets' : gets, 'adds' : adds}
variables = {}
run = True


while run == True:
	try:
		filename = input('Script name: ')
		f1 = open(filename)
	except FileNotFoundError:
		print('\nFile with name \'', filename, '\' cannot be located.\n', sep='')
		filename = ''
	except PermissionError:
		print('\nPermission denied.\n')
		filename = ''


	if filename != '':
		line = f1.readline()
		while line != '':

			line = line.split()

			try:
				if len(line) == 0:
					pass
					
				elif len(line) == 1:
					function = line[0]
					functions[function]()

				elif len(line) == 2:
					function = line[0]
					parameter = line[1]
					functions[function](parameter)

				elif len(line) == 3:
					function = line[1]
					parameter1 = line[0]
					parameter2 = line[2]

					if parameter1.isdigit():
						print('Syntax error.')
					else:
						functions[line[1]](parameter1, parameter2)

				else:
					print('Syntax error.')
			except (KeyError, TypeError):
				print('Syntax error.')

			line = f1.readline()
		f1.close()
