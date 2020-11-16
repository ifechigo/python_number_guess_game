import random

while True:
	network = input('enter your network: ').lower()
	networks = {"mtn" : 1,  "glo" : 2, "airtel" : 3, "zain" : 3, "etisalat": 4, }
	
	if network not in networks:
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
	
	
	
	
	
	total_cards()
	n = len(cards[network_input_value])
	select = random.randint(0, n - 1)
	card_won = cards[network_input_value][select]
	print(card_won)
	
	rm_card = cards[network_input_value].remove(card_won)
	
	total_cards()
	break
	
