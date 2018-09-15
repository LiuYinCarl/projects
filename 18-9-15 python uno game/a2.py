from random import shuffle


class Card(object):
    def __init__(self, number, colour):
        """
        initiate Card
        :param number: the number of card
        :param colour: the color of card
        """
        self.number = number
        self.colour = colour
        self.pickup_amount = 0  # pick up amount of this card
        self.skip = False       # If this card is a skip card
        self.reverse = False    # If this card is a reverse card

    def __str__(self):
        return 'Card({},{})'.format(self.number, self.colour)

    def __repr__(self):
        return 'Card({},{})'.format(self.number, self.colour)

    def get_number(self):
        return self.number

    def get_colour(self):
        return self.colour

    def set_number(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            raise TypeError(
                "number is not int Type"
            )

    def set_colour(self, colour):
        if isinstance(colour, str):
            self.colour = colour
        else:
            raise TypeError(
                "colour is not str Type"
            )

    def get_pickup_amount(self):
        return self.pickup_amount

    def matches(self, card):
        """
       Return True if the other card is playable on top of this card,
       otherwise return False
       """
        return (
                self.colour == card.colour or
                self.number == card.number
        )

    def play(self, player, game):
        pass


class SkipCard(Card):
    """
    Initiate SkipCard, make self.skip True
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.skip = True

    def __str__(self):
        return 'SkipCard({},{})'.format(self.number, self.colour)

    def __repr__(self):
        return 'SkipCard({},{})'.format(self.number, self.colour)


class ReverseCard(Card):
    """
    Initiate ReverseCard, make self.reverse True
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.reverse = True

    def __str__(self):
        return 'ReverseCard({},{})'.format(self.number, self.colour)

    def __repr__(self):
        return 'ReverseCard({},{})'.format(self.number, self.colour)


class Pickup2Card(Card):
    """
    Initiate Pickup2Card, make self.pickup_amount = 2
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.pickup_amount = 2

    def __str__(self):
        return 'Pickup2Card({},{})'.format(self.number, self.colour)

    def __repr__(self):
        return 'Pickup2Card({},{})'.format(self.number, self.colour)


class Pickup4Card(Card):
    """
    Initiate Pickup4Card, make self.pickup_amount = 4
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.pickup_amount = 4

    def __str__(self):
        return 'Pickup4Card({},{})'.format(self.number, self.colour)

    def __repr__(self):
        return 'Pickup4Card({},{})'.format(self.number, self.colour)


class Deck(object):

    def __init__(self, cards=[]):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def get_amount(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def pick(self, amount=1):
        if isinstance(amount, int):
            pick_cards = self.cards[-amount:]
            del (self.cards[-amount:])
            pick_cards.reverse()
            return pick_cards
        else:
            raise TypeError(
                "amount is not int Type"
            )

    def add_cards(self, cards):
        if isinstance(cards, Card):
            self.cards.append(cards)
        elif isinstance(cards, tuple) or isinstance(cards, list):
            for card in cards:
                self.cards.append(card)
        else:
            raise TypeError(
                "don't know the type of cards"
            )

    def top(self):
        """
        >>> deck.get_cards()
        [Card(12, red), Pickup2Card(0, red), ReverseCard(0, blue)]
        >>> deck.top()
        ReverseCard(0, blue)
        """
        return self.cards[-1]


class Player(object):

    def __init__(self, name):
        """
        Initiate Player
        :param name: name of Player
        """
        self.name = name
        self.deck = None
        self._win = False

    def get_name(self):
        return self.name

    def get_deck(self):
        self.deck = Deck()
        return self.deck

    def is_playable(self):
        raise NotImplementedError(
            "is_playable to be implemented by subclasses"
        )

    def has_won(self):
        if not len(self.deck.get_cards()):
            self._win = True
        else:
            self._win = False
        return self._win

    def pick_card(self, putdown_pile):
        """
        pick_card(self, putdown_pile: Deck): Selects a card to play from the players current deck.
        :param putdown_pile: a deck
        :return: card to play
        """
        card = putdown_pile.pick()
        if not card:
            return None
        else:
            return card


class HumanPlayer(Player):

    def is_playable(self):
        return True


class ComputerPlayer(Player):

    def is_playable(self):
        return None
