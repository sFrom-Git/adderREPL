"""

This is a very limited REPL that can take the following commands:

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

print('Welcome to the Adder REPL.')

while run == True:

	line = input('??? ').split()

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
