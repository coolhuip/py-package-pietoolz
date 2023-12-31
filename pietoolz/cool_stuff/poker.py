"""
NOTE: Always start with the client code. Always. Delay the gratification of
      writing code, and the code will be kind to you.

      If you begin your business logic from the fields THEN onto the client
      code, you will run into silly problems that render further efforts void.
    
NOTE: Never make the developer code the business of the client code,
      especially the problematic part of the developer code.
"""
from __future__ import annotations
from typing import Any, Optional, Union
import random as rand

from pietoolz.data_structures.stack import Stack


SUITS_EMJ: tuple = ('♠', '♥', '♦', '♣')
SUITS_STR: tuple = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
VALID_RANKS: tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 255)
RANKS_NO_JOKERS: tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

STANDARD_DECK_EMJ: dict = {'♠': RANKS_NO_JOKERS,
                           '♥': RANKS_NO_JOKERS,
                           '♦': RANKS_NO_JOKERS,
                           '♣': RANKS_NO_JOKERS
                          }

STANDARD_DECK_STR: dict = {'Spades': RANKS_NO_JOKERS,
                           'Hearts': RANKS_NO_JOKERS,
                           'Diamonds': RANKS_NO_JOKERS,
                           'Clubs': RANKS_NO_JOKERS
                          }

VALID_SUITS: tuple = ('s', 'S', 'spades', 'spade', 'Spades', 'Spade',
                      'SPADES', 'SPADE', 'spd', 'SPD',
                      'h', 'H', 'hearts', 'heart', 'Hearts', 'Heart',
                      'HEARTS', 'HEART', 'hrt', 'HRT',
                      'd', 'D', 'diamonds', 'diamond', 'Diamonds', 'Diamond',
                      'DIAMONDS', 'DIAMOND', 'dia', 'DIA',
                      'c', 'C', 'clubs', 'club', 'Clubs', 'clubs'
                      'CLUBS', 'CLUB', 'clb', 'CLB',
                      'j', 'J', 'jok', 'joker', 'Joker', 'JOKER'
                      'j0ker', 'J0ker', 'J0KER', 'j0k', 'J0k','J0K'
                     )

STD_DECK_STR: str = 'Standard 52-Card Deck'


