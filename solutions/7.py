import re
from operator import itemgetter
from collections import Counter

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

with open("inputs/7.txt", "r") as f:
    lines = f.read()

# lines = test_input
lines = lines.split("\n")

print("---- DAY 7 PART 1 ----")

card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hand_order = ["5oak", "4oak", "fullhouse", "3oak", "2pair", "1pair", "highcard"]

bids = {}
hands_by_type = {k: [] for k in hand_order}

for line in lines:
    hand, bid = line.split(" ")
    bid = int(bid)
    bids[hand] = bid
    cards = Counter(hand)
    card_vals = sorted(cards.values())
    key = None
    if card_vals == [5]:
        key = "5oak"
    elif card_vals == [1, 4]:
        key = "4oak"
    elif card_vals == [2, 3]:
        key = "fullhouse"
    elif card_vals == [1, 1, 3]:
        key = "3oak"
    elif card_vals == [1, 2, 2]:
        key = "2pair"
    elif card_vals == [1, 1, 1, 2]:
        key = "1pair"
    else:
        key = "highcard"
    hands_by_type[key] += [hand]

ordered_hands = []


def card_value_getter(val):
    return tuple(card_order.index(c) for c in val)


for k, v in sorted(hands_by_type.items(), key=lambda a: hand_order.index(a[0])):
    ordered_hands = sorted(v, key=card_value_getter, reverse=True) + ordered_hands

total = 0

for i, v in enumerate(ordered_hands):
    total += bids[v] * (i + 1)

print(total)

print("---- DAY 7 PART 2 ----")

card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hand_order = ["5oak", "4oak", "fullhouse", "3oak", "2pair", "1pair", "highcard"]

bids = {}
hands_by_type = {k: [] for k in hand_order}

for line in lines:
    hand, bid = line.split(" ")
    bid = int(bid)
    bids[hand] = bid
    actual_key = 'highcard'
    for replace_card in card_order[:-1]:
        cards = Counter(hand.replace('J', replace_card))
        card_vals = sorted(cards.values())
        key = None
        if card_vals == [5]:
            key = "5oak"
        elif card_vals == [1, 4]:
            key = "4oak"
        elif card_vals == [2, 3]:
            key = "fullhouse"
        elif card_vals == [1, 1, 3]:
            key = "3oak"
        elif card_vals == [1, 2, 2]:
            key = "2pair"
        elif card_vals == [1, 1, 1, 2]:
            key = "1pair"
        else:
            key = "highcard"
        if hand_order.index(key) < hand_order.index(actual_key):
            actual_key = key
    # print(hand, actual_key)
    hands_by_type[actual_key] += [hand]

ordered_hands = []


def card_value_getter(val):
    x = tuple(card_order.index(c) for c in val)
    # print(val, x)
    return x


for k, v in sorted(hands_by_type.items(), key=lambda a: hand_order.index(a[0])):
    ordered_hands = sorted(v, key=card_value_getter, reverse=True) + ordered_hands

# print(ordered_hands)
total = 0

for i, v in enumerate(ordered_hands):
    # print(v, i + 1, bids[v], bids[v] * (i + 1))
    total += bids[v] * (i + 1)

print(total)
