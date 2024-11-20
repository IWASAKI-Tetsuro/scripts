#! /bin/bash

svgfiles=(`ls -1 ./ | grep "\.svg$"`)
length=${#svgfiles[@]}
count=0

for svgfile in "${svgfiles[@]}"; do
  count=`expr $count + 1`
  filename=`echo ${svgfile} | sed 's/\.svg$//'`

if [ ! -f ./${filename}.pdf ]; then
	LC_ALL=C inkscape ${filename}.svg -D --export-type=pdf --export-filename=${filename}.pdf
  echo "${count}/${length} ${filename}.svg -> ${filename}.pdf"
else
  echo "${count}/${length} ${filename}.pdf already exists."
fi

done
