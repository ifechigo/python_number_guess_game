import random
from os import system, name
from time import sleep
import socket
import os

easy_rand = random.randint(1,9)
mid_rand = random.randint(10,99)
hard_rand = random.randint(100,999)

easy_trial = 3
mid_trial = 5
hard_trial = 10

win_msg = '\t\t****You Won****'

ip_addresses = ['127.0.1.10', '127.0.12.1']

#give an example explanation

def clear():
	#for windows
	if name == 'nt':
		_ = system('cls')
	
	#for mac & linux
	else:
		_ = system('clear')

def home():
	print("Welcome to Ifechigo's Game")
	print('Enter M [M]enu to go to Menu')
	print('Enter S [S]tart to Start Game')
	print('Enter Q [Q]uit to Exit Game\n')

def menu():
	print('\nSelect your Deficulty.\nEnter E [E]asy for Easy')
	print('Enter N [N]ormal for Normal')
	print('Enter H [H]ard for God Level')
	
	sleep(5)
	clear()

	print('\nRules: \n1. Only 3 attempts are possible for Easy')
	print('2. Only 5 attempts are possible for Normal')
	print('3. Only 10 attempts are possible for God Level')
	print('4. Enter any number from 1 to 9 for Easy')
	print('5. Enter any number from 10 to 99 for Normal')
	print('6. Enter any number from 100 to 999 for God Level')
	print('\n\nEnter Q [Q]uit to exit or B [B]ack to return')

def host_details():
	hostname = socket.gethostname()
	ip_address = socket.gethostbyname(hostname)
	
	if ip_address in ip_addresses:
		print('Address found\nThis ip address has been used to claim reward')
	else:
		ip_addresses.append(ip_address)
		print('You are Eligible for the reward')
	
	print(ip_addresses)
	sleep(2)
	clear()

def comment():
	no_of_participant = 0
	no_of_likes = 0

	while True:
		print('Did you like the Game?\nType "Y" or "Yes" if Yes and "Q" or "Quit" if No')
		entry = input('\nType your reply here => ').upper()
			
		if entry == 'Y' or entry == 'YES':
			no_of_likes = no_of_likes + 1
			no_of_participant = no_of_participant + 1
			break
					
		elif entry ==  'QUIT' or entry == 'Q':
			no_of_participant = no_of_participant + 1
			break #exit()
						
		else:
			clear()
			print('***NOTICE: Please enter a valid reply***\n')

	return print(no_of_participant, no_of_likes)

def rewards():
	while True:
		network = input('enter your network: ').lower()
		networks = {"mtn" : 1,  "glo" : 2, "airtel" : 3, "zain" : 3, "etisalat": 4, }
		
		if network not in networks:
			clear()
			print('enter either "MTN", "GLO", "AIRTEL", "ZAIN"\n')
			continue
			
		def total_cards():
			total_cards = []
			n = 1 	+  len(cards)
			for i in range(1,n):
				total = None
				total = len(cards[i])
				total_cards.append(total)
			
			print(f'total available cards are {sum(total_cards)}')
			
		network_input_value = networks[network]
		
		cards = {1: [1112545525, 11168866785, 11174456885, 111758533854], 2: [22248578544, 22278877588, 222709545884, 22212555488], 3: [333121745555, 3331254558098, 333458755481, 33396584858455], 4: [44498522555806, 4441568255548, 4412122585599]}		
		
		clear()
		total_cards()
		n = len(cards[network_input_value])
		select = random.randint(0, n - 1)
		card_won = cards[network_input_value][select]
		print(card_won)
		
		cards[network_input_value].remove(card_won)
		
		total_cards()
		break

def input_error():
	clear()
	print('Not a valid number, Try Again!!')
	sleep(2)
	clear()

def end_game():
	clear()
	print('\n\t\t\tGoodBye')
	print('\t\tThanks for Visiting')
	sleep(3)
	clear()
	exit()

def you_won():
	clear()
	print(win_msg)
	sleep(0.7)
	clear()
	sleep(0.7)
	print(win_msg)
	sleep(0.4)
	clear()
	sleep(0.4)
	print(win_msg)
	sleep(0.1)
	
