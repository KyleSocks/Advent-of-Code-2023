
def main():
    with open('input.txt') as f:
        lines = f.readlines()
        total_points = 0
        cards = {}
        cards_due = 0
        i = 0
        for line in lines:
            i += 1
            points = 0
            doubd = 0
            matched = set()
            #print(line.strip())
            t = line.strip().split(":")
            card_details = t[0].strip().split(" ")
            card_num = i#int(card_details[1])
            if card_num not in cards:
                cards[card_num] = 1
            else:
                cards[card_num] += 1
            t_nums = t[1].strip().split("|")
            our_nums = t_nums[0].strip().split(" ")
            winning_nums = t_nums[1].strip().split(" ")
            for num in our_nums:
                if num in winning_nums and num not in matched:
                    if num == '':
                        continue
                    matched.add(num)
                    if points == 0:
                        points += 1
                    else:
                        #if doubd < 3:
                        points *= 2
                        doubd += 1
            total_points += points
            cards_due += len(matched)
            mult = cards[card_num]
            for j in range(len(matched)):
                new_num = card_num+j+1
                if new_num not in cards:
                    cards[new_num] = mult
                else:
                    cards[new_num] += mult


        print(total_points)
        print(sum(cards.values()))

if __name__ == '__main__':
    main()