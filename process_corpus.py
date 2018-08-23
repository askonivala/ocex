#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd
import os
from collections import defaultdict

try:
	filename = sys.argv[1]
except:
	print
	print "Usage: ./process_corpus.py <filename.csv>"
	print
	sys.exit(0)

# Settings
query = "Bobriko"
offset = 50

# Read project dataset
df = pd.read_csv(filename)
# Parse languages
languages = df.language.unique()
for language in languages:

	path = "corpus/" + language + "/"

	if not os.path.exists(path):
    		os.makedirs(path)

	for index, row in df.iterrows():
		if row['language'] == "Finnish" or row['language'] == "Swedish":
			if row['language'] == language:
				#id = str(index + 2)
				id = str(row['id'])
				name = row['newspaper']
				filename = path + name + "_" + id + ".txt"
				try:
					len(row['text'])
				except:
					print row['text']
					row['text'] = ""
				if len(row['text']) == 0:
					print "skipping empty record " + str(row['newspaper'])
					continue
				try:
					with open (filename, "w") as f:
						f.write(row['text'])
				except:
					print "skipping " + str(row['newspaper'])
		else:
			if row['language'] == language:
				try:
					text = str(row['text'])
					pos_index = defaultdict(list)
					for pos, term in enumerate(text.split()):
    						pos_index[term].append(pos)
					tokens = text.split()
					for key, value in pos_index.iteritems():
						if key.startswith(query):
							#start immediately at first Bobrikoff
							start = pos_index[key][0]
							stop = pos_index[key][-1] + offset
							words = []
							# check how long the text is
							if start < 0:
								start = 0
							if stop > len(tokens):
								stop = len(tokens)
							for i in range(start,stop):
								try:
									words.append(tokens[i])
								except:
									print "WARNING"
							context = " ".join(words)
							print context
	        		        		#id = str(index + 2)
        	        				id = str(row['id'])
							name = row['newspaper']
                					filename = path + name + "_" + id + ".txt"
                					print filename
                					with open (filename, "w") as f:
                        					f.write(context)
				except:
					print "skipping " + str(row['newspaper'])
