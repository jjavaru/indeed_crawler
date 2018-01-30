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
