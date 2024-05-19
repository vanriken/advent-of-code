#!/bin/bash

# Check if an argument has been provided
if [ -z "$1" ]; then
    echo "Usage: $0 number"
    exit 1
fi

day=$1
padded_day=$(printf "%02d" "${day}")

input_filename="${padded_day}-input.txt"
solution_filename="${padded_day}-solution.py"

touch ${input_filename}
cp "solution_template.py" -- "${solution_filename}"

# Replace some strings in the solution file
sed -i "s/<day-number>/${day}/g" "${solution_filename}"
sed -i "s/<input-file>/${input_filename}/g" "${solution_filename}"

