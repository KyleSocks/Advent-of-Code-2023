import copy
class camel_hand:
	def __init__(self, line):
		line = line.split(' ')
		self.hand = line[0]
		self.bet = int(line[1])
		self.originalbet = int(line[1])
		self.strength = self.get_hand_strength()
		self.strength2 = self.get_hand_strength2()
		self.part2 = False

	def startpart2(self):
		self.strength = self.strength2
		self.bet = self.originalbet
		self.part2 = True

	def update_bet(self, mult):
		#print('old ', self.hand, self.bet)
		self.bet *= mult
		#print('new ', self.hand, self.bet)


	def get_hand_strength(self)->int:
		char_count = {}
		for char in self.hand:
		    if get_card_val(char) in char_count:
		        char_count[get_card_val(char)] += 1
		    else:
		        char_count[get_card_val(char)] = 1

		#print(self.hand, len(char_count), max(char_count.values()))

		#THIS IS FINE BECAUSE NO STRAIGHTS IN THIS PROBLEM
		if len(char_count) == 1:
			#five of a kind
			return 7
		if len(char_count) == 2:
			if max(char_count.values()) == 3:
				#full house
				return 5
			if max(char_count.values()) == 4:
				#four of a kind
				return 6
		if len(char_count) == 3:
			if list(char_count.values()).count(2) == 2:
				return 3
			return 4
		if len(char_count) == 4:
			return 2
		return 1

	def get_hand_strength2(self)->int:
		char_count = {}
		for char in self.hand:
		    if get_card_val2(char) in char_count:
		        char_count[get_card_val2(char)] += 1
		    else:
		        char_count[get_card_val2(char)] = 1

		max_count = len(char_count) 
		max_val = max(char_count.values())
		hand_no_js = char_count.copy()

		if 1 in char_count.keys():
			hand_no_js.pop(1)
			if len(hand_no_js) == 0:
				max_val = 5
			else:
				max_count -= 1
				max_val = max(hand_no_js.values()) + char_count[1]

		if max_count == 0:
			#all wild
			return 7
		if max_count == 1:
			#five of a kind
			return 7
		if max_count == 2:
			if max_val == 3:
				#full house
				return 5
			if max_val == 4:
				#four of a kind
				return 6
		if max_count == 3:
			if max_val == 2:
				return 3
			return 4
		if max_count == 4:
			return 2
		return 1


	def __lt__(self, other):
		if self.strength == other.strength:
			for i in range(5):
				if self.hand[i] != other.hand[i]:
					if not self.part2:
						return get_card_val(self.hand[i]) < get_card_val(other.hand[i])
					else:
						return get_card_val2(self.hand[i]) < get_card_val2(other.hand[i])
			return False
		return get_card_val(self.strength) < get_card_val(other.strength)


def get_card_val(card)->int:
	if card == 'T':
		return 10
	if card == 'J':
		return 11
	if card == 'Q':
		return 12
	if card == 'K':
		return 13
	if card == 'A':
		return 14
	return int(card)

def get_card_val2(card)->int:
	if card == 'T':
		return 10
	if card == 'J':
		return 1
	if card == 'Q':
		return 12
	if card == 'K':
		return 13
	if card == 'A':
		return 14
	return int(card)


def main():
    file = open('input.txt').read().strip()
    lines = file.split('\n')
    hands = [camel_hand(line) for line in lines]
    i = 0
    total_winnings = 0
    for hand in sorted(hands):
    	i += 1
    	hand.update_bet(i)
    	total_winnings += hand.bet
    	#print(i, hand.hand, hand.strength)
    bets = [x.bet for x in hands]
    print('part 1 ',sum(bets))

    total_winnings = 0
    i = 0
    for hand in hands:
    	hand.startpart2()
    for hand in sorted(hands):
    	i += 1
    	hand.update_bet(i)
    	total_winnings += hand.bet
    bets2 = [x.bet for x in hands]
    print('part 2 ', sum(bets2))
    return 0

if __name__ =='__main__':
    main()