#!/usr/bin/env python
import sys
from os import system, path
from time import strftime, localtime

# delay to use for the notify-send command
delay = 5000

def parseFile(p: str) -> EnvironmentError | list:
    if path.isfile(p):
        with open(p) as f:
            lines = f.readlines()
            mapping = []
            for line in lines:
                parts = line.split(" = ")
                item = (parts[0], parts[1])
                mapping.append(item)
            return mapping
    else:
        raise EnvironmentError(f"The provided path '{p}' does not exist")

def extractPath(argv: list) -> EnvironmentError | str:
    if (len(argv) <= 1):
        raise EnvironmentError("Looks like you have not provided the calendar path. Tip: --calendar=path")
    else:
        if not argv[1].startswith("--calendar="):
            raise EnvironmentError("You must provide the path to the calendar: --calendar=path")
        else:
            calendar = argv[1].split("=")[1]
            return calendar

try:
    calendar = extractPath(sys.argv)
    dates = parseFile(calendar)
    today = strftime("%d.%m", localtime())
    matches = [date for date in dates if date[0] == today]
    if (len(matches) > 0):
        text = ''
        for m in matches:
            text += m[1]
        system(f"notify-send -t {delay} \"{text}\"")
except EnvironmentError as e:
    print(e)
