from puzzle import HiddenWord, HiddenWords


def test_hidden_word() -> None:
    """Verify a hidden word value."""
    expected = 'frr'
    word = HiddenWord(board={}, value=expected)
    assert (
        word.value == 'frr'
    ), f'Expect to see {expected} value but got {word.value}'


def test_hidden_words() -> None:
    words = HiddenWords(board={}, words=(word for word in ('foo', 'bar')))
    actual = list(words)
    expected = [
        HiddenWord(board={}, value='foo'),
        HiddenWord(board={}, value='bar'),
    ]
    assert (
        actual == expected
    ), f'Expect to see {expected} value but got {actual}'
