#!/bin/bash

# needs at least one argument
# DO NOT MODIFY THIS IF BLOCK
if [[ $# -lt 1 ]]; then
    echo "usage: $0 <C files>"
    echo "  Turns C99/C++ style // coments into /* */ comments."
    echo "  Produces a file that has \".c89\" inserted before the \".c\" extension for each provided file"
    echo "  For example: \"c89ify.sh hello.c world.c\" will produce \"hello.c89.c\" and \"world.c89.c\" files"
    exit 1
fi

# Put your implementation here
# Function to replace // comments with /* */
convert_comments() {
    local file=$1
    local outfile="${file%.c}.c89.c" # Replace .c with .c89.c in the filename

    # Use sed to replace // comments with /* */ comments
    # The sed script handles lines with // and avoids replacing URLs that contain //
    sed -e '/https:\/\//b' -e '/http:\/\//b' -e 's|//\(.*\)|/*\1 */|' "$file" > "$outfile"
}

# Loop over each file provided as argument
for cfile in "$@"; do
    # Check if file has .c extension
    if [[ $cfile == *.c ]]; then
        convert_comments "$cfile"
    else
        echo "Error: File $cfile does not have a .c extension."
    fi
done