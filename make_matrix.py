#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pandas as pd

try:
	language = sys.argv[1]

except:
	print
	print "Usage: ./make_matrix.py language"
	print
	sys.exit(0)

filename = language + "_composition.txt"

# Read project dataset
df = pd.read_csv(filename, sep='\t', header=None)
df = df.round(2)
df.columns = ['id','file','topic_0','topic_1','topic_2','topic_3','topic_4']
df['file'] = df['file'].str.replace('%20',' ')
df['id'] = df['file'].str.extract('(\d+)')
df['id'] = df['id'].astype('int64')

metadata = pd.read_csv('final.csv')
dataset = pd.merge(df, metadata, on='id')
titles = dataset.groupby('newspaper').mean().round(2)
titles = titles.drop(columns=['id','lat','long'])
