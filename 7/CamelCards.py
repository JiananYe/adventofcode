
order = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

class Hand:
    rank = 0
    sec_rank = 0
    bid = 0
    hand = ""
    def __init__(self, hand:str, bid:int):
        self.hand = hand
        self.bid = int(bid)
    
    def set_ranks(self, ranks:(int, int)):
        self.rank = ranks[0]
        self.sec_rank = ranks[1]

    def __str__(self):
        return self.hand + " " + str(self.bid) + " " + str(self.rank) + " " + str(self.sec_rank)

def load_hands(filename:str) -> list():
    f = open(filename, "r")
    lines = f.readlines()
    hands = []
    for line in lines:
        line = line.strip()
        hand = line.split(" ")
        hands.append(Hand(hand[0], hand[1]))
    f.close()
    return hands

def get_rank(hand:str) -> (int, int):
    counts = list(map(lambda x : hand.count(x), set(hand)))
    counts.sort(reverse=True)
    return (counts[0], counts[1] if len(counts) > 1 else 0)

def sort_hands(hands:list[Hand]) -> list[Hand]:
    return sorted(hands, key=lambda hand: (hand.rank, hand.sec_rank, order.get(hand.hand[0]), order.get(hand.hand[1]), order.get(hand.hand[2]), order.get(hand.hand[3]), order.get(hand.hand[4])))

def calc_total(hands:list[Hand]) -> int:
    total = 0
    for index, hand in enumerate(hands):
        total += hand.bid * (index + 1)
    return total

def main():
    hands = load_hands("hands.txt")
    for hand in hands:
        hand.set_ranks(get_rank(hand.hand))
    hands_sorted = sort_hands(hands)
    for index, hand in enumerate(hands_sorted):
        print(hand, index)
        # if (hand.sec_rank == 2):
        #     print(hand, index)
    print(calc_total(hands_sorted))

main()
