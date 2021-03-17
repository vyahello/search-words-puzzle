"""A module represents an API for the `search-words-puzzle` tool."""
from typing import List

from loguru import logger as _logger

from puzzle.grids import Grid, RandomWordsGrid
from puzzle.properties import GridSize
from puzzle.puzzles import SearchPuzzle, SearchWordPuzzle


def start_words_search_puzzle(grid_size: GridSize, word: str) -> None:
    """Start words search puzzle tool.

    It will generate a random grid of letters and match them with
    the corresponding word.

    Args:
        grid_size: (GridProperty) the size of a grid.
        word: (str) a word to search.
    """
    with RandomWordsGrid(grid_size=grid_size) as grid:  # type: Grid
        puzzle: SearchPuzzle = SearchWordPuzzle(
            board=grid.content.to_coordinates()
        )
        coordinates: List[str] = puzzle.coordinates(word)
        if not coordinates:
            _logger.info(f'"{word}" word is absent in a grid')
        else:
            _logger.info(
                f'Found "{word}" word coordinates in a grid: {coordinates}'
            )