class Card:
    """
    Card object. 54 unique variations of Card can be created:
    - 52 of the standard 52-card deck
    - 2 joker Cards: 1 black, 1 color

    There are no limits as to how many Card() objects of any given variation
    can be instantiated. It is up to the client code to instantiate the correct
    number of each Card variation.

    NOTE: Card objects are not truly unique b/c it's possible to instantiate
    more than one Card that share the same rank and suit, but with different
    instance IDs.

    Use Cases
    ---------
    Maybe you'd like to design code for a poker game. Use this Card class to
    generate the cards that you need for your deck. The combinations of Card
    objects you can instantiate are infinite, limited only by memory space.

    Notes for Client Code
    ---------------------
    This class is designed to be used with instance/static methods only, b/c
    these methods are designed to be extensible for general purposes.

    Representation Invariants
    -------------------------
    - Once instantiated, the instance attributes, <_suit> and <_rank>, cannot
    be changed. In other words, they are immutable.
    - The same applies for a joker card and its color.
    """
    # Class Attribute:
    num_instances: int=0

    # Instance Attributes:
    # --------------------
    # Basic playing-card info
    _rank: str
    _suit: str
    # Card status
    _is_face_up: bool
    _is_joker: bool
    # Misc
    _inst_id: int


    def __init__(self, rank: int, suit: str) -> None:
        """
        Pre-conditions
        --------------
        1. To create a standard number card:
            >>> ace_spades = Card(1, 's')
            >>> ace_spades = Card(1, 'S')
            >>> ace_spades = Card(1, 'spades')
            >>> ace_spades = Card(1, 'Spades')
            >>> ace_spades = Card(1, 'spade')
            >>> ace_spades = Card(1, 'Spade')

        2. To create a standard face card:
            >>> jack_hearts = Card(11, 'h')
            >>> queen_diamonds = Card(12, 'd')
            >>> king_clubs = Card(13, 'c')

        3. To create a black joker card:
            >>> black_joker = Card(0, 'joker')

        4. To create a color joker card:
            >>> color_joker = Card(255, 'joker')

        Exceptions
        ----------
        If the pre-conditions above are NOT satisfied, InvalidArgException
        is raised.
        """
        # Check: Invalid Args
        if suit not in VALID_SUITS:
            raise InvalidArgException
        if rank not in VALID_RANKS:
            raise InvalidArgException
        # Suit: j0ker
        if (c:=suit[0].lower()) == 'j':
            if rank == 0:
                self._rank = 'black'
            elif rank == 255:
                self._rank = 'c0l0r'
            self._suit = 'j0ker'
            self._is_joker = True
        # Suits: Spades, Hearts, Diamonds, Clubs
        else:
            self._is_joker = False
            self._rank = rank
            # Spade
            if c == 's':
                self._suit = 'Spades'
            # Hearts
            elif c == 'h':
                self._suit = 'Hearts'
            # Diamonds
            elif c == 'd':
                self._suit = 'Diamonds'
            # Clubs
            elif c == 'c':
                self._suit = 'Clubs'
        # Housekeeping
        self._is_face_up = False
        self._id = self.num_instances
        self.num_instances += 1
    

    def __str__(self) -> str:
        """
        Return:
            str, representation of this Card.

        Client Code
        -----------
        >>> ace_spades = Card(1, 'spades')
        >>> str(ace_spades)
        '< Ace of Spades >'
        >>> str(Card(7, 'diamond'))
        '< 7 of Diamonds >'
        >>> str(Card(13, 'Hearts'))
        '< King of Hearts >'
        >>> str(Card(0, 'joker'))
        '< black j0ker >'
        >>> str(Card(255, 'Joker'))
        '< c0l0r j0ker >'
        """
        return self.get()
    

    def __repr__(self) -> str:
        return self.get()


    def get_suit(self) -> str:
        return self._suit


    def get_rank(self) -> str:
        return self._rank


    def get(self) -> str:
        """
        Return a str representation of this Card.

        Client Code
        -----------
        >>> ace_spades = Card(1, 'spades')
        >>> ace_spades.get()
        '< Ace of Spades >'
        >>> str(Card(7, 'diamond'))
        '< 7 of Diamonds >'
        >>> Card(13, 'Hearts').get()
        '< King of Hearts >'
        >>> joker1 = Card(0, 'joker')
        >>> joker1.get()
        '< black j0ker >'
        >>> joker2 = Card(255, 'joker')
        >>> joker2.get()
        '< c0l0r j0ker >'
        """
        if self._is_joker:
            return f'< {self._rank} j0ker >'
        if self._rank == 1:
            return f'< Ace of {self._suit} >'
        elif self._rank == 11:
            return f'< Jack of {self._suit} >'
        elif self._rank == 12:
            return f'< Queen of {self._suit} >'
        elif self._rank == 13:
            return f'< King of {self._suit} >'
        return f'< {self._rank} of {self._suit} >'


    def print(self) -> None:
        """
        "Draw" this card in the console output.

        Cilent Code
        -----------
        """
        pass


    @staticmethod
    def help() -> None:
        """
        Print detailed instructions on how to create a Card object.

        How to Use
        ----------
        Uncomment the line of code below:
        >>> # Card.help()
        """
        print("\n\
             TUTORIAL:\n\
+----------------------------------+\n\
| How to instantiate a Card object |\n\
+----------------------------------+\n\n\
Pre-conditions:\n\n\
1. For a standard number card:\n\
    >>> ace_spades = Card(1, 's')\n\
    >>> ace_spades = Card(1, 'S')\n\
    >>> ace_spades = Card(1, 'spades')\n\
    >>> ace_spades = Card(1, 'Spades')\n\
    >>> ace_spades = Card(1, 'spade')\n\
    >>> ace_spades = Card(1, 'Spade')\n\n\
2. For a standard face card:\n\
    >>> jack_hearts = Card(11, 'h')\n\
    >>> queen_diamonds = Card(12, 'd')\n\
    >>> king_clubs = Card(13, 'c')\n\n\
3. For a black joker card:\n\
    >>> black_joker = Card(0, 'joker')\n\n\
4. For a color joker card:\n\
    >>> color_joker = Card(255, 'joker')\n\n\
If the pre-conditions above are NOT satisfied, \
an InvalidArgException is raised.\n\n\
Try again with the correct args.\n".replace("<BLANKLINE>", ""))


class InvalidArgException(Exception):
    def __init__(self) -> None:
        super().__init__("\
To see how to initialize a Card, run 'Card.help()'")


