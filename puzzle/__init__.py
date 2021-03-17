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
    GridSize,
    LetterCoordinates,
    SafePropertyMixin,
)
from puzzle.tools import start_words_search_puzzle


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
    'GridSize',
    'LetterCoordinates',
    'SafePropertyMixin',
    'SearchPuzzle',
    'SearchWordPuzzle',
    'start_words_search_puzzle',
)
