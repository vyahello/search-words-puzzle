"""A module contains as set API for the puzzle grids."""
import string
import random
from abc import ABC, abstractmethod
from types import TracebackType
from typing import Any, List, Optional, Sequence, Type, Union

from loguru import logger as _logger

from puzzle.properties import Coordinate, GridProperty, LetterCoordinates


class Content(ABC):
    """The class represents an abstract content."""

    __slots__: Sequence[str] = ()

    @abstractmethod
    def to_coordinates(self) -> LetterCoordinates:
        """Return the abstract coordinates of a content.

        Returns:
            dict: a collection of abstract letters coordinates.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return an abstract content as a string.

        Returns:
            str: an abstract string content.
        """
        pass


class Grid(ABC):
    """The class represents an abstract interface of a grid.

    Any implementation of this interface allows to close connection:
      - using context manager (**with** statement)
      - automatically when an object will be deleted by garbage collector
      - manually with **__del__**
    """

    __slots__: Sequence[str] = ()

    @property
    @abstractmethod
    def content(self) -> Content:
        """Create a new abstract grid content.

        Returns:
            Content: an abstract grid content.
        """
        pass

    @property
    @abstractmethod
    def height(self) -> int:
        """Specify an abstract grid height.

        Returns:
            int: an abstract grid height e.g `10`.
        """
        pass

    @property
    @abstractmethod
    def width(self) -> int:
        """Specify an abstract grid width.

        Returns:
            int: an abstract grid width e.g `10`.
        """
        pass

    @abstractmethod
    def build(self) -> None:
        """Build an abstract grid."""
        pass

    @abstractmethod
    def refresh(self) -> None:
        """Clear an abstract grid."""
        pass

    @abstractmethod
    def __enter__(self) -> 'Grid':
        """Return runtime connection itself."""
        pass

    @abstractmethod
    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Close connection itself.

        Raise any exception triggered within the runtime context.
        """
        pass

    @classmethod
    def __subclasshook__(cls, other: Any) -> Union[bool, NotImplementedError]:
        """Customize ``issubclass`` builtin function on the ABC level.

        Args:
            other: (any) other class type

        Returns:
            bool: True, False or NotImplemented of subclassing procedure.
        """
        if cls is Grid:
            method_order: Sequence[Any] = other.__mro__
            for method in '__enter__', '__exit__':
                for other_type in method_order:
                    if method in other_type.__dict__:
                        if other_type.__dict__[method] is None:
                            return NotImplemented
                        break
                else:
                    return NotImplemented
            return True
        return NotImplemented


class GridContent(Content):
    """The class represents a grid content."""

    __slots__: Sequence[str] = ('_rows',)

    def __init__(self, rows: List[str]) -> None:
        self._rows = rows

    def to_coordinates(self) -> LetterCoordinates:
        """Return the abstract coordinates of a content.

        Every letter in a grid is able to contain multiple coordinates.

        Example:
        >>> content = GridContent(['a', 'b'])
        >>> content.to_coordinates()
        {'a': [Coordinate(0, 0)], 'b': [Coordinate(1, 0)]}

        Returns:
            dict: a collection of coordinates for letters.
        """
        board: LetterCoordinates = {}
        for row_index, row_value in enumerate(
            str(self).split()
        ):  # type: int, str
            for column_index, column_value in enumerate(
                row_value
            ):  # type: int, str
                if column_value not in board:
                    board[column_value] = []
                board[column_value].append(Coordinate(row_index, column_index))
        return board

    def __str__(self) -> str:
        """Return grid content.

        Returns:
            str: an grid content as string.

        Raises:
            ValueError: if grid rows are empty.
        """
        if len(self._rows) == 0:
            raise ValueError('Cannot build a grid as it contains empty rows')
        content: str = '\n'.join(self._rows)
        _logger.info(f'The following grid of letters is generated\n{content}')
        return content


class RandomWordsGrid(Grid):
    """The class represents randomly created grid of letters.

    Any implementation of this interface allows to close connection:
      - using context manager (**with** statement)
      - automatically when an object will be deleted by garbage collector
      - manually with **__del__**

    Example:
    >>> with RandomWordsGrid(GridProperty(10, 10)) as grid:
    >>>     content = grid.content
    ...
    """

    __slots__: Sequence[str] = ('_property', '_rows')

    def __init__(self, grid_property: GridProperty) -> None:
        self._property = grid_property
        self._rows: List[str] = []

    @property
    def content(self) -> Content:
        """Create a new grid content.

        Returns:
            Content: a grid content.
        """
        return GridContent(self._rows)

    @property
    def height(self) -> int:
        """Specify a grid height.

        Returns:
            int: a grid height e.g `10`.
        """
        return self._property.height

    @property
    def width(self) -> int:
        """Specify a grid width.

        Returns:
            int: an abstract grid width e.g `10`.
        """
        return self._property.width

    def build(self) -> None:
        """Create a grid of randomly created letters (a-z only).

        Raises:
           ValueError: if the size of a grid is invalid.
        """
        _logger.info(f'{self._property} is used')
        if (self.height < 0 or self.width < 0) or (
            not self.height or not self.width
        ):
            raise ValueError(
                'Cannot generate a grid of letters due to '
                f'invalid "{self.height}x{self.width}" grid size. '
                'It should not contain negative or zero values!'
            )
        _logger.info('Generating a grid of random letters ...')
        rows_counter: int = 0
        while rows_counter < self.height:
            next_row: str = ''.join(
                random.choices(
                    population=string.ascii_lowercase,
                    k=self.width,
                )
            )
            self._rows.append(next_row)
            rows_counter += 1

    def refresh(self) -> None:
        """Clear a grid of letters."""
        self._rows = []

    def __enter__(self) -> Grid:
        """Build grid rows of randomly created words.

        Returns:
            Grid: a grid connection.
        """
        self.build()
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Close a grid connection.

        Raise any exception triggered within the runtime context.
        """
        self.refresh()
