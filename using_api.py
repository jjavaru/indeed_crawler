from indeed import IndeedClient

# set up API connection and initial query
client = IndeedClient(publisher=4201738803816157)

# query parameters
query = "python"
location = "53562"
user_ip = "1.2.3.4"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
start = 0
limit = 10

params = {
    'q': query,
    'l': location,
    'userip': user_ip,
    'useragent': user_agent,
    'start': start,
    'limit': limit
}

job_dict = dict() # create empty dictionary to hold job results

while True:
    search_response = client.search(**params)
    print("Page #{}. Start {}. End {}. Total {}.".format(search_response['pageNumber'], search_response['start'], search_response['end'], search_response['totalResults']))
    for result in search_response['results']:
        job_dict[result['jobkey']] = result['jobtitle']
    if search_response['totalResults'] > search_response['end']:
        params['start'] = search_response['end']
    else: break

for val in sorted(job_dict.values()):
    print(val) # printing out job titles to sanity check data 
