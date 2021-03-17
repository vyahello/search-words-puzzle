"""
A test suite contains a set of test cases for the puzzle
grids interfaces.
"""
import pytest

from puzzle.grids import Content, GridContent, Grid, RandomWordsGrid
from puzzle.properties import Coordinate, LetterCoordinates, GridSize

pytestmark = pytest.mark.unittest

_grid_height: int = 15
_grid_width: int = 15


@pytest.fixture()
def random_words_grid() -> Grid:
    """Return a grid of random letters.

    Build a grid of letters when entering into the context manager.
    """
    with RandomWordsGrid(
        grid_size=GridSize(_grid_height, _grid_width)
    ) as grid:  # type: Grid
        yield grid


@pytest.mark.parametrize(
    'content, letter_to_coordinates',
    (
        pytest.param(
            GridContent(rows=['a']),
            {'a': [Coordinate(x_axis=0, y_axis=0)]},
            id='a',
        ),
        pytest.param(
            GridContent(rows=['a', 'b']),
            {
                'a': [Coordinate(x_axis=0, y_axis=0)],
                'b': [Coordinate(x_axis=1, y_axis=0)],
            },
            id='a\nb',
        ),
        pytest.param(
            GridContent(rows=['aa', 'bb', 'cc']),
            {
                'a': [
                    Coordinate(x_axis=0, y_axis=0),
                    Coordinate(x_axis=0, y_axis=1),
                ],
                'b': [
                    Coordinate(x_axis=1, y_axis=0),
                    Coordinate(x_axis=1, y_axis=1),
                ],
                'c': [
                    Coordinate(x_axis=2, y_axis=0),
                    Coordinate(x_axis=2, y_axis=1),
                ],
            },
            id='aa\nbb\ncc',
        ),
    ),
)
def test_grid_content_to_coordinates(
    content: Content, letter_to_coordinates: LetterCoordinates
) -> None:
    """Test the location (coordinates) of the content of random letters.

    Every letter in a grid is able to contain multiple coordinates.
    """
    expected = content.to_coordinates()
    assert expected == letter_to_coordinates, (
        f'Expected letter coordinates: {expected} != '
        f'Actual letter coordinates: {letter_to_coordinates}'
    )


@pytest.mark.parametrize(
    'content, result',
    (
        pytest.param(GridContent(rows=['a']), 'a', id='a'),
        pytest.param(GridContent(rows=['a', 'b']), 'a\nb', id='a\nb'),
        pytest.param(
            GridContent(rows=['aa', 'bb', 'cc']), 'aa\nbb\ncc', id='aa\nbb\ncc'
        ),
    ),
)
def test_valid_grid_content(content: Content, result: str) -> None:
    """Test the random grid of letters is properly generated (not empty)."""
    assert result == str(
        content
    ), f'Expected content: {result} != Actual content: {content}'


@pytest.mark.parametrize(
    'grid_size',
    (
        GridSize(0, 0),
        GridSize(1, 0),
        GridSize(0, 1),
        GridSize(-1, 0),
        GridSize(0, -1),
        GridSize(1, -1),
        GridSize(-1, 1),
    ),
)
def test_invalid_grid_size(grid_size: GridSize) -> None:
    """The the combination of invalid grid size.

    ValueError should be raised in case of invalid grid size.
    """
    with pytest.raises(ValueError):
        with RandomWordsGrid(grid_size) as grid:  # type: Grid
            str(grid.content)


def test_valid_grid_size(random_words_grid: Grid) -> None:
    """Test grid generates a content with the expected height and width."""
    content = str(random_words_grid.content).split()
    assert len(content) == _grid_height, (
        f'Expected grid height: {_grid_height} != '
        f'Actual grid height: {len(content)}'
    )
    assert len(content[0]) == _grid_width, (
        f'Expected grid width: {_grid_width} != '
        f'Actual grid width: {len(content[0])}'
    )


def test_invalid_grid_content() -> None:
    """Test the random grid of letters is invalid (empty).

    ValueError exception should be raised in case of empty grid rows.
    """
    with pytest.raises(ValueError):
        str(GridContent(rows=[]))


def test_grid_content_is_generated(random_words_grid: Grid) -> None:
    """Test the grid is able to generate a content of random letters."""
    assert isinstance(random_words_grid.content, Content), (
        f'Random grid content should be "{Content.__class__}" '
        f'data type but got "{random_words_grid.content.__class__}" type'
    )
    assert str(random_words_grid.content), (
        'The grid content is not generated: '
        f'got "{random_words_grid.content}" content'
    )


def test_grid_properties(random_words_grid: Grid) -> None:
    """Test grid contains proper attributes (height and width)."""
    height = random_words_grid.height
    width = random_words_grid.width
    assert _grid_height == height, (
        f'Expected grid height property: {_grid_height} '
        f'!= Actual grid height property: {height}'
    )
    assert _grid_width == width, (
        f'Expected grid width property: {_grid_width} '
        f'!= Actual grid width property: {width}'
    )


def test_empty_grid(random_words_grid: Grid) -> None:
    """Test grid is able to be refreshed (got empty).

    ValueError should be raised when generating empty grid content.
    """
    random_words_grid.refresh()
    with pytest.raises(ValueError):
        str(random_words_grid.content)
