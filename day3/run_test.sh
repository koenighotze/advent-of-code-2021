#!/usr/bin/env bash
script=$1
expected=$2

last_line=$(perl -w "$script" < input.test | tail -n 1)

if [ "$last_line" = "$expected" ]; then
    echo "$0 [$script] Success"
    exit 0
else
    >&2 echo "Error: expected '$expected' but got '$last_line'"
    exit 1
fi