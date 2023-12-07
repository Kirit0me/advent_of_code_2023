input = open("aoc_in7.txt", 'r').read().split("\n")

def value_p1(card):
    return "23456789TJQKA".index(card)

def value_p2(card):
    return "J23456789TQKA".index(card)

def score(hand):
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(), reverse=True)

# part 2

def best_score(hand):
    cards="23456789TQKA"
    if 'J' in hand:
        return max([best_score(hand.replace('J', c, 1)) for c in cards])
    return score(hand)

def tiebreak(hand):
    sc_1 = score(hand)
    sc_2 = best_score(hand)
    sc_1.extend([value_p1(x) for x in hand])
    sc_2.extend([value_p2(x) for x in hand])
    # return sc_1
    return sc_2

scored = []
for line in input:
    hand, bid = line.split()
    scored.append((tiebreak(hand), hand, int(bid)))
print(scored)
scored.sort()
print(scored)

acc = 1
total = 0
for g in scored:
    bid = g[2]
    total += acc * bid
    mul += 1

print(total)