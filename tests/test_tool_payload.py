"""A test suite contains a set of test cases for the puzzle tool."""
from pathlib import Path

import pytest

from puzzle.__main__ import (
    _random_words,
    _validate_puzzle_grid_size,
    _validate_puzzle_word,
    _validate_puzzle_words_path,
)

pytestmark = pytest.mark.unittest
_test_path: Path = Path(__file__).parent / 'words.txt'


@pytest.mark.parametrize(
    'word, grid_size, path',
    (('foo', '1x1', Path('file.txt')), ('bar', '10x10', Path('file.log'))),
)
def test_valid_puzzle_payload(word: str, grid_size: str, path: Path) -> None:
    """Test the puzzle tool is able to handle valid input parameters."""
    _validate_puzzle_grid_size(grid_size)
    _validate_puzzle_word(word)
    _validate_puzzle_words_path(path)


@pytest.mark.parametrize(
    'grid_size',
    ('fooxbar', '', '~-.+-",#@^&%*'),
)
def test_invalid_puzzle_grid_size(grid_size: str) -> None:
    """Test the puzzle tool fails when invalid grid size parameter is passed.

    ValueError should be raised in case of invalid puzzle tool parameter.
    """
    with pytest.raises(ValueError):
        _validate_puzzle_grid_size(grid_size)


@pytest.mark.parametrize(
    'word',
    ('', 'AA', '100', '~-.+-",#@^&%*'),
)
def test_invalid_puzzle_word(word: str) -> None:
    """Test the puzzle tool fails when invalid word parameter is passed.

    ValueError should be raised in case of invalid puzzle tool parameter.
    """
    with pytest.raises(ValueError):
        _validate_puzzle_word(word)


def test_invalid_puzzle_words_path() -> None:
    """Test the puzzle tool fails when invalid words path file
    parameter is passed.

    ValueError should be raised in case of invalid puzzle tool parameter.
    """
    with pytest.raises(ValueError):
        _validate_puzzle_words_path(Path('file.png'))


def test_random_words() -> None:
    """Test the puzzle random words are invoked from a test file of words."""
    expected_amount_words = 3
    actual_amount_words = len(
        tuple(_random_words(_test_path, expected_amount_words))
    )
    assert expected_amount_words == actual_amount_words, (
        f'Expected N words: {expected_amount_words} '
        f'!= Actual N words: {actual_amount_words}'
    )
