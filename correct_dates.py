#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd
from datetime import datetime
from dateutil.parser import parse

try:
	filename = sys.argv[1]
except:
	print
	print "Usage: ./correct_dates.py <filename.csv>"
	print
	sys.exit(0)

df = pd.read_csv(filename)

corrected_dates = []

for i in range(0,len(df['Date'])):
	corrected_dates.append(parse(df['Date'][i]))

df['Date'] = corrected_dates

new_file = "CLEAN_" + str(filename)

df.to_csv(new_file)
