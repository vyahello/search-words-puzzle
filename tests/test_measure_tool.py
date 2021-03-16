"""
A test suite contains a set of test cases to measure performance
of search words puzzle engine.
"""
import time

import pytest

from puzzle.grids import RandomWordsGrid, Grid
from puzzle.properties import GridProperty
from puzzle.puzzles import SearchWordPuzzle

pytestmark = pytest.mark.unittest


@pytest.mark.parametrize(
    'word', ('foo', 'foobar', 'foobar', 'foobarlong', 'foobarisatoolongword')
)
def test_measure_word_search(word: str) -> None:
    """Test the time execution for a puzzle tool.

    Basically word should be matched within less that 0.5 seconds
    in a 50x50 grid of letters.
    """
    max_allowed_time: float = 0.5
    execution_start_time: float = time.time()
    with RandomWordsGrid(GridProperty(50, 50)) as grid:  # type: Grid
        puzzle = SearchWordPuzzle(board=grid.content.to_coordinates())
        puzzle.coordinates(word)
        execution_end_time: float = time.time() - execution_start_time
        assert execution_end_time < max_allowed_time, (
            'Execution time of a puzzle tool exceeds '
            f'maximum allowed "{max_allowed_time}" time.'
        )
