"""
A test suite contains a set of test cases to measure performance
of search words puzzle engine.
"""
import time
from typing import List

import pytest

from puzzle.grids import RandomWordsGrid, Grid
from puzzle.properties import GridSize, LetterCoordinates
from puzzle.tools import start_word_search_puzzle
from puzzle.words import HiddenWords, HiddenWord

pytestmark = pytest.mark.unittest
_max_allowed_time: float = 0.5


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
        ('foo', 'foobar'),
        (
            'foo',
            'foobar',
            'foobar',
        ),
        (
            'foo',
            'foobar',
            'foobar',
            'foobarlong',
        ),
        ('foo', 'foobar', 'foobar', 'foobarlong', 'foobarisatoolongword'),
        (
            'foo',
            'foobar',
            'foobar',
            'foobarlong',
            'foobarisatoolongword',
            'foobarisasupertoolongword',
        ),
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
    for word in HiddenWords(board, iter(words)):  # type: HiddenWord
        start_word_search_puzzle(word)
    execution_end_time: float = time.time() - execution_start_time
    assert execution_end_time < _max_allowed_time, (
        'Execution time of a puzzle tool exceeds '
        f'maximum allowed "{_max_allowed_time}" time.'
    )
