from indeed import IndeedClient

# set up API connection and initial query
client = IndeedClient(publisher=4201738803816157)

default_params = {
    'q': "python",
    'l': "53562",
    'userip': "1.2.3.4", # testing value
    'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)" # testing value
}

def find_all_jobs(params):
    job_dict = dict() # create empty dictionary to hold job results
    start = 0 # initialize start variable so it can be used in while loop
    while True:
        paged_response = search_by_page(params, start)
        extract_job_keys(paged_response, job_dict)
        if paged_response['totalResults'] > paged_response['end']:
            start = paged_response['end']
        else: break
    return job_dict

def search_by_page(params, start=0):
    params['start'] = start
    search_response = client.search(**params)
    print("Page #{}. Start {}. End {}. Total {}.".format(search_response['pageNumber'], search_response['start'], search_response['end'], search_response['totalResults']))
    return search_response

def extract_job_keys(search_response, job_dict):
    for result in search_response['results']:
        job_dict[result['jobkey']] = result['jobtitle']

job_dict = find_all_jobs(default_params)
    

for val in sorted(job_dict.values()):
    print(val) # print out job titles to sanity check data 
