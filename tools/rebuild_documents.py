# -*- coding: utf-8 -*-

import json,yaml
import codecs

def regenerateSource(filename, doc):

	meta = doc['meta']
	contents = doc['content']

	with codecs.open(filename, "w", "utf-8") as f:
		f.write("---\n")
		f.write('layout: ' + meta['layout'] + '\n')
		f.write("date: " + meta['date'] + "\n")
		f.write('title: ' + meta['title'] + '\n')
		if 'description' in meta:
			f.write('description: "' + meta['description'] + '"\n')
		if 'shorturl' in meta:
			f.write('shorturl: ' + meta['shorturl'] + '\n')
		f.write("tags:\n")
		for t in meta['tags']:
			f.write(" - " + t + "\n")
		f.write("\n---\n")
		f.write(contents)	
	return

with codecs.open("posts.json", "r", "utf-8") as f:
	documents = json.load(f)

	for filename, doc in documents.iteritems(): 
		print "Rebuilding " + filename
		regenerateSource(filename, doc)


