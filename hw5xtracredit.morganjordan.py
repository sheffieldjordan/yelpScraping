 # name: Morgan Jordan
# morgan.jordan@berkeley.edu

import urllib.request as req
import json
import oauth2
from yelp.oauth1_authenticator import Oauth1Authenticator


# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = ''
CONSUMER_SECRET = '-Z2-k'
TOKEN = 'Ab7amphS-U-9QZwqPvIsS7'
TOKEN_SECRET = 'DOAhykv4z9w'

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API

def yelp_req(url):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = req.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read().decode('utf8'))

    finally:
        conn.close()
    
    return response
    
#################################################################################
# Your code goes here
# print(yelp_req('http://api.yelp.com/v2/search?term=restaurant&location=San+Francisco'))
def parse_page():
    """code does not run, but reflects how I would
    plan to format, once I figure out how to read the 
    data from the json object"""
    rev_count_all = []
    restaurants_all = []
    response = yelp_req('http://api.yelp.com/v2/search?term=restaurant&location=San+Francisco')
    for entry in response[businesses]:
        rev_count_all.append(response[businesses][[review_count]])
        restaurants_all.append(response[businesses][name])
    results = dict(zip(restaurants_all, rev_count_all))
    sort_list = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
    with open('restaurants2.morganjordan.txt', 'w+') as file_handle:
        for item in sort_list:
            file_handle.write("".join(str(item).replace('(', '').replace(')', '').replace('\'', '').replace(', ', ',')) + "\n")
    
def main():
    print(parse_page())

if __name__ == '__main__':
    main()
