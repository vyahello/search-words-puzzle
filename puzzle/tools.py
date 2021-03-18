"""A module represents an API for the `search-words-puzzle` tool."""
from typing import Generator, Iterable

from loguru import logger as _logger

from puzzle.properties import LetterCoordinates
from puzzle.puzzles import SearchPuzzle, SearchWordPuzzle


async def start_word_search_puzzle(board: LetterCoordinates, word: str) -> None:
    """Start word search puzzle tool.

    It will generate a random grid of letters and match them with
    the corresponding word.

    Args:
        board: (dict) a board with coordinates of grid letters.
        word: (str) a word to search.
    """
    puzzle: SearchPuzzle = SearchWordPuzzle(board)
    coordinates: Iterable[str] = await puzzle.coordinates(word)
    if not coordinates:
        _logger.info(f'"{word}" word is absent in a grid')
    else:
        _logger.info(
            f'Found "{word}" word coordinates in a grid: {coordinates}'
        )


async def start_words_search_puzzle(
    board: LetterCoordinates, words: Generator[str, None, None]
) -> None:
    """Start words search puzzle tool.

    It will generate a random grid of letters and match them with
    the corresponding words.

    Args:
        board: (dict) a board with coordinates of grid letters.
        words: (generator) a generator of words to search.
    """
    for word in words:  # type: str
        await start_word_search_puzzle(board, word)
