import socket
import os
import time

ip_addresses = [2, 3, 4, 5, 6, '127.0.1.1']

def host_details():
	hostname = socket.gethostname()
	ip_address = socket.gethostbyname(hostname)
	
	if ip_address in ip_addresses:
		print('Address found\nThis ip address has been used to claim reward')
	else:
		ip_addresses.append(ip_address)
		print('You are Eligible for the reward')
	
	print(ip_addresses)
	time.sleep(2)
	os.system('clear')

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
						
		elif entry != 'Y' or entry == 'Q' or entry == 'YES' or entry == 'QUIT':
			os.system('clear')
			print('***NOTICE: Please enter a valid reply***\n')
			continue
	
	return print(no_of_participant, no_of_likes)

host_details()
comment()


