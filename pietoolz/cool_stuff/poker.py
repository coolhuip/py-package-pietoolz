"""
NOTE: Always start with the client code. Always. Delay the gratification of
      writing code, and the code will be kind to you.

      If you begin your business logic from the fields THEN onto the client
      code, you will run into silly problems that render further efforts void.
"""
from __future__ import annotations
from typing import Any, Optional, Union
import random as rand


CARD_SUITS_EMJ: tuple = ('♠', '♥', '♦', '♣')
CARD_SUITS_STR: tuple = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
CARD_RANKS: tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

STANDARD_DECK_EMJ: dict = {'♠': CARD_RANKS,
                           '♥': CARD_RANKS,
                           '♦': CARD_RANKS,
                           '♣': CARD_RANKS
                           }

STANDARD_DECK_STR: dict = {'Spades': CARD_RANKS,
                           'Hearts': CARD_RANKS,
                           'Diamonds': CARD_RANKS,
                           'Clubs': CARD_RANKS
                           }

VALID_RANKS: tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 255)
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

STD_DECK_INFO: str = 'Standard 52-Card Deck'


class Card:
    """
    Card object. 54 unique variations of Card can be created:
    - 52 of the standard 52-card dec
    - 2 joker Cards: 1 black, 1 color

    There are no limits as to how many Card() objects of any given variation
    can be instantiated. It is up to the client code to instantiate the correct
    number of each Card variation.

    Use Cases
    ---------
    Maybe you'd like to design code for a poker game. Use the Card class to
    generate the cards that you need.

    Notes for Client Code
    ---------------------
    The methods are designed to be extensible for general purposes. Use them.

    __Dev Representation Invariants
    -------------------------------
    - Once instantiated, a Card object must NOT change the instance attributes
    <suit> or <rank>... Ever.
    - The same applies for a joker card and its color.
    """
    # Class Attribute:
    __num_card_instances: int = 0

    # Instance Attributes:
    # --------------------
    # Basic playing-card info
    _rank: str
    _suit: str
    # Card status
    _is_face_up: bool
    _is_joker: bool
    # Misc
    _id: int


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
        if (rank not in VALID_RANKS) or (suit not in VALID_SUITS):
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
        self._id = self.__num_card_instances
        self.__num_card_instances += 1


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
        #TODO
        """
        pass


    @staticmethod
    def get_some_help(trol=None) -> None:
        """
        Print detailed instructions on how to create a Card object.

        How to Use
        ----------
        Uncomment the line of code below:
        >>> # Card.get_some_help()
        """
        if not trol:
            print(f"\
\n\
             TUTORIAL:\n\
+----------------------------------+\n\
| How to instantiate a Card object |\n\
+----------------------------------+\n\
\n\
Pre-conditions:\n\
\n\
1. For a standard number card:\n\
    >>> ace_spades = Card(1, 's')\n\
    >>> ace_spades = Card(1, 'S')\n\
    >>> ace_spades = Card(1, 'spades')\n\
    >>> ace_spades = Card(1, 'Spades')\n\
    >>> ace_spades = Card(1, 'spade')\n\
    >>> ace_spades = Card(1, 'Spade')\n\
\n\
2. For a standard face card:\n\
    >>> jack_hearts = Card(11, 'h')\n\
    >>> queen_diamonds = Card(12, 'd')\n\
    >>> king_clubs = Card(13, 'c')\n\
\n\
3. For a black joker card:\n\
    >>> black_joker = Card(0, 'joker')\n\
\n\
4. For a color joker card:\n\
    >>> color_joker = Card(255, 'joker')\n\
\n\
If the pre-conditions above are NOT satisfied, an InvalidArgException \
is raised. Try again with the correct args.\n"
             )
        else:
            Card().get_some_help()


class Deck:
    """
    What the Deck?
    ==============
    Essentially, the Deck object is a collection of Card objects. It provides
    useful methods that can be used to design a number of games that involve
    traditional playing cards, such as poker and blackjack.

    Client Code
    -----------
    There are 2 ways to instantiate a Deck:

    1. Suppose: You want to quickly instantiate a standard 52-card deck, plus
    with (or without) joker cards. Do the following:
        >>> my_deck = Deck()
        >>> my_deck.get_info()
        {'type': 'Standard 52-Card Deck', 'num_cards': 52, 'joker_count': 0}
        >>> my_deck.draw_from_top()
        '< Ace of Spades >'
        >>> my_deck.draw_from_top()
        '< Two of Spades >'
        >>> my_deck.draw_from_top()
        '< Three of Spades >'
        >>> # By default, the Deck is shuffled, unless you specify it as shown below:
        >>> my_unshuffled_deck = Deck(shuffle=False)

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
        {'deck_type': 'cUsToM dEcK', 'num_cards': 52, 'joker_count': 2}
        >>> custom_deck.draw_from_top()
        '< c0l0r j0ker >'
        >>> custom_deck.draw_from_top()
        '< black j0ker >'
        >>> custom_deck.draw_from_top()
        '< Ten of Clubs >'
        >>> custom_deck.draw_from_top()
        '< King of Diamonds >'
        >>> custom_deck.draw_from_top()
        '< Three of Hearts >'
        >>> custom_deck.draw_from_top()
        '< Seven of Spades >'
        >>> custom_deck.draw_from_top()
        None
    """
    #TODO: Declare class/instance attributes.


    def __init__(self,
                 deck_name=STD_DECK_INFO,
                 cust_deck=None,
                 shuffle=False) -> None:
        """
        Refer to class docstring.
        """
        raise NotImplementedError

    
    def draw_from_top(self) -> str:
        """
        Refer to class docstring.
        """
        raise NotImplementedError


    def get_info(self) -> dict:
        """
        Refer to the class docstring.
        """
        raise NotImplementedError


class Poker():
    """


    Poker Hands
    ===========
    Find below all types of hands in Texas hold'em, starting from the highest
    rank.

    Royal Flush: 10♠ J♠ Q♠ K♠ A♠
    ------------
        * The best possible hand in Texas hold'em: ten, jack,queen, king, ace, all of the same suit

    Straight Flush: 5♥ 6♥ 7♥ 8♥ 9♥
    ---------------
        * Five cards of the same suit in sequential order

    Four of a kind: 3♣ 3♠ 3♦ 3♥ 4♦
    ---------------
        * Any four numerically matching cards

    Full house: J♠ J♥ J♣ K♣ K♦
    -----------
        * Combination of three of a kind and a pair in the same hand

    Flush: 2♦ 4♦ 5♦ 9♦ K♦
    ------
        * Five cards of the same suit, in any order

    Straight: A♦ 2♣ 3♦ 4♠ 5♣
    ---------
        * Five cards of any suit, in sequential order

    Three of a kind: 7♣ 7♦ 7♠ 4♣ 5♦
    ----------------
        * Any three numerically matching cards

    Two pair: 9♦ 9♠ K♦ K♥ 4♣
    ---------
        * Two different pairs in the same hand

    One pair: 10♦ 10♠ 3♠ Q♦ K♣
    ---------
        * Any two numerically matching cards

    High card: K♣ 2♥ 4♦ 8♦ Q♠
    ----------
        * The highest ranked card in your hand with an ace being the highest and two being the lowest

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

    Hand Rankings (Highest to Lowest):
        Royal Flush
        Straight Flush
        Four of a Kind
        Full House
        Flush
        Straight
        Three of a Kind
        Two Pair
        One Pair
        High Card

    This hierarchy covers the essential rules and structure of Texas Hold'em.
    
    Happy Playing!
    ==============
    """
    pass


class InvalidArgException(Exception):
    def __init__(self) -> None:
        super().__init__("\
\n\n\
+----------------------------------+\n\
| How to instantiate a Card object |\n\
+----------------------------------+\n\
\n\
Pre-conditions:\n\
\n\
1. For a standard number card:\n\
    >>> ace_spades = Card(1, 's')\n\
    >>> ace_spades = Card(1, 'S')\n\
    >>> ace_spades = Card(1, 'spades')\n\
    >>> ace_spades = Card(1, 'Spades')\n\
    >>> ace_spades = Card(1, 'spade')\n\
    >>> ace_spades = Card(1, 'Spade')\n\
\n\
2. For a standard face card:\n\
    >>> jack_hearts = Card(11, 'h')\n\
    >>> queen_diamonds = Card(12, 'd')\n\
    >>> king_clubs = Card(13, 'c')\n\
\n\
3. For a black joker card:\n\
    >>> black_joker = Card(0, 'joker')\n\
\n\
4. For a color joker card:\n\
    >>> color_joker = Card(255, 'joker')\n\
\n\
If the pre-conditions above are NOT satisfied, this InvalidArgException \
is raised. Try again with the correct args.\n\
")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Tests: Edge Cases
    # print(Card(7, 'c').get_some_help())
