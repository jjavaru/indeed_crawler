#More comments. This was added after I staged this file into the index. Will it get pushed into my local repo?
#Adding a comment just so I'll have something to add, commit, and push into github

# This comment was actually made from a different box altogether! *codeanywhere*

from indeed import IndeedClient



client = IndeedClient(publisher=4201738803816157)

params = {
    'q': "python",
    'l': "53562",
    'userip': "1.2.3.4",
    'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

search_response = client.search(**params)

print(search_response)
