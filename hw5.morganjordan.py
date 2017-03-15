# name: Morgan Jordan
# morgan.jordan@berkeley.edu

import sys
import urllib.request as req
from bs4 import BeautifulSoup
import operator

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.decode().split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code
def start_page():
	""" assigns the first page for scraping, collects follow-on links on the page;
	Outputs the start-page, all follow on pages, and the BS4 soup of the first page"""
	url = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=0#'
	try:
		content = req.urlopen(url).read()
		content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
	except:
		print("Oops! url not found. Please confirm the url, or check your internet connection.")
		exit()
	try:
		soup = BeautifulSoup(content, 'html.parser')
	except:
		print("Error. Confirm you have Beautiful Soup installed!")
	captcha_check(soup)
	follow_on = soup.find_all('a', class_ = 'available-number pagination-links_anchor')
	return url, follow_on, soup

def captcha_check(soup):
	check = []
	captcha_check = soup.find('title')
	for item in captcha_check:
		check.append(item)
	if check[0] == "Yelp Captcha":
		print("You've likely encountered a Captcha Page! \nCheck that yelp.com has not blocked you from scraping. \nIf you're prompted by a Captcha in the browser, change subnets.")
		exit()

def parse_pages():
	""" puts all the pages into one list, then collects the business names and review quantity from 
	each restaurant into lists; special attention taken to match format from example output
	This function outputs a dictionary of {restaurant: review count}"""
	results = {}
	all_pages = []
	restaurants = []
	just_rev_count = []
	url, follow_on, soup = start_page()
	all_pages.append(url)
	
	for i, a in enumerate(follow_on):
		source = a['href'] # Get the remaining url attribute from the tag
		page = 'http://www.yelp.com/' + source # Combine the src into a full address
		all_pages.append(page)

	for page in all_pages:
		content = req.urlopen(page).read()
		content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
		soup = BeautifulSoup(content, 'html.parser')
		
		links_biz = soup.find_all('span', class_ = 'indexed-biz-name') #all the <a> tags that have the buisness name; creates a BS object
		follow_on_restaurant = [tag.text for tag in links_biz] #removes the tags from around the restaurant name and stores them in a list
		for restaurant in follow_on_restaurant:
			restaurants.append(str(restaurant[11:])) #strip off the leading Restaurant# in the search results and add it to list
		
		review_count = soup.find_all('span', class_ = 'review-count rating-qualifier') #all the <span>No. of reviews</span> for each restaurant; creates BS object
		reviews = [tag.text for tag in review_count] #removes the span tag, leaving only e.g. '240 reviews'
		for item in reviews:
			just_rev_count.append(int(item[:-8])) #removes the 'reviews' text and converts the number into an integer; I could put this on line 29 tag.text[:-8], but I want to retain readability if I come back to this script in the future	
	
	restaurants = [item.lstrip(' ') for item in restaurants] #strip the leading space off some restr names, to match the example output
	results = dict(zip(restaurants, just_rev_count))
	return results

def rest_text():
	"""gets the returned results from parse_page(), 
	sorts the dictionary by greatest to least value, strips it 
	of extra-chracters, and writes it to file""" 
	dict_ = parse_pages()
	sort_list = sorted(dict_.items(), key=operator.itemgetter(1), reverse=True)
	with open('restaurants.morganjordan.txt', 'w+') as file_handle:
		for item in sort_list:
			file_handle.write("".join(str(item).replace('(', '').replace(')', '').replace('\'', '').replace(', ', ',')) + "\n")
	

def main():
	rest_text()

if __name__ == '__main__':
	main()


