# -*- coding: utf-8 -*-

import json,yaml
import codecs

#
# CREATE TABLE "posts" ("id" integer not null primary key autoincrement not null, 
#						"uuid" varchar(36) not null, 
#						"title" varchar(150) not null, 
#                       "slug" varchar(150) not null, 
#                       "markdown" text, 
#                       "html" text, 
# 						"image" text, 
#                       "featured" tinyint not null default '0', 
#                       "page" tinyint not null default '0', 
#						"status" varchar(150) not null default 'draft', 
#						"language" varchar(6) not null default 'en_US', 
#						"meta_title" varchar(150), 
#						"meta_description" varchar(200), 
#						"author_id" integer not null, 
#						"created_at" datetime not null, 
#						"created_by" integer not null, 
#						"updated_at" datetime, 
#						"updated_by" integer, 
#						"published_at" datetime, 
#						"published_by" integer
# );
#

def yaml_escape(s):
	return json.dumps(s, ensure_ascii=False)

def regenerateSource(filename, doc, idx):

	meta = doc['meta']
	contents = doc['content']

	with codecs.open(filename, "w", "utf-8") as f:

		f.write("---\n")
		f.write('layout: ' + meta['layout'] + '\n')
		f.write("date: " + yaml_escape(meta['date']) + "\n")
		f.write('title: ' + yaml_escape(meta['title']) + '\n')
		if 'description' in meta:
			f.write('description: ' + yaml_escape(meta['description']) + '\n')
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

	idx = 1
	for filename, doc in documents.iteritems(): 
		print "Rebuilding " + filename
		regenerateSource(filename, doc, idx)
		idx = idx + 1


