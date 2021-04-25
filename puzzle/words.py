"""A module contains as set API for all words to search."""
from dataclasses import dataclass
from typing import Iterator

from puzzle import LetterCoordinates


@dataclass
class HiddenWord:
    """The class represents a hidden word to search in a board of letters."""

    board: LetterCoordinates
    value: str

    def __str__(self) -> str:
        """Return a hidden word name."""
        return self.value


class HiddenWords(Iterator[HiddenWord]):
    """The class represents hidden words to search in a board of letters."""

    def __init__(self, board: LetterCoordinates, words: Iterator[str]) -> None:
        self._board = board
        self._words = words

    def __iter__(self) -> Iterator[HiddenWord]:
        """Return an iterator itself."""
        return self

    def __next__(self) -> HiddenWord:
        """Return next the initiated word to search."""
        return HiddenWord(self._board, next(self._words))
