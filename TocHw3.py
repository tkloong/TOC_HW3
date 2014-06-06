#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author		: 陳勁龍
#Student ID	: F74005018
#Description	: Calculate average sale price of the specific area after the year

import sys
import urllib
import json

if len(sys.argv) != 5:
	print 'Usage: {0} <URL> <鄉鎮市區> <Road_Name> <year>'.format(sys.argv[0])
	sys.exit()

sys.argv[4] = int(sys.argv[4]+"01")		# Year + month
data = json.load(urllib.urlopen(sys.argv[1]))

total = matches = 0
for datum in data:
	if datum[u'鄉鎮市區'] and datum[u'土地區段位置或建物區門牌'] and sys.argv[2] == datum[u'鄉鎮市區'].encode('utf-8') and sys.argv[3] in datum[u'土地區段位置或建物區門牌'].encode('utf-8') and sys.argv[4] <= datum[u'交易年月']:
		total += datum[u'總價元']
		matches += 1

if matches:
	print total / matches
else:
	print 0
