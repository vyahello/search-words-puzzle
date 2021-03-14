#!/usr/bin/env bash

declare -a RESULT

# Specifies a set of variables to declare files to be used for code assessment
PACKAGE="puzzle"
PY_FILES="*.py"
ROOT="./"

# Specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"


pretty-printer-box() {
:<<DOC
  Provide pretty-printer static tool checker box
DOC
  tab="$*xxxx"
  format=${replace:--}
  echo -e "${tab//?/$format}"
  echo -e "$format $* $format"
  echo -e "${tab//?/$format}"
}


store-failures() {
:<<DOC
  Combine encountered failures from all static analysis tools
DOC
  RESULT+=("$1")
}


install-python-dependencies() {
:<<DOC
  Install python static code analysis dependencies
DOC
  ( pretty-printer-box "Installing python code analysis packages ..." &&
    ( pip install --no-cache-dir --upgrade pip ) &&
    ( pip install --no-cache-dir -r requirements-dev.txt )
  ) || store-failures "Python packages installation is failed!"
}


check-black() {
:<<DOC
  Start "black" code analyser
DOC
  ( pretty-printer-box "Running black analysis ..." &&
    black --check ${ROOT}
  ) || store-failures "black analysis is failed"
}


check-flake8() {
:<<DOC
  Start "flake8" code analyser
DOC
  ( pretty-printer-box "Running flake8 analysis ..." &&
    flake8 "${PACKAGE}"
  ) || store-failures "flake8 analysis is failed"
}


check-pylint() {
:<<DOC
  Start "pylint" code analyser
DOC
  ( pretty-printer-box "Running pylint analysis ..." &&
    pylint $(find "${PACKAGE}" -iname "${PY_FILES}")
  ) || store-failures "pylint analysis is failed"
}


check-mypy() {
:<<DOC
  Start "mypy" code analyser
DOC
  ( pretty-printer-box "Running mypy analysis ..." &&
    mypy --package ${PACKAGE}
  ) || store-failures "mypy analysis is failed"
}


check-docstrings() {
:<<DOC
  Start static documentation code style formatters
DOC
  ( pretty-printer-box "Running pydocstyle analysis ..." &&
    pydocstyle --explain --count ${PACKAGE}
  ) || store-failures "pydocstyle analysis is failed"

  ( pretty-printer-box "Running interrogate analysis ..." &&
    interrogate -vv ${PACKAGE}
  ) || store-failures "interrogate analysis is failed"
}


start-analysis() {
:<<DOC
  Start all code analysis tools
DOC
  check-black
  check-flake8
  check-pylint
  check-mypy
  check-docstrings
}


run-code-assessment() {
:<<DOC
  Start code assessment procedure
DOC
  pretty-printer-box "Code assessment is started for the '$PACKAGE' project"
  start-analysis

  if [[ ${#RESULT[@]} -ne 0 ]]; then
    pretty-printer-box "${FAILED_OUT}There are some errors identified while assessing the code. Please see errors above.${NONE_OUT}"
    for item in "${RESULT[@]}"; do
      pretty-printer-box "${FAILED_OUT}- ${item}${NONE_OUT}"
    done
    exit 100
  fi
  pretty-printer-box "${PASSED_OUT}Code analysis is passed for the '$PACKAGE' project ${NONE_OUT}"
}


main() {
:<<DOC
  Start main entrypoint of a code assessment tool
DOC
  if [[ "$1" == "with-tools-installation" ]];
    then install-python-dependencies
  fi
  run-code-assessment
}


main "$@"