"""A module contains as set API for the puzzle properties."""
from dataclasses import dataclass
from typing import Any  # pylint:disable=unused-import
from typing import Dict, List, Tuple

LetterCoordinates = Dict[str, List['Coordinate']]


class SafePropertyMixin:  # pylint:disable=too-few-public-methods
    """The class represents a safe mixin in terms of used properties.

    It is not supposed to be initiated as a part of mixin type.
    """

    def __post_init__(self) -> None:
        """Evaluate input properties for proper data types.

        Raises:
            TypeError: if invalid data type was passed.
        """
        for (
            field_name,
            field_type,
        ) in self.__annotations__.items():  # type: str, Any
            if not isinstance(self.__dict__[field_name], field_type):
                raise TypeError(
                    f'The field "{field_name}" should be '
                    f'"{field_type}" data type but '
                    f'"{type(self.__dict__[field_name])}" is used.'
                )


@dataclass(frozen=True)
class Coordinate(SafePropertyMixin):
    """The class represents a single coordinate property of a particular item.

    Example:
    >>> point = Coordinate(x_axis=15, y_axis=15)
    ...
    """

    x_axis: int
    y_axis: int

    def as_tuple(self) -> Tuple[int, int]:
        """Convert coordinate of x and y axis into tuple object.

        Example:
        >>> point = Coordinate(x_axis=15, y_axis=15)
        >>> point.as_tuple()
        (15, 15)

        Returns:
            tuple: a sequence of x and y axis e.g (10, 10)
        """
        return self.x_axis, self.y_axis

    def __str__(self) -> str:
        """Return user friendly coordinate name.

        Returns:
            str: string representation of the coordinate.
        """
        return f'(X{self.x_axis}, Y{self.y_axis})'


@dataclass(frozen=True)
class GridSize(SafePropertyMixin):
    """The class represents a particular grid size.

    Example:
    >>> grid = GridSize(height=10, width=10)
    ...
    """

    height: int
    width: int
