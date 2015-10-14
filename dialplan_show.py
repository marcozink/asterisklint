#!/usr/bin/env python3
"""
Show dialplan like Asterisk does with CLI command "dialplan show".
"""
import sys

from asterisklint import FileDialplanParser


parser = FileDialplanParser()
parser.include(sys.argv[1])
dialplan = next(iter(parser))
print(dialplan.format_as_dialplan_show(
    reverse=(not sys.argv[2:3])))
