"""A module represents an entrypoint for `search-words-puzzle` app."""
import asyncio
import random
import re
import textwrap
from pathlib import Path
from typing import Generator, IO

from typer import Option, run

from puzzle.grids import Grid, RandomWordsGrid
from puzzle.properties import GridSize
from puzzle.tools import start_word_search_puzzle, start_words_search_puzzle


def _validate_puzzle_grid_size(grid_size: str) -> None:
    """Validate puzzle grid size input parameter.

    Args:
        grid_size: (str) the size of a grid.

    Raises:
        ValueError: in case invalid input parameter.
    """
    if not re.findall(string=grid_size, pattern=r'-?\d+x-?\d+'):
        raise ValueError(
            f'Specified "{grid_size}" grid size value is invalid. '
            'It should match "NxN" pattern e e.g "10x10"!.'
        )


def _validate_puzzle_word(word: str) -> None:
    """Validate puzzle custom word input parameter.

    Args:
        word: (str) a word to search.

    Raises:
        ValueError: in case invalid input parameter.
    """
    if not re.findall(string=word, pattern=r'^[a-z]+$'):
        raise ValueError(
            f'Specified "{word}" word value is invalid. It '
            'should match "only lowercase letters" pattern e.g "foo"!.'
        )


def _validate_puzzle_words_path(path: Path) -> None:
    """Validate puzzle words filepath input parameter.

    Args:
        path: (Path) a path to words to search.

    Raises:
        ValueError: in case invalid input parameter.
    """
    if path.suffix not in ('.txt', '.log'):
        raise ValueError(
            f'"{path}" file has invalid suffix ' f'"{path.suffix}"'
        )


def _random_words(path: Path, limit: int = 5) -> Generator[str, None, None]:
    """Read random N words from a text file path.

    Args:
        path: (Path) a path to text file.
        limit: (int) the amount of words to invoke.

    Returns:
        generator: a generator N random words.
    """
    with path.open() as payload:  # type: IO[str]
        words = payload.read().split()
        for _ in range(limit):  # type: int
            yield random.choice(words)


def _tool_chain(
    grid_size: str = Option(
        default='50x50',
        help=textwrap.dedent(
            'The size for a randomly created grid of letters (a-z only).'
        ),
    ),
    words_file_path: Path = Option(
        default=Path('payload/words.txt'),
        help=textwrap.dedent(
            'A path to a custom text file with words to search.'
        ),
    ),
    words_limit: int = Option(
        default=5,
        help=textwrap.dedent('Search N random words from a given text file.'),
    ),
    word: str = Option(
        default='',
        help=textwrap.dedent(
            'A custom word to search in a grid of letters e.g "foo".'
        ),
    ),
) -> None:
    """The tool searches words in a randomly generated grid of letters."""
    grid_height, grid_width = tuple(map(int, grid_size.split('x')))
    _validate_puzzle_grid_size(grid_size)
    with RandomWordsGrid(
        grid_size=GridSize(grid_height, grid_width)
    ) as grid:  # type: Grid
        board = grid.content.to_coordinates()
        if word:
            _validate_puzzle_word(word)
            asyncio.run(start_word_search_puzzle(board, word=word))
        else:
            _validate_puzzle_words_path(words_file_path)
            random_words = _random_words(
                path=words_file_path, limit=words_limit
            )
            asyncio.run(start_words_search_puzzle(board, words=random_words))


def easyrun() -> None:
    """Start the puzzle command line interface tool chain."""
    run(_tool_chain)


if __name__ == '__main__':
    easyrun()
