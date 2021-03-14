"""A test suite contains a set of test cases for the puzzles interfaces."""
from typing import List

import pytest

from puzzle.properties import Coordinate, LetterCoordinates
from puzzle.puzzles import SearchWordPuzzle

pytestmark = pytest.mark.unittest

_board_of_letters: LetterCoordinates = {
    'm': [
        Coordinate(x_axis=0, y_axis=0),
        Coordinate(x_axis=0, y_axis=4),
        Coordinate(x_axis=1, y_axis=5),
        Coordinate(x_axis=1, y_axis=9),
        Coordinate(x_axis=2, y_axis=6),
        Coordinate(x_axis=3, y_axis=5),
        Coordinate(x_axis=3, y_axis=13),
    ],
    'y': [
        Coordinate(x_axis=0, y_axis=1),
        Coordinate(x_axis=1, y_axis=6),
        Coordinate(x_axis=3, y_axis=6),
    ],
    'n': [
        Coordinate(x_axis=0, y_axis=2),
        Coordinate(x_axis=1, y_axis=7),
        Coordinate(x_axis=2, y_axis=4),
        Coordinate(x_axis=3, y_axis=11),
    ],
    'a': [
        Coordinate(x_axis=0, y_axis=3),
        Coordinate(x_axis=1, y_axis=8),
        Coordinate(x_axis=2, y_axis=1),
        Coordinate(x_axis=2, y_axis=5),
        Coordinate(x_axis=2, y_axis=11),
        Coordinate(x_axis=3, y_axis=1),
        Coordinate(x_axis=3, y_axis=8),
        Coordinate(x_axis=3, y_axis=12),
    ],
    'e': [
        Coordinate(x_axis=0, y_axis=5),
        Coordinate(x_axis=1, y_axis=10),
        Coordinate(x_axis=2, y_axis=7),
        Coordinate(x_axis=3, y_axis=14),
    ],
    'i': [
        Coordinate(x_axis=0, y_axis=6),
        Coordinate(x_axis=1, y_axis=3),
        Coordinate(x_axis=2, y_axis=8),
        Coordinate(x_axis=3, y_axis=3),
    ],
    's': [
        Coordinate(x_axis=0, y_axis=7),
        Coordinate(x_axis=1, y_axis=4),
        Coordinate(x_axis=2, y_axis=2),
        Coordinate(x_axis=2, y_axis=9),
        Coordinate(x_axis=3, y_axis=4),
        Coordinate(x_axis=3, y_axis=9),
    ],
    'f': [Coordinate(x_axis=0, y_axis=8), Coordinate(x_axis=1, y_axis=0)],
    'o': [
        Coordinate(x_axis=0, y_axis=9),
        Coordinate(x_axis=0, y_axis=10),
        Coordinate(x_axis=1, y_axis=1),
        Coordinate(x_axis=1, y_axis=2),
    ],
    'l': [Coordinate(x_axis=2, y_axis=0), Coordinate(x_axis=3, y_axis=7)],
    't': [Coordinate(x_axis=2, y_axis=3), Coordinate(x_axis=3, y_axis=10)],
    'b': [Coordinate(x_axis=2, y_axis=10), Coordinate(x_axis=3, y_axis=0)],
    'r': [Coordinate(x_axis=2, y_axis=12), Coordinate(x_axis=3, y_axis=2)],
}


@pytest.mark.parametrize(
    'word, coordinates',
    (
        pytest.param(
            'foo',
            [
                'Start at: (X0, Y8), End at: (X0, Y10)',
                'Start at: (X1, Y0), End at: (X1, Y2)',
            ],
            id='foo',
        ),
        pytest.param(
            'bar',
            [
                'Start at: (X2, Y10), End at: (X2, Y12)',
                'Start at: (X3, Y0), End at: (X3, Y2)',
            ],
            id='bar',
        ),
        pytest.param(
            'name',
            [
                'Start at: (X0, Y2), End at: (X0, Y5)',
                'Start at: (X1, Y7), End at: (X1, Y10)',
                'Start at: (X2, Y4), End at: (X2, Y7)',
                'Start at: (X3, Y11), End at: (X3, Y14)',
            ],
            id='name',
        ),
        pytest.param(
            'is',
            [
                'Start at: (X0, Y6), End at: (X0, Y7)',
                'Start at: (X1, Y3), End at: (X1, Y4)',
                'Start at: (X1, Y3), End at: (X2, Y2)',
                'Start at: (X2, Y8), End at: (X2, Y9)',
                'Start at: (X2, Y8), End at: (X3, Y9)',
                'Start at: (X3, Y3), End at: (X3, Y4)',
                'Start at: (X3, Y3), End at: (X2, Y2)',
            ],
            id='is',
        ),
    ),
)
def test_puzzle_search_word_coordinates(
    word: str, coordinates: LetterCoordinates
) -> None:
    """Test the combination of given words are found in a board of letters.

    The word with starting/ending coordinates are expected to be generated.
    """
    puzzle = SearchWordPuzzle(_board_of_letters)
    actual_coordinates = puzzle.coordinates(word)
    assert coordinates == actual_coordinates, (
        f'Expected: {coordinates} coordinates '
        f'for "{word}" word but got {actual_coordinates}'
    )


def test_puzzle_invalid_board_of_letters() -> None:
    """Test that board of letters is empty.

    ValueError should be raised in case if empty board of letters.
    """
    puzzle = SearchWordPuzzle(board={})
    with pytest.raises(ValueError):
        puzzle.coordinates('foo')


def test_puzzle_word_not_in_board() -> None:
    """Test that a given word is absent in a board of letters."""
    puzzle = SearchWordPuzzle(
        board={
            'a': [
                Coordinate(x_axis=0, y_axis=0),
                Coordinate(x_axis=1, y_axis=1),
            ]
        }
    )
    coordinates: List[str] = puzzle.coordinates('foo')
    assert (
        not coordinates
    ), f'Coordinates should be empty but "{coordinates}" found'


def test_puzzle_letter_directions() -> None:
    """Test that letters in a grid can be found in all 8 directions: forwards,
    upwards, downwards, backwards and corresponding diagonals.
    """
    puzzle = SearchWordPuzzle(board={})
    actual_coordinates = len(puzzle.MOVEMENT_COORDINATES)
    expected_coordinates = 8
    assert expected_coordinates == actual_coordinates, (
        f'There should be {expected_coordinates} possible movement '
        f'coordinates to search a word but got {actual_coordinates} instead'
    )


def test_puzzle_name() -> None:
    """Test a puzzle name is properly generated."""
    expected_name = 'SearchWordPuzzle'
    actual_name = SearchWordPuzzle(board={}).name
    assert expected_name == actual_name, (
        f'Expected: {expected_name} puzzle name '
        f'!= Actual: {actual_name} puzzle name'
    )
