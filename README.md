![Screenshot](media/icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://www.travis-ci.com/vyahello/search-words-puzzle.svg?branch=master)](https://travis-ci.org/vyahello/search-words-puzzle)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/search-words-puzzle/badge.svg?branch=search-words-puzzle-tool)](https://coveralls.io/github/vyahello/search-words-puzzle?branch=search-words-puzzle-tool)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with interrogate](https://img.shields.io/badge/interrogate-checked-yellowgreen)](https://interrogate.readthedocs.io/en/latest/)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/search-words-puzzle/badge)](https://www.codefactor.io/repository/github/vyahello/search-words-puzzle)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)

# Search words puzzle

> The project provides a command line interface tool to search words in a randomly generated grid of letters.
> 
> Words can be found along any diagonal, forwards, upwards, downwards or backwards and cannot be wrapped between edges.
> It is possible to find random words from the pre-defined text file as well as a single custom word.

## Tools

### Production

- python 3.7, 3.8, 3.9
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [typer](https://typer.tiangolo.com/)
- [loguru](https://loguru.readthedocs.io/en/stable/index.html)

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)
- [interrogate](https://interrogate.readthedocs.io/en/latest/)
- [bats](https://github.com/sstephenson/bats)

## Usage

![Usage](media/howto.gif)

### Quick start

Clone the repository:
```bash
git clone git@github.com:vyahello/search-words-puzzle.git
```

Install the tool:
```bash
cd search-words-puzzle
python setup.py install
```

Run the tool help via shell:
```bash
search-words-puzzle --help


  The tool searches words in a randomly generated grid of letters.

Options:
  --grid-size TEXT                The size for a randomly created grid of
                                  letters (a-z only).  [default: 50x50]

  --words-file-path PATH          A path to a custom text file with words to
                                  search.  [default: payload/words.txt]

  --words-limit INTEGER           Search N random words from a given text
                                  file.  [default: 5]

  --word TEXT                     A custom word to search in a grid of letters
                                  e.g "foo".  [default: ]

  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

### Local debug

Clone the repository:
```bash
git clone git@github.com:vyahello/search-words-puzzle.git
```

Install the tool requirements:
```bash
cd search-words-puzzle
python3 -m venv puzzle-env
. puzzle-env/bin/activate
pip install -r requirements.txt
```

Run the tool help via python:
```bash
python -m puzzle --help
```

**[⬆ back to top](#search-words-puzzle)**

## Development notes

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest -m unittest
```

In addition, package unit tests are implemented with [bats](https://github.com/sstephenson/bats) framework:
> `PACKAGE_NAME` and `PACKAGE_VERSION` environment variables should be set to run tests.

```bash
export PACKAGE_NAME=search-words-puzzle PACKAGE_VERSION=0.0.1
bats --pretty test-puzzle-tool.bats
```

### CI

The project has Travis CI and GitHub actions integration thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle` and `interrogate`) will be run automatically after every made change to the repository.

Please execute the command below, to be able to run code analysis locally:
```bash
./analyse-source-code.sh
```

In order to install python development dependencies before starting the code assessment procedure, please use the following command:
```bash
./analyse-source-code.sh with-tools-installation
```

### Commit template
In order to activate commit message template please run the following command:
```bash
git config commit.template .gitmessage.txt
```

### Documentation style

The project is based on [Google Style Python Docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for source code documentation. 
It is possible to integrate this style of docstring with PyCharm, please follow next instructions:
`Settings -> Tools -> Python Integrated Tools -> Docstring format -> Google`.

Here is an example of Google style docstring used within a project:
```python
def do_thing(first: int, second: int) -> int:
    """Do something ...
    
    Example:
    >>> do_thing('foo', 'bar')
    'FooBar'

    Args:
        first (int): parameter declares ...
        second (int): parameter declares ...

    Raises:
        ValueError if ...

    Returns: a result of ...
    """
    pass
```

### Logging

If you need a logger object, you have to define it as private variable on a module level like:
```python
from loguru import logger as _logger


_logger.info('Log an important message')
``` 
Then, just log a message. And please follow recommendations from https://docs.python.org/3.9/howto/logging.html#when-to-use-logging
while defining a level of logging for a particular message. Do not define a logging level within modules.

A best practice for _waits_ or _retries_ is:
1. `INFO` message when enter a function.
2. `DEBUG` message between iterations .
3. `INFO` message in case of successful execution (exit).

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Vladimir Yahello_. Please check [authors](AUTHORS.md) file for more details.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas will be described at project [issues](https://github.com/vyahello/search-words-puzzle/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#search-words-puzzle)**
