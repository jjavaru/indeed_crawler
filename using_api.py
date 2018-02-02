#More comments. This was added after I staged this file into the index. Will it get pushed into my local repo?
#Adding a comment just so I'll have something to add, commit, and push into github

from indeed import IndeedClient
from pprint import pprint

client = IndeedClient(publisher=4201738803816157)

params = {
    'q': "python",
    'l': "53562",
    'userip': "1.2.3.4",
    'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

search_response = client.search(**params)

job_dict = dict()

for result in search_response['results']:
    job_dict[result['jobkey']] = result['jobtitle']

for val in sorted(job_dict.values()):
    print(val)

##pprint(job_dict)
##print(search_response['results'])