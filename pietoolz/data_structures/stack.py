"""
How to Implement Code:
----------------------
1. Program a working logic. This makes the code shippable immediately after.
2. Refactor/optimize if necessary.
"""
from __future__ import annotations
from typing import Any, Optional, Union
from collections.abc import Iterable


class Stack:
    """
    The classic Stack object experience, equipped w/ the usual stack type
    methods. You can store any combination of data types within the same
    instance of Stack.

    Client Code
    -----------
    >>> s = Stack()
    >>> s.is_empty()
    True
    >>> s.push(1)
    >>> s.is_empty()
    False
    >>> s.push([2.0, 2.1, 2.2, 2.3])
    >>> s.push('three')
    >>> s.pop()
    'three'
    >>> s.is_empty()
    False
    >>> s.pop()
    [2.0, 2.1, 2.2, 2.3]
    >>> s.pop()
    1
    >>> s.is_empty()
    True
    >>> s.pop()

    Extra Features
    --------------
    1. Shuffle Stack
        >>> s1 = Stack()
        >>> s1.push(1)
        >>> s1.push(2)
        >>> s1.push(3)
        >>> # The line of code below pseudo-randomly shuffles the order of the Stack.
        >>> s1.shuffle()
        >>> # Now, there's only a "33.3% possibility" that s1.pop() will return 3.
    
    Representation Invariants
    -------------------------
    - The number of elements in the Stack cannot be a negative integer.
    I.e., Stack(arg_list).size() will never return a negative integer.
    """
    _stack: list[Any]
    _size: int


    def __init__(self, item: Any=None) -> None:
        """
        Initialize Stack.
        
        Client Code
        -----------
        >>> empty_stack = Stack()
        >>> premade_stack = Stack([1, 2, 3, 'four', 'five', [6.0, 6.1], 7])
        >>> one_element_stack = Stack('bottom element')
        """
        # Initialize an empty Stack
        self._stack = []
        self._size = 0
        # If an <item> is passed
        if item is not None:
            # <item>: list
            if isinstance(item, list):
                self._stack = item
                self._size = len(item)
            # <item>: tuple
            elif isinstance(item, tuple):
                for i in item:
                    self._stack.append(i)
                self._size = len(item)
            # <item>: anything other than Python list or tuple
            else:
                self._stack.append(item)
                self._size += 1


    def push(self, item: Any) -> None:
        """
        Push <item> to the top of the Stack.

        Client Code:
        ------------
        >>> s = Stack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.push(3)
        >>> s.pop()
        3
        >>> s.pop()
        2
        >>> s.pop()
        1
        >>> s.pop()
        """
        self._stack.append(item)
        self._size += 1
    

    def pop(self) -> Any:
        """
        Intro
        -----
        Remove an item from the top of this Stack.

        Return
            Any: The popped (i.e., removed) item from this Stack.

        Client Code:
        ------------
        >>> s = Stack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.push(3)
        >>> s.pop()
        3
        >>> s.pop()
        2
        >>> s.pop()
        1
        >>> s.pop()
        """
        if len(self._stack) == 0:
            return None
        else:
            self._size -= 1
            return self._stack.pop()


    def is_empty(self) -> bool:
        """
        Return True if Stack is empty. Else, return False.
        """
        return len(self._stack) == 0


    def shuffle(self) -> None:
        """
        Randomly shuffle the order of this Stack.
        """
        pass


# class EmptyStackException(Exception):
#     def __init__(self) -> None:
#         super().__init__("\
# EmptyStackException: Trying to pop from an empty Stack.\
#                         ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
