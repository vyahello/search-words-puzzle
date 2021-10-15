Versions
========

0.0.2
--------
_Release date: 15.10.2021_

- Introduce git commit template
- Remove redundant files from manifest
- Update build status badge link
- Add test to measure parallel words search
- Introduce multiprocessing for words search
- Remove howtos from test branch
- Use asynchronous approach to match words in a grid
- Implement a unified interface to start "words search" puzzle
- Introduce the puzzle tool usage
- Introduce project logo

0.0.1
--------
_Release date: 17.03.2021_

- Implement package tests within CI
- Implement initial version of a search words puzzle tool
  - Check the tool instructions via `python -m puzzle --help` command
  - Additionally unit tests are added
- Configure CI workflow with Travis & Github actions
- Cover source code with docstring static analysis tools
- Integrate mypy static type checker tool
- Integrate pylint coding standard tool
- Integrate flake8 style guide tool
- Integrate black static code formatter tool
- Initialize puzzle package
- Split production/development project dependencies
- Support metadata within a search words puzzle
