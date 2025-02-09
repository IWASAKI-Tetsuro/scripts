#! /bin/bash

while read line; do
filename=`echo ${line} | sed "s/\.svg$//g"`

  if [[ $line =~ \.svg$ ]]; then
    if [ "${filename}.pdf" -nt "${filename}.svg" ]; then
      echo "Nothing to do for ${filename}.svg"
    fi
    if [ ! -e ${filename}.pdf ] || [ "${filename}.pdf" -ot "${filename}.svg" ]; then
      echo "${filename}.svg -> ${filename}.pdf"
  	  LC_ALL=C inkscape ${filename}.svg -D --export-type=pdf --export-filename=${filename}.pdf
    fi
  else
    echo "${filename} is not an SVG file."
  fi

done
