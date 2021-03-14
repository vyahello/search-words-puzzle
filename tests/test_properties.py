"""
A test suite contains a set of test cases for the puzzle
properties interfaces.
"""
import pytest

from puzzle.properties import Coordinate, GridProperty

pytestmark = pytest.mark.unittest

_expected_x_axis: int = 15
_expected_y_axis: int = 15
_expected_height: int = 15
_expected_width: int = 15


@pytest.fixture(scope='module')
def coordinate() -> Coordinate:
    """Return a custom coordinate object.

    A coordinate with X15 and Y15 location.
    """
    yield Coordinate(x_axis=_expected_x_axis, y_axis=_expected_y_axis)


@pytest.fixture(scope='module')
def grid_property() -> GridProperty:
    """Return a custom grid property object.

    A grid with 15 x 15 size.
    """
    yield GridProperty(height=_expected_height, width=_expected_width)


def test_coordinate_props(coordinate: Coordinate) -> None:
    """Test the coordinate contains proper x_axis and y_axis properties."""
    x_axis = coordinate.x_axis
    y_axis = coordinate.y_axis
    assert (
        _expected_x_axis == x_axis
    ), f'Expect to see {_expected_x_axis} x axis coordinate but got - {x_axis}'
    assert (
        _expected_y_axis == y_axis
    ), f'Expect to see {_expected_y_axis} y axis coordinate but got - {y_axis}'


def test_coordinate_as_tuple(coordinate: Coordinate) -> None:
    """Test the coordinate representation as a tuple data type."""
    expected_coordinate_tuple = _expected_x_axis, _expected_y_axis
    actual_coordinate_tuple = coordinate.as_tuple()
    assert expected_coordinate_tuple == actual_coordinate_tuple, (
        f'Expect to see {expected_coordinate_tuple} axis tuple coordinate '
        f'but got - {actual_coordinate_tuple}'
    )


def test_coordinate_as_str(coordinate: Coordinate) -> None:
    """Test the coordinate representation as a string data type."""
    expected_coordinate_str = f'(X{_expected_y_axis}, Y{_expected_y_axis})'
    actual_coordinate_str = str(coordinate)
    assert expected_coordinate_str == actual_coordinate_str, (
        f'Expect to see {expected_coordinate_str} axis string coordinate '
        f'but got - {actual_coordinate_str}'
    )


def test_invalid_coordinate() -> None:
    """Test invalid coordinate data type.

    The coordinate should match only integers.
    TypeError should be raised if invalid is passed.
    """
    with pytest.raises(TypeError):
        Coordinate(x_axis='Foo', y_axis='Bar')


def test_grid_property(grid_property: GridProperty) -> None:
    """Test the coordinate contains proper x_axis and y_axis properties."""
    height = grid_property.height
    width = grid_property.width
    assert (
        _expected_height == height
    ), f'Expect to see {_expected_height} height but got - {height}'
    assert (
        _expected_width == width
    ), f'Expect to see {_expected_width} width but got - {width}'


def test_invalid_grid_property() -> None:
    """Test invalid grid properties data type.

    The grid should match only integers.
    TypeError should be raised if invalid is passed.
    """
    with pytest.raises(TypeError):
        GridProperty(height='Foo', width='Bar')
