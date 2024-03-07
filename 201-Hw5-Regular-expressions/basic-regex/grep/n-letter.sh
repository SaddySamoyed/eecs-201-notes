#!/bin/bash

# n-letter.sh <path to dictionary file> <n>
# ^ This specifies that the dictionary file path is the first argument and 
#   the number is the second argument,
#   and the angle brackets specifies that that they are mandatory arguments
# print out words in the dictionary that are composed of only n alphabetic letters; no apostrophes or other punctuation
# Like in the dictionary file, each word should be on its own line
# *This must use only one grep command*

# do not modify this if block
if [[ $# -lt 2 ]]; then
    echo "usage: $0 <path to dictionary file> <n>"
    exit 1
fi

# TODO add your grep here
grep -E "^[a-zA-Z]{$2}$" $1