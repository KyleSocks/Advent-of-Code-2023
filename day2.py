import sys

bag_max = {'red': 12, 'green': 13, 'blue': 14}

file1 = open('input.txt', 'r')
total_game_count = 0
power_sum = 0
count = 0

while True:
	count += 1
	good_line = 1
	min_count = {'red': 0, 'green': 0, 'blue': 0}


	line = file1.readline()

	if not line:
		break

	line_split = line.split(":")
	game = line_split[0].split(" ")
	game_number = int(game[1])
	print(game_number)

	bags = line_split[1].split(";")
	for bag in bags:
		colors = bag.split(",")
		for color in colors:
			temp = color.strip().split(" ")
			print(temp)
			num = int(temp[0])
			col = temp[1]
			if num > bag_max[col]:
				good_line = 0
			if num > min_count[col]:
				min_count[col] = num

	if good_line == 1:
		total_game_count += game_number

	line_power = int(min_count['red']) * int(min_count['green']) * int(min_count['blue'])
	power_sum += line_power

print("total games number with max bag: ", total_game_count)
print("sum of power of min sets: ", power_sum)