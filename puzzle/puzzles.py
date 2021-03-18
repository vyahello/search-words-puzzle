"""A module contains as set API for all supported puzzles."""
from abc import ABC, abstractmethod
from typing import List, Sequence, Tuple

from loguru import logger as _logger

from puzzle.properties import Coordinate, LetterCoordinates


class SearchPuzzle(ABC):
    """The class represents an abstract interface for a search puzzle."""

    __slots__: Sequence[str] = ()

    @abstractmethod
    async def coordinates(self, item: str) -> List[str]:
        """Return the abstract starting and ending coordinates of a given item.

        Args:
            item: (str) name of an item.

        Returns:
            list: a list of found coordinates.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Return an abstract name of a search puzzle.

        Returns:
            str: a name of a search puzzle.
        """
        pass


class SearchWordPuzzle(SearchPuzzle):
    r"""The class represents a search word puzzle.

    It allows to search a grid of letters (a-z only) for valid English words.

    Words can be found along any diagonal, forwards, upwards, downwards or
    backwards and does not ‘wrap’ between edges.

    The search engine is able to find all words in the following 8 directions:
    ```
     \|/
    - | -
     /|\
    ```
    """

    MOVEMENT_COORDINATES: Tuple[Coordinate, ...] = (
        Coordinate(1, 0),
        Coordinate(0, 1),
        Coordinate(-1, 0),
        Coordinate(0, -1),
        Coordinate(-1, -1),
        Coordinate(1, 1),
        Coordinate(-1, 1),
        Coordinate(1, -1),
    )
    __slots__: Sequence[str] = ('_board',)

    def __init__(self, board: LetterCoordinates) -> None:
        self._board = board

    async def coordinates(self, item: str) -> List[str]:
        """Return all starting and ending coordinates of a given word item.

        Example:
        >>> puzzle = SearchWordPuzzle(board)
        >>> await puzzle.coordinates('foo')
        ['Start at: (X13, Y36); End at: (X11, Y34)', ...]

        Args:
            item: (str) name of an item.

        Returns:
            list: a list of found coordinates of a given word.

        Raises:
            ValueError: if the board of letters is empty.
        """
        if len(self._board) == 0:
            raise ValueError('The board of letters is empty!')
        word_coordinates: List[str] = []
        _logger.info(f'Searching for "{item}" word in a grid of letters ...')
        try:
            for first_coordinate in self._board[item[0]]:  # type: Coordinate
                for (
                    movement_coordinate
                ) in self.MOVEMENT_COORDINATES:  # type: Coordinate
                    row_point, column_point = (
                        first_coordinate.x_axis,
                        first_coordinate.y_axis,
                    )
                    for next_letter in item[1:]:  # type: str
                        row_point, column_point = (
                            row_point + movement_coordinate.x_axis,
                            column_point + movement_coordinate.y_axis,
                        )
                        if (
                            Coordinate(row_point, column_point)
                            not in self._board[next_letter]
                        ):
                            break
                    else:
                        last_coordinate = Coordinate(row_point, column_point)
                        _logger.debug(
                            f'Found "{item}" word at: '
                            f'{first_coordinate}; {last_coordinate}'
                        )
                        word_coordinates.append(
                            f'Start at: {first_coordinate}, '
                            f'End at: {last_coordinate}'
                        )
        except KeyError as error_message:
            _logger.warning(
                f'Cannot find coordinates for "{item}" word as the board '
                f'does not contain "{error_message.args[0]}" letter'
            )
        return word_coordinates

    @property
    def name(self) -> str:
        """Return name of a search word puzzle.

        Returns:
            str: a name of a search puzzle e.g `SearchWordPuzzle`.
        """
        return self.__class__.__name__
