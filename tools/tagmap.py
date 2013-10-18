# -*- coding: utf-8 -*-

import yaml
import fnmatch
import os
import json
import codecs

matches = []
collection = {}
tag_map = {}

def normalize_tag(tag):
    return normalize_accent(tag.lower())

def normalize_accent(chaine):
    accent = ['\xc3\xa9', '\xc3\xa8', '\xc3\xaa', '\xc3\xa0', '\xc3\xb9', '\xc3\xbb', '\xc3\xa7', '\xc3\xb4', '\xc3\xae', '\xc3\xaf', '\xc3\xa2']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
 
    chaine = chaine.encode('utf-8')
    for i in xrange(len(accent)):
        chaine = chaine.replace(accent[i], sans_accent[i])
 
    return chaine

for root, dirnames, filenames in os.walk('src'):
  for filename in fnmatch.filter(filenames, '*.html.md'):
      matches.append(os.path.join(root, filename))

for _file in matches:
    section = {}
    section_name = ['meta', 'content']

    print "Parsing " + _file

    with codecs.open(_file, "r", "utf-8") as f:
        section_count = -1
        for line in f:      
            if (line == "---\n"):
                section_count += 1
            
            else:
                if not (section_name[section_count] in section): 
                    section[section_name[section_count]] = []

                section[section_name[section_count]].append(line)

    meta =  yaml.load("".join(section['meta']))
    section['meta'] = meta
    section['content'] = "".join(section['content'])

    new_tags = []
    for t in section['meta']['tags']: 
        nt = normalize_tag(t)

        if not nt in tag_map:
            tag_map[nt] = []
        tag_map[nt].append(_file)
        new_tags.append(nt)
    
    section['meta']['tags'] = new_tags

    if 'categories' in section['meta']:
        del section['meta']['categories']
    if 'status' in section['meta']:
        del section['meta']['status']
    if 'wordpress_id' in section['meta']:
        del section['meta']['wordpress_id']
    if 'slug' in section['meta']:
        del section['meta']['slug']

    collection[_file] = section

f_collection = codecs.open("posts.json",'w','utf-8')
f_collection.write(json.dumps(collection, ensure_ascii=False))
f_collection.close()

f_tag_map = codecs.open("tag_map.json",'w','utf-8')
f_tag_map.write(json.dumps(tag_map, ensure_ascii=False))
f_tag_map.close()