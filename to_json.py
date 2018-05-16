#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd
import json

try:
	filename = sys.argv[1]
except:
	print
	print "Usage: ./to_json.py <filename.csv>"
	print
	sys.exit(0)

df = pd.read_csv(filename)
out = "out.json"

for index, row in df.iterrows():
	data = {
		'lang' : row['Language'],
		'title' : row['Title (Newspaper)'],
		'link' : row['Link'],
		'text' : row['Text'],
		'date' : row['Date'],
		'location' : row['Location'],
		'id' : index
	}
	with open(out,'a') as outfile:
		json.dump(data, outfile, sort_keys=False)
		outfile.write('\n')
	outfile.close()
	data = {}
