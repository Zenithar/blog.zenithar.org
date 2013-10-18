# -*- coding: utf-8 -*-

import json,yaml
import codecs
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.blog

def importInMongo(filename, doc):
	docId = filename[23:-8]
	db.articles.save({"_id": docId, "document": doc})

with codecs.open("posts.json", "r", "utf-8") as f:
	documents = json.load(f)

	for filename, doc in documents.iteritems(): 
		print "Importing " + filename
		importInMongo(filename, doc)