def easy_dificulty():
	print('Great! choice lets getting kicking')
	print('Rules: \n1. Only 3 attempts are possible for Easy')
	print('2. Enter any number from 1 to 9 for Easy')
	sleep(7)
	clear()
	
	trial = 0
		
	my_choice = None		
	
	while my_choice != easy_rand:
		try:
			my_choice = int(input('Enter number: '))
		except ValueError:
			input_error()
			continue

		if my_choice > easy_rand:
			print('Too high')
		if my_choice < easy_rand:
			print('Too low')
		if easy_trial > trial:
			trial = trial + 1
			re_trial = 3 - trial
			print('you have %d attempt(s) left' %re_trial)
			sleep(1.5)
			clear()
			if mid_trial == trial & my_choice != easy_rand:
				sleep(1)
				clear()
				print('\t\tSorry you are out of attempts')
				sleep(3)
				clear()
				comment()
				end_game()
				
			
		if my_choice == easy_rand:
			you_won()
			host_details()
			rewards()
			sleep(20)
			clear()
			comment()
			end_game()
	
def mid_dificulty():
	print('Great! choice lets getting kicking')
	print('Rules: \n1. Only 5 attempts are possible for Normal')
	print('2. Enter any number from 10 to 99 for Normal')
	sleep(7)
	clear()
	
	trial = 0
		
	my_choice = None		
	
	while my_choice != mid_rand:
		try:
			my_choice = int(input('Enter number: '))
		except ValueError:
			input_error()
			continue

		if my_choice > mid_rand:
			print('Too high')
		if my_choice < mid_rand:
			print('Too low')
		if mid_trial > trial:
			trial = trial + 1
			re_trial = 5 - trial
			print('you have %d attempt(s) left' %re_trial)
			sleep(1.5)
			clear()
			if mid_trial == trial & my_choice != mid_rand:
				sleep(1)
				clear()
				print('\t\tSorry you are out of attempts')
				sleep(3)
				clear()
				comment()
				end_game()
			
		if my_choice == mid_rand:
			you_won()
			host_details()
			rewards()
			sleep(20)
			clear()
			comment()
			end_game()

def hard_dificulty():
	print('Great! choice lets getting kicking')
	print('Rules: \n1. Only 10 attempts are possible for God Level')
	print('2. Enter any number from 100 to 999 for God Level')
	sleep(7)
	clear()
	
	trial = 0
		
	my_choice = None		
	
	while my_choice != hard_rand:
		try:
			my_choice = int(input('Enter number: '))
		except ValueError:
			input_error()
			continue

		if my_choice > hard_rand:
			print('Too high')
		if my_choice < hard_rand:
			print('Too low')
		if hard_trial > trial:
			trial = trial + 1
			re_trial = 10 - trial
			print('you have %d attempt(s) left' %re_trial)
			sleep(1.5)
			clear()
			if mid_trial == trial & my_choice != hard_rand:
				sleep(1)
				clear()
				print('\t\tSorry you are out of attempts')
				sleep(3)
				clear()
				comment()
				end_game()
			
		if my_choice == hard_rand:
			you_won()
			host_details()
			rewards()
			sleep(20)
			clear()
			comment()
			end_game()

sleep(3)
clear()
print('\t\t*****************************************')
print('\t\t*****         IFECHIGO GAME         *****')
print('\t\t*****************************************')
sleep(2)
clear()

home()

while True:
	entry = input('\nWhat would you like to do?: ').upper()

	clear()

	if entry == 'M':
		clear()
		menu()
		sleep(15)
		clear()

		while True:
			dificulty_entry = input('Select a(n) (deficulty) option: ').upper()
				
			if dificulty_entry == 'Q':
				clear()
				end_game()
			elif dificulty_entry == 'E':
				clear()
				easy_dificulty()
				break
			elif dificulty_entry == 'N':
				clear()
				mid_dificulty()
				break
			elif dificulty_entry == 'H':
				clear()
				hard_dificulty()
				break
			elif dificulty_entry == 'B':
				home()
				sleep(5)
				clear()
				entry = input('\nWhat would you like to do?: ').upper()
				clear()
				if entry == 'S':
					mid_dificulty()
			else:
				clear()
			print('***NOTICE: Please enter a valid reply***\n')

	if entry == 'S':
		mid_dificulty()
		break

	if entry == 'Q':
		end_game()

	else:
		print('***NOTICE: Please enter a valid reply***\n')
		home()

