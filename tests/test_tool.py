"""A test suite contains a set of test cases for the puzzle tool."""
import pytest

from puzzle.__main__ import _validate_puzzle_parameters

pytestmark = pytest.mark.unittest


@pytest.mark.parametrize('word, grid_size', (('foo', '1x1'), ('bar', '10x10')))
def test_valid_puzzle_parameters(word: str, grid_size: str) -> None:
    """Test the puzzle tool is able to handle valid input parameters."""
    _validate_puzzle_parameters(word, grid_size)


@pytest.mark.parametrize(
    'word, grid_size',
    (
        ('', '1x1'),
        ('AA', '1x1'),
        ('100', '1x1'),
        ('~-.+-",#@^&%*', '1x1'),
        ('foo', 'fooxbar'),
        ('foo', ''),
        ('foo', '~-.+-",#@^&%*'),
    ),
)
def test_invalid_puzzle_parameters(word: str, grid_size: str) -> None:
    """Test the puzzle tool is able to handle invalid input parameters.

    ValueError should be raised in case of invalid puzzle tool parameters.
    """
    with pytest.raises(ValueError):
        _validate_puzzle_parameters(word, grid_size)
