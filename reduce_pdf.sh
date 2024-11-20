#!/bin/bash

error()
{
    echo "$@"
    exit 1
}

if [ $# -ne 2 ]; then
    cat<<EOF
usage:
   $0   <input-pdf>  <output-pdf>
EOF
    exit 1
fi

input=$1
output=$2

[ -f "$input" ] || error "no such input file, $input"
[ -f "$output" ] && error "$output already exists"

gs \
   -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
  -dDownsampleColorImages=true \
  -dColorImageResolution=300 \
  -dNOPAUSE -dBATCH \
  -sOutputFile="$output"  "$input"
