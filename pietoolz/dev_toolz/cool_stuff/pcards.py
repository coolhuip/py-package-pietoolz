from __future__ import annotations
import random as r


SUIT_EMOJIS = ['♠', '♥', '♦', '♣']
SUIT_STRS = ['spade', 'spades', 's',
             'heart', 'hearts', 'h',
             'diamond', 'diamonds', 'd',
             'club', 'clubs', 'c'
             ]


class Card:
    """
    Static card generator class.
    """
    _suit: str
    _rank: int
    

    def __init__(self, suit: str, rank: int) -> None:
        """
        >>> c = Card('h', 13)
        >>> c._suit
        '♥'
        >>> c._val
        13
        """
        # Error checks
        if suit.lower() not in SUIT_EMOJIS or SUIT_STRS:
            raise ValueError          #TODO: Program your own Exception class.
        if rank not in range(1, 14):
            raise ValueError          #TODO: Program your own Exception class.
        # Suit
        s = suit[0].lower()
        if s == 's':
            self._suit = '♠'
        elif s == 'h':
            self._suit = '♥'
        elif s == 'd':
            self._suit = '♦'
        elif s == 'c':
            self._suit = '♣'
        # Rank
        self._rank = rank
    

    def get() -> str:
        """
        """
        pass
        
    




class Deck:
    """
    Standard 52 card deck.
    """
    pass


if __name__ == '__main__':
    from doctest import testmod; testmod()
