#!/bin/bash

# ing.sh <path to dictionary file>
# ^ This specifies that the dictionary file path is the first argument
#   and the angle brackets specifies that it's a mandatory argument
# prints out words in the dictionary that end with "ing"
# Like in the dictionary file, each word should be on its own line
# *This must use only one grep command*

# do not modify this if block
if [[ $# -lt 1 ]]; then
    echo "usage: $0 <path to dictionary file>"
    exit 1
fi

# TODO add your grep here
grep "ing$" $1