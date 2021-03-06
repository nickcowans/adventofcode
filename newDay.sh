#!/bin/bash
# use: ./newDay day (year)
if [[ "${1}" == "" ]]; then
    echo "use: ./newDay.sh day (year)"
    echo "e.g. ./newDay.sh 7 2015"
    exit
fi

day=$(printf "%02d" ${1})

if [[ "${2}" == "" ]]; then
    year=2021
else
    year=${2}
fi

if [[ ! -d "$year" ]]; then
    mkdir $year
fi

if [[ ! -d "$year/Day_$day" ]]; then
    mkdir $year/Day_$day
fi

touch $year/Day_$day/input.txt
touch $year/Day_$day/example.txt
touch $year/Day_$day/day-$day-part-1.py
touch $year/Day_$day/day-$day-part-2.py
