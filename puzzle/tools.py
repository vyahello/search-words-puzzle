"""A module represents an API for the `search-words-puzzle` tool."""
from multiprocessing import Pool, cpu_count
from typing import Iterable

from loguru import logger as _logger

from puzzle.puzzles import SearchPuzzle, SearchWordPuzzle
from puzzle.words import HiddenWord, HiddenWords


def start_word_search_puzzle(word: HiddenWord) -> None:
    """Start word search puzzle tool.

    It will generate a random grid of letters and match them with
    the corresponding word.

    Args:
        word: (HiddenWord) a word to search.
    """
    puzzle: SearchPuzzle = SearchWordPuzzle(word.board)
    coordinates: Iterable[str] = puzzle.coordinates(word.value)
    if not coordinates:
        _logger.info(f'"{word}" word is absent in a grid')
    else:
        _logger.info(
            f'Found "{word}" word coordinates in a grid: {coordinates}'
        )


def start_words_search_puzzle(words: HiddenWords) -> None:
    """Start words search puzzle tool.

    The search is conducted with parallel processes based on CPU cores amount.

    It will generate a random grid of letters and match them with
    the corresponding words.

    Args:
        words: (generator) a generator of words to search.
    """
    pool = Pool(processes=cpu_count())
    parallel_search = pool.map_async(
        func=start_word_search_puzzle, iterable=words
    )
    parallel_search.get()
