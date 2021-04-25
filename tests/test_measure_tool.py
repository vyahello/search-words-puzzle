"""
A test suite contains a set of test cases to measure performance
of search words puzzle engine.
"""
import time
from pathlib import Path
from typing import List, Sequence

import pytest

from puzzle.grids import RandomWordsGrid, Grid
from puzzle.properties import GridSize, LetterCoordinates
from puzzle.tools import start_word_search_puzzle, start_words_search_puzzle
from puzzle.words import HiddenWords, HiddenWord

pytestmark = pytest.mark.unittest
_max_allowed_time: float = 0.5


def real_words() -> Sequence[str]:
    """Loads a list of real words to search."""
    with (Path(__file__).parent / 'words.txt').open() as path:
        return tuple(map(str.strip, path.readlines()))[:5]


@pytest.fixture(scope='module')
def board() -> LetterCoordinates:
    """Creates a random board of letters for a puzzle."""
    with RandomWordsGrid(GridSize(height=50, width=50)) as grid:  # type: Grid
        yield grid.content.to_coordinates()


@pytest.mark.parametrize(
    'word', ('foo', 'foobar', 'foobar', 'foobarlong', 'foobarisatoolongword')
)
def test_measure_word_search(board: LetterCoordinates, word: str) -> None:
    """Test the performance of a single word puzzle search.

    Basically word should be matched within less that 0.5 seconds
    in a 50x50 grid of letters.
    """
    execution_start_time: float = time.time()
    start_word_search_puzzle(HiddenWord(board, word))
    execution_end_time: float = time.time() - execution_start_time
    assert execution_end_time < _max_allowed_time, (
        'Execution time of a puzzle tool exceeds '
        f'maximum allowed "{_max_allowed_time}" time.'
    )


@pytest.mark.parametrize(
    'words',
    (
        ('foo', 'bar'),
        (
            'foo',
            'bar',
            'foobar',
        ),
        (
            'foo',
            'bar',
            'foobar',
            'foobarlong',
        ),
        (
            'foo',
            'bar',
            'foobar',
            'foobarlong',
            'foobarisatoolongword',
        ),
        (
            'foo',
            'bar',
            'foobar',
            'foobarlong',
            'foobarisatoolongword',
            'foobarisasupertoolongword',
        ),
        (
            'foo',
            'bar',
            'foobar',
            'foobarlong',
            'foobarisatoolongword',
            'foobarisasupertoolongword',
            'honestlyfoobarisasupertoolongwordcraaap',
        ),
        real_words(),
    ),
)
def test_measure_words_search(
    board: LetterCoordinates, words: List[str]
) -> None:
    """Test the performance of multiple words puzzle search.

    Basically word should be matched within less that 0.5 seconds
    in a 50x50 grid of letters.
    """
    execution_start_time: float = time.time()
    start_words_search_puzzle(HiddenWords(board, iter(words)))
    execution_end_time: float = time.time() - execution_start_time
    assert execution_end_time < _max_allowed_time, (
        'Execution time of a puzzle tool exceeds '
        f'maximum allowed "{_max_allowed_time}" time.'
    )
