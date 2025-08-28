import pydealer as pd

euchre_ranks = {
    "values": {
        "Jack": 13,
        "Ace": 12,
        "King": 11,
        "Queen": 10,
        "10": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }
}


def four_hands():
    deck = pd.Deck(ranks=euchre_ranks)

    to_remove = [str(x) for x in range(2, 9)]
    # now deck should be euchre only
    deck.get_list(to_remove)
    print(len(deck.cards))
    deck.shuffle()
    hands = [deck.deal(5) for x in range(4)]
    print(len(deck.cards))
    return hands, deck


def get_inverse(suit):
    if suit == "Spades":
        return "Clubs"
    if suit == "Clubs":
        return "Spades"
    if suit == "Hearts":
        return "Diamonds"
    if suit == "Diamonds":
        return "Hearts"


def beats(card_a, card_b, trump=None):
    print(f"You: {card_a} Them: {card_b}")
    if trump:
        if card_a.suit == trump:
            if card_b.suit == trump:
                # special check for left bower
                return card_a >= card_b
            elif card_b.suit == get_inverse(trump):
                return card_b.value != "Jack" or card_a.value == "Jack"
            else:
                return True
        else:
            if card_b.suit != trump:
                return card_a > card_b

    else:
        if card_a.suit == card_b.suit:
            return card_a > card_b
        return True


# calculate a cards chance of winning
def chance_to_win(cards, card, trump=None):
    deck = pd.Deck()

    to_remove = [str(x) for x in range(2, 9)]
    # now deck should be euchre only
    deck.get_list(to_remove)
    deck.get_list([str(c) for c in cards])
    possible_cards = deck
    chance = 0
    for possible in possible_cards:
        if beats(card, possible, trump):
            print("Beat")
            chance += 1
    return chance / len(possible_cards)


cards_seen = pd.Stack()
hands, deck = four_hands()
trump = deck.deal()
# print(trump)

hand1 = hands[0]
# print(hand1)
print(hand1[0])
print(chance_to_win(hand1, hand1[0], "Spades"))
