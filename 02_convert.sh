#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

## This is a bit of a hack to only process the latest version of each act
cd ${SCRIPT_DIR}/act/public
for d1 in $(ls); do
  cd ${SCRIPT_DIR}/act/public/$d1
  for d2 in $(ls); do
    cd ${SCRIPT_DIR}/act/public/$d1/$d2
    d3=$(ls | sort -g | tail -n 1)
    echo cd ${SCRIPT_DIR}/act/public/$d1/$d2/$d3
    cd ${SCRIPT_DIR}/act/public/$d1/$d2/$d3
    find . -name \*.xml -exec ${SCRIPT_DIR}/format.sh "{}" \;
  done
done

# Use jq to merge all the json files into a single jsonl file
find act -name \*.json -exec jq -c . '{}' \; >> corpus.jsonl
