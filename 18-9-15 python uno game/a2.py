#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

from random import shuffle

__author__ = "Your name & student number here"


class Card(object):
    """
    The basic type of colour and number.
    """
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour
        self.pickup_amount = 0
        self.skip = False
        self.reverse = False

    def __str__(self):
        return 'Card({}, {})'.format(self.number, self.colour)

    def __repr__(self):
        return 'Card({}, {})'.format(self.number, self.colour)

    def get_number(self):
        """
        Returns the card number
        """
        return self.number

    def get_colour(self):
        """
        Returns the card colour
        """
        return self.colour

    def set_number(self, number):
        """
        Set the number value of the card
        """
        self.number = number

    def set_colour(self, colour):
        """
        Set the colour of the card
        """
        self.colour = colour

    def get_pickup_amount(self):
        """
        Returns the amount of cards the next player should pickup
        """
        return self.pickup_amount

    def matches(self, card):
        """
        matches(self, card: Card): Determines if the next
        card to be placed on the pile matches this card.
        """
        # select out the special cards
        if self.pickup_amount == 4:
            return True
        elif self.get_colour() == card.get_colour() or self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        """
        Perform a special card action. The base Cards has no special action
        """
        if self.pickup_amount == 2:
            cards = game.pickup_pile.pick(2)
            game.get_turns().peak().get_deck().add_cards(cards)
            # player.deck.add_cards(cards)
        elif self.pickup_amount == 4:
            cards = game.pickup_pile.pick(4)
            game.get_turns().peak().get_deck().add_cards(cards)
        elif self.skip:
            game.skip()
        elif self.reverse:
            game.reverse()


class SkipCard(Card):
    """
    Initiate SkipCard, make self.skip True
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.skip = True

    def __str__(self):
        return 'SkipCard({}, {})'.format(self.number, self.colour)

    def __repr__(self):
        return 'SkipCard({}, {})'.format(self.number, self.colour)


class ReverseCard(Card):
    """
    Initiate ReverseCard, make self.reverse True
    """

    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.reverse = True

    def __str__(self):
        return 'ReverseCard({}, {})'.format(self.number, self.colour)

    def __repr__(self):
        return 'ReverseCard({}, {})'.format(self.number, self.colour)


class Pickup2Card(Card):
    """
    Initiate Pickup2Card, make self.pickup_amount = 2
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.pickup_amount = 2

    def __str__(self):
        return 'Pickup2Card({}, {})'.format(self.number, self.colour)

    def __repr__(self):
        return 'Pickup2Card({}, {})'.format(self.number, self.colour)


class Pickup4Card(Card):
    """
    Initiate Pickup4Card, make self.pickup_amount = 4
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self.pickup_amount = 4

    def __str__(self):
        return 'Pickup4Card({}, {})'.format(self.number, self.colour)

    def __repr__(self):
        return 'Pickup4Card({}, {})'.format(self.number, self.colour)


class Deck(object):
    """
    A collection of ordered Uno cards.
    """
    def __init__(self, starting_cards=None):
        self.cards = []
        if not starting_cards:
            pass
        elif isinstance(starting_cards, list):
            self.cards = starting_cards
        else:
            self.cards.append(starting_cards)

    def get_cards(self):
        """
        Returns a list of cards in the deck.
        """
        return self.cards

    def get_amount(self):
        """
        Returns the amount of cards in a deck.
        """
        return len(self.cards)

    def shuffle(self):
        """
        Shuffle the order of the cards in the deck.
        """
        shuffle(self.cards)

    def pick(self, amount=1):
        """
        Take the first 'amount' of cards off the deck and return them.
        """
        if len(self.cards) >= amount:
            pick_cards = []
            for i in range(amount):
                pick_cards.append(self.cards[-1])
                del(self.cards[-1])
            return pick_cards
        else:
            # don't have enough cards
            return []

    def add_card(self, card):
        """
        Place a list of cards on top of the deck.
        """
        self.cards.append(card)

    def add_cards(self, cards):
        """
        Place a list of cards on top of the deck.
        """
        for card in cards:
            self.cards.append(card)

    def top(self):
        """
        Peaks at the card on top of the deck and
        returns it or None if the deck is empty.
        """
        if len(self.cards) >= 1:
            return self.cards[-1]
        else:
            print("the deck is empty")


class Player(object):
    """
    The base type of player which is not meant to be initiated (i.e. an abstract class)..
    """
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self._win = False

    def get_name(self):
        """
        Returns the name of the player.
        """
        return self.name

    def get_deck(self):
        """
        Returns the players deck of cards.
        """
        return self.deck

    def is_playable(self):
        """
        Returns True iff the players moves aren't automatic.
        """
        raise NotImplementedError(
            "is_playable to be implemented by subclasses"
        )

    def has_won(self):
        """
        Returns True if the player
        has an empty deck and has therefore won.
        """
        if not self.deck.get_amount():
            self._win = True
        else:
            self._win = False
        return self._win

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        """
        raise NotImplementedError(
            "is_playable to be implemented by subclasses"
        )


class HumanPlayer(Player):
    """
    A human player that selects cards to play using the GUI.
    """
    def __init__(self, name):
        super().__init__(name)

    def is_playable(self):
        return True

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        """
        for card in self.deck.get_cards():
            if card.colour == putdown_pile.top().colour and card.number == putdown_pile.top().number:
                return None
        if len(self.deck.get_cards()) > 0:
            for i, card in enumerate(self.deck.get_cards()):
                if card.matches(putdown_pile.top()):
                    need_card = card
                    del self.deck.cards[i]
                    return need_card
        else:
            return None


class ComputerPlayer(Player):
    """
    A computer player that selects cards to play automatically.
    """
    def __init__(self, name):
        super().__init__(name)

    def is_playable(self):
        return False

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        """
        for card in self.deck.get_cards():
            if card.colour == putdown_pile.top().colour and card.number == putdown_pile.top().number:
                return None
        if len(self.deck.get_cards()) > 0:
            for i, card in enumerate(self.deck.get_cards()):
                if card.matches(putdown_pile.top()):
                    need_card = card
                    del self.deck.cards[i]
                    return need_card
        else:
            return None



