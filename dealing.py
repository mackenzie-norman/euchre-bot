import pydealer as pd


def four_hands():
    deck = pd.Deck()

    to_remove = [str(x) for x in range(2, 9)]
    # now deck should be euchre only
    deck.get_list(to_remove)
    print(len(deck.cards))
    deck.shuffle()
    hands = [deck.deal(5) for x in range(4)]
    print(len(deck.cards))
    return hands, deck


hands, deck = four_hands()
trump = deck.deal()
print(trump)
