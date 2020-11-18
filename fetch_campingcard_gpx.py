#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import requests


if __name__ == "__main__" :
	
	# Download
	
	r = requests.get('https://www.campingcard.is/')
	if r.status_code != 200 : raise ValueError("Http status code " + str(r.status_code))
	html = str(r.text)
	
	objs = None
	try :
		
		map_objects = html[html.find('var tjaldsvaedi_markers'):]
		map_objects = map_objects.split('\n')
		map_objects = map_objects[1]
		
		text = '[' + map_objects.strip()[:-1] + ']'
		
		# Fix broken json
		def fix_json(text, value) :
			key = value + ":"
			ret = text.replace(key, '"' + value + '":')
			return ret
		text = text.replace("'", '"')
		text = fix_json(text, "position")
		text = fix_json(text, "lng")
		text = fix_json(text, "lat")
		text = fix_json(text, "map")
		text = fix_json(text, "title")
		text = fix_json(text, "url")
		text = fix_json(text, "categories")
		text = fix_json(text, "description")
		text = text.replace(', "map": map', '')
		
		with open('CampingCard.is_Locations.json', 'w') as f_out :
			f_out.write(text)
			f_out.write('\n')
		
		objs = json.loads(text)
	
	except Exception as e:
		sys.stderr.write("Error parsing: " + str(e) + "\n")
		sys.exit(1)

	# Print GPX file
	print(
'''<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.0">
	<name>Example gpx</name>''')

#	<wpt lat="46.57638889" lon="8.89263889">
#		<ele>2372</ele>
#		<name>LAGORETICO</name>
#	</wpt>
		
	for i in objs :
		try :
			title = i['title']
			pos = i['position']
			lat = float(pos['lat'])
			lon = float(pos['lng'])
			url = i['url']
			desc = i['description']
			cat =i['categories']
			
			print('    <wpt lat="' + str(lat) + '" lon="' + str(lon) + '">')
			print('        <name>' + str(title) + '</name>')
			print('        <desc>' + str(desc).replace('<br/>', ' ') + '</desc>')
			print('        <link href="%s">%s</link>' % (str(url), str(title)))
			print('    </wpt>')
		except Exception as e :
			sys.stderr.write("Error parsing element " + str(i) + "\n")
	print('</gpx>')