class Deck:
    """
    What the Deck?
    ==============
    Essentially, the Deck object is a Stack representation of Card objects.
    It provides useful methods that can be used to design a number of games
    that involve decks of traditional playing cards, such as go-fish, poker,
    and blackjack.

    Client Code
    -----------
    There are 2 ways to instantiate a Deck:

    1. Suppose: You want to quickly instantiate a standard 52-card deck, plus
    with (or without) joker cards. Do the following:
        >>> deck = Deck()
        >>> deck.get_info()
        {'deck_name': 'Standard 52-Card Deck', 'joker_count': 0, 'cards_remaining': 52}
        >>> deck.draw_card_from_top()
        < King of Clubs >
        >>> deck.draw_card_from_top()
        < Queen of Clubs >
        >>> deck.draw_card_from_top()
        < Jack of Clubs >
        >>> deck.draw_card_from_top()
        < 10 of Clubs >
        >>> # By default, the Deck is NOT shuffled, unless you specify it as shown below:
        >>> unshuffled_deck = Deck(shuffle=True)
        >>> # If you need to include jokers, do the following:
        >>> j_deck = Deck()
        >>>
        # >>> j_deck.summon_joker()  # Now, there is one joker card in j_deck
        # >>> j_deck.summon_joker()  # Now, there are two joker cards in j_deck

    2. Suppose: You want to instantiate your own custom Deck, of any number or
    combinations of Card objects. Do the following:
        >>> # Create Card objects
        >>> ss = Card(7, 's')
        >>> th = Card(3, 'h')
        >>> kd = Card(13, 'd')
        >>> tc = Card(10, 'c')
        >>> bjokr = Card(0, 'joker')
        >>> cjokr = Card(255, 'joker')
        >>> # Create a list of Card objects, in the order you want them stacked in the Deck
        >>> card_list = [ss, th, kd, tc, bjokr, cjokr]  
        >>> # Instantiate Deck
        >>> custom_deck = Deck('cUsToM dEcK', card_list, shuffle=False)
        >>> custom_deck.get_info()
        {'deck_name': 'cUsToM dEcK', 'joker_count': 2, 'cards_remaining': 6}
        >>> custom_deck.draw_card_from_top()
        < 7 of Spades >
        >>> custom_deck.draw_card_from_top()
        < 3 of Hearts >
        >>> custom_deck.draw_card_from_top()
        < King of Diamonds >
        >>> custom_deck.draw_card_from_top()
        < 10 of Clubs >
        >>> custom_deck.draw_card_from_top()
        < black j0ker >
        >>> custom_deck.draw_card_from_top()
        < c0l0r j0ker >
        >>> custom_deck.draw_card_from_top()
    """
    # Private instance attributes
    _deck_info: dict[str, Any]
    _deck_stack: Stack[Card]
    _cards_remaining: int
    # Instance ID
    __inst_id: int=-1
    # Total number of Deck objects instantiated thus far
    __total_count: int=0


    def __init__(self,
                 deck_name: str=STD_DECK_STR,
                 cust_deck: Optional[list[Card]]=None,
                 shuffle=False) -> None:
        """
        Deck() representations are shuffled by default.
        """
        # Set up the Deck info
        self._deck_info = dict()
        self._deck_info.setdefault('deck_name', deck_name)
        self._deck_info.setdefault('joker_count', 0)
        # Create the Deck Stack
        if not cust_deck:
            self._deck_info.setdefault('cards_remaining', 52)
            self._deck_stack = self._gen_std52_deck()
        else:
            self._deck_info.setdefault('cards_remaining', len(cust_deck))
            self._deck_stack = self._gen_cust_deck(cust_deck)
        # To shuffle or not to shuffle is not a question but a boolean.
        if shuffle:
            self.shuffle()
        # Assign instance id and update total object count.
        self.__inst_id += 1
        self.__total_count += 1


    def _gen_std52_deck(self) -> Stack[Card]:
        """
        Generate a Stack that contains 52 unique Card objects, in order.

        Representation (side view)
        --------------------------
        [Top of the Deck]       \n
        '< King of Clubs >'     \n
        '< Queen of Clubs >'    \n
        '< Jack of Clubs >'     \n
        '< 10 of Clubs >'       \n
        '< 9 of Clubs >'        \n
                      :         \n
                      :         \n
                      :         \n
        '< 3 of Spades >'       \n
        '< 2 of Spades >'       \n
        '< Ace of Spades >'     \n
        [Bottom of the Deck]    \n
        """
        stack = Stack()
        for suit, rank_list in STANDARD_DECK_STR.items():
            for rank in rank_list:
                stack.push(Card(rank, suit))
        return stack


    def _gen_cust_deck(self, cust_deck: list[Card]) -> Stack[Card]:
        """
        Generate a Stack that contains an collection of Card objects, in order.
        
        Client Code
        -----------
        >>> # Create Card objects
        >>> ss = Card(7, 's')
        >>> th = Card(3, 'h')
        >>> kd = Card(13, 'd')
        >>> tc = Card(10, 'c')
        >>> bjokr = Card(0, 'joker')
        >>> cjokr = Card(255, 'joker')
        >>> # Create a list of Card objects, in the order you want them stacked in the Deck
        >>> card_list = [ss, th, kd, tc, bjokr, cjokr]  
        >>> # Instantiate Deck
        >>> custom_deck = Deck('cUsToM dEcK', card_list, shuffle=False)
        >>> custom_deck.get_info()
        {'deck_name': 'cUsToM dEcK', 'joker_count': 2, 'cards_remaining': 6}
        >>> custom_deck.draw_card_from_top()
        < 7 of Spades >
        >>> custom_deck.draw_card_from_top()
        < 3 of Hearts >
        >>> custom_deck.draw_card_from_top()
        < King of Diamonds >
        >>> custom_deck.draw_card_from_top()
        < 10 of Clubs >
        >>> custom_deck.draw_card_from_top()
        < black j0ker >
        >>> custom_deck.draw_card_from_top()
        < c0l0r j0ker >
        >>> custom_deck.draw_card_from_top()
        >>>
        """
        stack = Stack()
        for _ in range(len(cust_deck)):
            stack.push(card:=cust_deck.pop())
            if card.get_suit() == 'j0ker':
                self._deck_info['joker_count'] += 1
        return stack


    def shuffle(self) -> None:
        """
        Shuffle the currently-remaining cards in this Deck.
        """
        self._deck_stack.shuffle()


    def draw_card_from_top(self) -> str:
        """
        Refer to class docstring.
        """
        card = self._deck_stack.pop()
        self.__total_count -= 1
        return card


    def get_info(self) -> dict:
        """
        Refer to the class docstring.
        Client Code
        -----------
        >>> card_list = [Card(0, 'joker'), Card(255, 'joker')]
        >>> custom_deck = Deck('cUsToM dEcK', card_list, shuffle=False)
        >>> custom_deck.get_info()
        {'deck_name': 'cUsToM dEcK', 'joker_count': 2, 'cards_remaining': 2}
        """
        return self._deck_info


    def add_joker(self, random=True, black=True) -> None:
        """
        By default, add a j0ker card at a random location of this Deck.
        If <random> is set to False, then put the j0ker card at the top of
        the Deck.

        Color of the j0ker card is, by default, <black>=True.
        To add a colored j0ker instead of a black j0ker, set <black>=False.
        """
        # Which color j0ker?
        if black:
            joker = Card(0, 'joker')
        else:
            joker = Card(255, 'joker')
        # Put where in the Deck?
        if random:
            raise NotImplementedError
        else:
            self._deck_stack.push(joker)


