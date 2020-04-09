#!/usr/bin/env sh

START_DATE="$(stat /proc/1/cmdline | grep "Modify:" | cut -d' ' -f 2,3 | cut -d '.' -f 1)"
START=$(date --date="$START_DATE" +%s)

NOW=$(date +%s)

DIFF=$(($NOW - $START))

if [ $DIFF -ge $GRACE_PERIOD ]; then
	exit 0
else
	exit 1
fi
