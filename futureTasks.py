#!/usr/bin/env python

"""
filter incoming lines based on date threshold
hides tasks marked with a date threshold ("t:YYYY-MM-DD") in the future
this is intended to be used as TODOTXT_FINAL_FILTER
"""

import sys
import re

from datetime import datetime


pattern = re.compile(r"t:(\d{4})-(\d{2})-(\d{2})")


def main(args=None):
	now = datetime.now()
	for line in sys.stdin:
		match = pattern.search(line)
		if match:
			threshold = [int(i) for i in match.groups()]
			if datetime(*threshold) < now:
				print(line.strip())
		else:
			print(line.strip())
	return True


if __name__ == "__main__":
	status = not main(sys.argv)
sys.exit(status)
