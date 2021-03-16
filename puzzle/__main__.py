"""A module represents an entrypoint for `search-words-puzzle` app."""
import textwrap
import re
from typing import List

from loguru import logger as _logger
from typer import Option, run

from puzzle.grids import Grid, RandomWordsGrid
from puzzle.properties import GridProperty
from puzzle.puzzles import SearchPuzzle, SearchWordPuzzle


def _validate_puzzle_parameters(word: str, grid_size: str) -> None:
    """Validate puzzle tool input parameters.

    Args:
        word: (str) a word to search.
        grid_size: (str) the size of a grid.

    Raises:
        ValueError: in case invalid input parameters.
    """
    if not re.findall(string=word, pattern=r'^[a-z]+$'):
        raise ValueError(
            f'Specified "{word}" word value is invalid. It '
            'should match "only lowercase letters" pattern e.g "foo"!.'
        )
    if not re.findall(string=grid_size, pattern=r'-?\d+x-?\d+'):
        raise ValueError(
            f'Specified "{grid_size}" grid size value is invalid. '
            'It should match "NxN" pattern e e.g "10x10"!.'
        )


def _tool_chain(
    grid_size: str = Option(
        ...,
        '--grid-size',
        '-s',
        help=textwrap.dedent(
            'The size for a randomly created grid of letters (a-z only)'
        ),
    ),
    word: str = Option(
        ...,
        '--word',
        '-w',
        help=textwrap.dedent('A word to search in a grid of letters.'),
    ),
) -> None:
    """The tool searches words in a randomly generated grid of letters."""
    _validate_puzzle_parameters(word, grid_size)
    grid_height, grid_width = tuple(map(int, grid_size.split('x')))
    with RandomWordsGrid(
        grid_property=GridProperty(grid_height, grid_width)
    ) as grid:  # type: Grid
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


def easyrun() -> None:
    """Start the puzzle command line interface tool chain."""
    run(_tool_chain)


if __name__ == '__main__':
    easyrun()