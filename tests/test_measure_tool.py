"""
A test suite contains a set of test cases to measure performance
of search words puzzle engine.
"""
import asyncio
import time
from typing import List

import pytest

from puzzle.grids import RandomWordsGrid, Grid
from puzzle.properties import GridSize
from puzzle.puzzles import SearchWordPuzzle

pytestmark = [pytest.mark.unittest, pytest.mark.asyncio]
_max_allowed_time: float = 0.5


@pytest.mark.parametrize(
    'word', ('foo', 'foobar', 'foobar', 'foobarlong', 'foobarisatoolongword')
)
async def test_measure_word_search(word: str) -> None:
    """Test the performance of a single word puzzle search.

    Basically word should be matched within less that 0.5 seconds
    in a 50x50 grid of letters.
    """
    execution_start_time: float = time.time()
    with RandomWordsGrid(GridSize(50, 50)) as grid:  # type: Grid
        puzzle = SearchWordPuzzle(board=grid.content.to_coordinates())
        await puzzle.coordinates(word)
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
async def test_measure_words_search(event_loop, words: List[str]) -> None:
    """Test the performance of multiple words puzzle search.

    Basically word should be matched within less that 0.5 seconds
    in a 50x50 grid of letters.
    """

    async def queue_task(word: str) -> None:
        """Add search word puzzle task into a queue.

        Args:
            word: (str) a word to search in a board of letters.
        """
        with RandomWordsGrid(GridSize(50, 50)) as grid:  # type: Grid
            puzzle = SearchWordPuzzle(board=grid.content.to_coordinates())
            await puzzle.coordinates(word)

    execution_start_time: float = time.time()
    tasks = [event_loop.create_task(queue_task(word)) for word in words]
    await asyncio.gather(*tasks)
    execution_end_time: float = time.time() - execution_start_time
    assert execution_end_time < _max_allowed_time, (
        'Execution time of a puzzle tool exceeds '
        f'maximum allowed "{_max_allowed_time}" time.'
    )
