import sys

while True:
	try:
		choice = int(input('Enter number: '))
	except ValueError:
		print('not a number')
		continue
		

	number = 0
	for i in range(1,100):
		number = i
	if choice != number:
		print('Enter a valid number!!')
	if choice > 10:
		print('good')