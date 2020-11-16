import random
import os
from time import sleep


print('\t\t*****************************************')
print('\t\t*****         IFECHIGO GAME         *****')
print('\t\t*****************************************')
sleep(1)
os.system('clear')

easy_rand = random.randint(1,9)
mid_rand = random.randint(10,99)
hard_rand = random.randint(100,999)

easy_trial = 3
mid_trial = 5
hard_trial = 10

def home():
	print("Welcome to Ifechigo's Game")
	print('Enter M [M]enu to go to Menu')
	print('Enter S [S]tart to Start Game')
	print('Enter Q [Q]uit to Exit Game\n')

def menu():
	print('\nSelect your Deficulty.\nEnter E [E]asy for Easy')
	print('Enter N [N]ormal for Normal')
	print('Enter H [H]ard for God Level')
	
	print('\nRules: \n1. Only 3 attempts are possible for Easy')
	print('2. Only 5 attempts are possible for Normal')
	print('3. Only 10 attempts are possible for God Level')
	print('4. Enter any number from 1 to 9 for Easy')
	print('5. Enter any number from 10 to 99 for Normal')
	print('6. Enter any number from 100 to 999 for God Level')
	print('\n\nEnter Q [Q]uit to exit or B [B]ack to return')

def exit():
	if entry == 'Q':
		os.system('clear')
		print('\n\t\t\tGoodBye')
		print('\t\tThanks for Visiting')
		exit()

def you_won():
	os.system('clear')
	print('\t\t****You Won****')
	sleep(0.7)
	os.system('clear')
	sleep(0.7)
	print('\t\t****You Won****')
	sleep(0.4)
	os.system('clear')
	sleep(0.4)
	print('\t\t****You Won****')
	sleep(0.1)
	
	
def easy_dificulty():
	print('Great! choice lets getting kicking')
	print('Rules: \n1. Only 3 attempts are possible for Easy')
	print('2. Enter any number from 1 to 9 for Easy')
	sleep(3)
	os.system('clear')
	
	trial = 0
		
	my_choice = None		
	
	while my_choice != easy_rand:
		print(easy_rand)
		my_choice = int(input('Enter number: '))

		if my_choice > easy_rand:
			print('Too high')
		if my_choice < easy_rand:
			print('Too low')
		if easy_trial > trial:
			trial = trial + 1
			re_trial = 3 - trial
			print('you have %d attempt(s) left' %re_trial)
			sleep(1.5)
			os.system('clear')
			if mid_trial == trial & my_choice != easy_rand:
				sleep(1)
				os.system('clear')
				print('\t\tSorry you are out of attempts')
				break
			
		if my_choice == easy_rand:
			you_won()
	
def mid_dificulty():
	print('Great! choice lets getting kicking')
	print('Rules: \n1. Only 5 attempts are possible for Normal')
	print('2. Enter any number from 10 to 99 for Normal')
	sleep(3)
	os.system('clear')
	
	trial = 0
		
	my_choice = None		
	
	while my_choice != mid_rand:
		print(mid_rand)
		my_choice = int(input('Enter number: '))

		if my_choice > mid_rand:
			print('Too high')
		if my_choice < mid_rand:
			print('Too low')
		if mid_trial > trial:
			trial = trial + 1
			re_trial = 5 - trial
			print('you have %d attempt(s) left' %re_trial)
			sleep(1.5)
			os.system('clear')
			if mid_trial == trial & my_choice != mid_rand:
				sleep(1)
				os.system('clear')
				print('\t\tSorry you are out of attempts')
				break
			
		if my_choice == mid_rand:
			you_won()

def hard_dificulty():
	print('Great! choice lets getting kicking')
	print('Rules: \n1. Only 10 attempts are possible for God Level')
	print('2. Enter any number from 100 to 999 for God Level')
	sleep(3)
	os.system('clear')
	
	trial = 0
		
	my_choice = None		
	
	while my_choice != hard_rand:
		print(hard_rand)
		my_choice = int(input('Enter number: '))

		if my_choice > hard_rand:
			print('Too high')
		if my_choice < hard_rand:
			print('Too low')
		if hard_trial > trial:
			trial = trial + 1
			re_trial = 10 - trial
			print('you have %d attempt(s) left' %re_trial)
			sleep(1.5)
			os.system('clear')
			if mid_trial == trial & my_choice != hard_rand:
				sleep(1)
				os.system('clear')
				print('\t\tSorry you are out of attempts')
				break
			
		if my_choice == hard_rand:
			you_won()

home()

entry = input('\nWhat would you like to do?: ').upper()
os.system('clear')
		
exit()		
if entry == 'M':
	os.system('clear')
	menu()
	sleep(10)
	os.system('clear')
	try:
		dificulty_entry = input('Select an option: ').upper()
		exit()
		if dificulty_entry == 'E':
			easy_dificulty()
		if dificulty_entry == 'N':
			mid_dificulty()
		if dificulty_entry == 'H':
			hard_dificulty()
		if dificulty_entry == 'B':
			home()
			sleep(5)
			os.system('clear')
			entry = input('\nWhat would you like to do?: ').upper()
			os.system('clear')
			if entry == 'S':
				mid_dificulty()
			
	except:
		ValueError()

if entry == 'S':
	mid_dificulty()
		



