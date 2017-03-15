You will need to use regular expressions to interpret the data on Yelp pages.


Your script will get the forty highest rated restaurants in San Francisco from the search results (pages 1 through 4) of Yelp.  (You can figure out the URLs for pages 2 through four of the search results from the buttons on the first page or from the pattern in the URL.)  For each restaurant, your script will figure out how many reviews it has.

In the starter code, we read a page into a string and calls the preprocess_yelp_page function to preprocess the string before proceeding to BeautifulSoup.  Feel free to modify these four lines of code or write your own code, but do preprocess the page content for every web page your read.

Your script will create a text file named restaurants.<userID>.txt and write in this file each of the top 40 restaurant names followed by a comma followed by the number of reviews from the four results page, one line for each restaurant, in sorted order based on the number of reviews for each restaurant.  For example:

Ichido,50
Patisserie,1439

Note that a search result page may contain advertised results at the top of the page.  Perform a sanity check that confirms the number of restaurants you are counting is ten.  If you do encounter an advertised restaurant, figure out how to separate the advertised restaurants from the "real restaurant" results.

Note also that if you are running an ad blocker in your web browser you will likely see different results in the browser and the HTML downloaded by their code, so it we strongly suggest turning off the ad blocker temporarily.

When your program is complete, upload the hw5.<userID>.py and restaurants.<userID>.txt files using the file upload tool available at https://www.ischool.berkeley.edu/uploader/?s=i206  Login with your ISchool userid and password and follow the directions.

Extra Credit:

For extra credit, you can collect the same information in a different way, using the Yelp APIs.

Download the hw5xtracredit.py file from the Piazza Resources page, and rename it hw5xtracredit.<userID>.py

(Note that the extra credit script uses urllib2 rather than urllib for compatibility with the oath2 package).

Run the command pip install oauth2.

Go to http://www.yelp.com/developers and create an account.  Go to http://www.yelp.com/developers/manage_api_keys to generate your app key/secret and a token by providing a website URL (such as the ISchool website or a dummy URL) and giving the reason to use the APIs (homework assignment).  Copy the "Consumer Key", "Consumer Secret", "Token", and "Token Secret" into the relevant portions of the extra credit script.

Go to http://www.yelp.com/developers/documentation and learn how to build the URLs to use the Yelp Search and Business APIs.

You will need to form a URL and send it to the yelp_req function in the script we gave you to get the API response.  

(Hints:  Look at the parameters limit, offset, and sort in the Yelp API documentation.  Perform a Google search to find out how to percent-encode the parameters using urllib2.urlencode.  Many additional parameters are needed to be appended to the URL you form for the purpose of authentication.  Try printing the full URL in the HTTP request for yourself and see what parameters are included.)

The HTTP responses will be JSON strings.  Your program should go through them and produce the file restaurants2.<userID>.txt in the same format as restaurants.<userID>.txt

Upload your hw8xtracredit.<userID>.py and restaurants2.<userID>.txt using the usual process.
