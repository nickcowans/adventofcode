#!/bin/bash
# use: ./newDay day (year)
if [[ "${1}" == "" ]]; then
    echo "use: ./newDay.sh day (year)"
    echo "e.g. ./newDay.sh 7 2015"
    exit
fi

day=$(printf "%02d" ${1})
dayAOC=${1}


if [[ "${2}" == "" ]]; then
    year=2022
else
    year=${2}
fi

if [[ ! -d "$year" ]]; then
    mkdir $year
fi

if [[ ! -d "$year/Day_$day" ]]; then
    mkdir $year/Day_$day
fi

touch $year/Day_$day/example.txt
touch $year/Day_$day/day-$day-part-1.py
touch $year/Day_$day/day-$day-part-2.py
touch $year/Day_$day/day-$day.py

source .session
curl https://adventofcode.com/$year/day/$dayAOC/input --cookie "session=${SESSION}" > $year/Day_$day/input.txt