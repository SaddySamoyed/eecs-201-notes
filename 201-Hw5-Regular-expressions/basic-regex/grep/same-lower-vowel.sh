#!/bin/bash

# same-lower-vowel.sh <path to dictionary file>
# ^ This specifies that the dictionary file path is the first argument
#   and the angle brackets specifies that it's a mandatory argument
# print out words in the dictionary that contain at least 2 of the same lowercase vowel *in a row*
# (for the sake of this assignment: a,e,i,o,u are vowels, and y is never a vowel)
# e.g. aardvark, week, radii, zoom, vacuum
# Like in the dictionary file, each word should be on its own line
# *This must use only one grep command*
# Hint: think about backreferences

# do not modify this if block
if [[ $# -lt 1 ]]; then
    echo "usage: $0 <path to dictionary file>"
    exit 1
fi

# TODO add your grep here
grep -E '([aeiou])\1' $1