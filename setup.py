"""Package setup entrypoint."""
import re
import sys
from pathlib import Path
from typing import IO, Sequence
from setuptools import find_packages, setup


class _Package:
    """Represents a single package."""

    def __init__(self, path: Path) -> None:
        self._path = path

    @property
    def name(self) -> str:
        """Returns a package name e.g `some-package-name`."""
        return self._read(
            pattern=r"(?<=__package_name__: str = ')[\w-]+",
        )

    @property
    def version(self) -> str:
        """Return a package version e.g `0.0.1`."""
        return self._read(pattern=r"(?<=__version__: str = ')[\d\.\d\.\d]+")

    @property
    def author(self) -> str:
        """Return a package author e.g `some-author`."""
        return self._read(
            pattern=r"(?<=__author__: str = ')[\w\s-]+",
        )

    @property
    def license_(self) -> str:
        """Return a package license e.g `MIT`."""
        return self._read(
            pattern=r"(?<=__license__: str = ')[\w-]+",
        )

    @property
    def email(self) -> str:
        """Return a package email e.g `some-email@com`."""
        return self._read(
            pattern=r"(?<=__email__: str = ')[\w@\.-]+",
        )

    @property
    def goal(self) -> str:
        """Return a package goal e.g `reporting results`."""
        return self._read(
            pattern=r'(?<=""")[\w\s\.`-]+',
        )

    @property
    def _init_path(self) -> Path:
        """Return path to init file of a package."""
        return self._path / '__init__.py'

    def _read(self, pattern: str) -> str:
        """Read a package content.

        Args:
            pattern: <str> a package regular expression pattern.

        Raises:
            ValueError if a given pattern was not found.

        Returns:
            a content of init file.
        """
        with self._init_path.open() as init_stream:  # type: IO[str]
            try:
                return re.findall(pattern=pattern, string=init_stream.read())[0]
            except IndexError as error_message:
                raise ValueError(
                    f'Unable to grep "{pattern}" pattern '
                    f'from "{self._init_path}" filepath!'
                ) from error_message


def _load_readme() -> str:
    """Return a project description."""
    with Path('README.md').open() as readme:  # type: IO[str]
        return readme.read()


def _load_requirements() -> Sequence[str]:
    """Return project requirements sequence."""
    with Path('requirements.txt').open() as requirements:  # type: IO[str]
        return tuple(map(str.strip, requirements.readlines()))


def _setup_package(package: _Package) -> None:
    """Setup a package entrypoint.

    Args:
        package: <_Package> a package to setup.
    """
    setup(
        name=package.name,
        version=package.version,
        author=package.author,
        author_email=package.email,
        description=package.goal,
        long_description=_load_readme(),
        long_description_content_type='text/markdown',
        url=f'https://github.com/vyahello/{package.name}',
        packages=find_packages(
            exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')
        ),
        include_package_data=True,
        install_requires=_load_requirements(),
        classifiers=(
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            f'License :: OSI Approved :: {package.license_} License',
            'Operating System :: OS Independent',
        ),
        python_requires='>=3.7',
        entry_points={
            'console_scripts': (f'{package.name} = puzzle.__main__:easyrun',)
        },
    )


if __name__ == '__main__':
    sys.exit(_setup_package(package=_Package(path=Path('puzzle'))))
