#!/bin/bash

exitScript () {
	echo "Exiting with exit code $1."$'\n'
	exit $1
}

# Change to the directory of this file
cd $(dirname "${BASH_SOURCE[0]}")

# Activate the virtual Environment
VENV=".venv"
if ! [[ -f "$VENV/bin/activate" ]]; then
	echo "Virtual environment [$VENV] not found!"
	exitScript 1
fi
source $VENV/bin/activate

# Building the package
python3 setup.py sdist bdist_wheel

exitScript 0