class Poker():
    """
    Poker Hands
    ===========
    Find below all types of hands in Texas hold'em, starting w/ the hand of
    the highest rank. 

    Royal Flush: 10♠ J♠ Q♠ K♠ A♠
    ------------
        - The best possible hand in Texas hold'em: ten, jack, queen, king, ace, all of the same suit

    Straight Flush: 5♥ 6♥ 7♥ 8♥ 9♥
    ---------------
        - Five cards of the same suit in sequential order

    Four of a kind: 3♣ 3♠ 3♦ 3♥ 4♦
    ---------------
        - Any four numerically matching cards

    Full house: J♠ J♥ J♣ K♣ K♦
    -----------
        - Combination of three of a kind and a pair in the same hand

    Flush: 2♦ 4♦ 5♦ 9♦ K♦
    ------
        - Five cards of the same suit, in any order

    Straight: A♦ 2♣ 3♦ 4♠ 5♣
    ---------
        - Five cards of any suit, in sequential order

    Three of a kind: 7♣ 7♦ 7♠ 4♣ 5♦
    ----------------
        - Any three numerically matching cards

    Two pair: 9♦ 9♠ K♦ K♥ 4♣
    ---------
        - Two different pairs in the same hand

    One pair: 10♦ 10♠ 3♠ Q♦ K♣
    ---------
        - Any two numerically matching cards

    High card: K♣ 2♥ 4♦ 8♦ Q♠
    ----------
        - The highest ranked card in your hand with an ace being the highest and two being the lowest

    ===================================

    Summary of Texas Hold'em Poker
    ------------------------------
    Parent class for different variations of the poker game.
        First Betting Round: Players fold, call, or raise in turn.

    Betting Rounds:
        Pre-flop: Initial round described in "Starting."
        Flop: After three community cards are revealed.
        Turn: After fourth community card is revealed.
        River: After fifth community card is revealed.

    Community Cards:
        Flop: First three cards, face up.
        Turn: Fourth card, face up.
        River: Fifth card, face up.

    Combination:
        Use five of seven cards (two private, five community).
        Form best hand: High Card, Pair, Two Pair, etc.

    Winning:
        Best Hand: Highest-ranking hand wins pot.
        Last Player: Remaining player if others fold.
        Tie: Split pot if hands are equal.

    Happy Playing!
    ==============
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
