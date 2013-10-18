import elasticsearch,json

# Connect to localhost:9200 by default:
es = elasticsearch.Elasticsearch()

query = {
    "query" : {
      "match_all" : {}
    },
 
    "facets" : {
        "tagcloud" : {
            "terms" : { 
            	"field" : "document.meta.tags", 
            	"size" : 25, 
            	"exclude" : ["toulouse", "nice", "emi", "moi", "wordpress", "stage", "iup", "isi", "crous", "glasgow", "cv", "saint", "tgs", "url", "life", "amis", "wii", "pathinfo", "rewriting", "theme", "suexec", "opencube", "noel", "migration", "crash", "licence", "latex"] 
            }
        }
    }
}

print json.dumps(es.search(search_type="count", index="blog", body=query)['facets']['tagcloud']['terms'])