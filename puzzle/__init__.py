"""A package contains a set of interfaces for `search-words-puzzle` app."""
from typing import Tuple

from puzzle.grids import (  # noqa: F401
    Content,
    Grid,
    GridContent,
    RandomWordsGrid,
)
from puzzle.puzzles import SearchPuzzle, SearchWordPuzzle  # noqa: F401
from puzzle.properties import (
    Coordinate,
    GridProperty,
    LetterCoordinates,
    SafePropertyMixin,
)

__author__: str = 'Vladimir Yahello'
__email__: str = 'vyahello@gmail.com'
__license__: str = 'MIT'
__copyright__: str = f'Copyright 2021, {__author__}'
__version__: str = '0.0.1'
__package_name__: str = 'search-words-puzzle'
__all__: Tuple[str, ...] = (
    'Content',
    'Coordinate',
    'Grid',
    'GridContent',
    'GridProperty',
    'LetterCoordinates',
    'SafePropertyMixin',
    'SearchPuzzle',
    'SearchWordPuzzle',
)
