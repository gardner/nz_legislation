#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python3 ${SCRIPT_DIR}/src/char.py -p "$1"
python3 ${SCRIPT_DIR}/src/act2json.py -p "$1"


