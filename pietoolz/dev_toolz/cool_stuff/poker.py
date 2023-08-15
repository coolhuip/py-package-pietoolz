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
        1. For a standard number card:
            >>> ace_spades = Card(1, 's')
            >>> ace_spades = Card(1, 'S')
            >>> ace_spades = Card(1, 'spades')
            >>> ace_spades = Card(1, 'Spades')
            >>> ace_spades = Card(1, 'spade')
            >>> ace_spades = Card(1, 'Spade')

        2. For a standard face card:
            >>> jack_hearts = Card(11, 'h')
            >>> queen_diamonds = Card(12, 'd')
            >>> king_clubs = Card(13, 'c')

        3. For a black joker card:
            >>> black_joker = Card(0, 'joker')

        4. For a color joker card:
            >>> color_joker = Card(255, 'joker')

        Exceptions
        ----------
        If the pre-conditions above are NOT satisfied, Exceptions are raised.
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
    def print_help() -> None:
        """
        Print the manual on how to instantiate a Card object.
        """
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


class Deck:
    """
    Standard 52-card deck.
    
    Optional Parameter
    ------------------
    jokers=0
        Enter integers 1 or 2, for the number of joker cards to add
        to the 52-card deck.

    Pre-Condition
    -------------
    - 
    
    Client Code
    -----------
    >>> 

    __Dev Representation Invariants
    -------------------------------
    - Inbetween method calls, the instance fields <_ordered_deck> and
      <_unordered_deck> must share the same number of cards remaining in the
      Deck. I.e., the two instance fields are two different representations
      of the current status of the Deck.
    """
    _joker_count: int
    _ordered_deck: list[Card]
    _unordered_deck: dict[str, list[str]]


    def __init__(self, jokers=0) -> None:
        """
        Create a Deck of Cards.
        """
        self._joker_count = jokers
        self._generate_decks()


    def _generate_decks(self):
        """
        Generate both the ordered AND the unordered deck representations.
        """
        pass


    def _update_decks(self):
        """
        Update both the ordered AND the unordered deck representations.
        """
        pass


    def get_joker_count(self) -> int:
        """
        Get the count of joker cards in the deck.

        Returns
        -------
            int: The number of joker cards.
        """
        return self._joker_count


class Poker():
    """
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
"
                        )


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Tests: Edge Cases
    Card(3, 'heaRt')
