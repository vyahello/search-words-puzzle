#!/usr/bin/env bats


setup() {
:<<DOC
  Install puzzle package
DOC
  python setup.py install
}


teardown() {
:<<DOC
  Remove puzzle package
DOC
  rm -rf ${PACKAGE_NAME}.egg-info dist build
  pip uninstall -y ${PACKAGE_NAME}
}


@test "puzzle package name" {
:<<DOC
  Test puzzle name
DOC
  pip list | grep ${PACKAGE_NAME}
  [ "$?" -eq 0 ]
}


@test "puzzle package version" {
:<<DOC
  Test puzzle version
DOC
  pip list | grep ${PACKAGE_VERSION}
  [ "$?" -eq 0 ]
}


@test "puzzle package summary" {
:<<DOC
  Test puzzle summary
DOC
  pip show ${PACKAGE_NAME} | grep "A package contains a set of interfaces for \`${PACKAGE_NAME}\` app"
  [ "$?" -eq 0 ]
}
