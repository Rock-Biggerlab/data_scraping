__author__ = 'LilyDu'



#Tutorial -- How to fetch data from Sina Weibo



""" How to download canopy """
#Go to https://www.enthought.com/canopy-express/ and click "download free"
#After that, open canopy and click on "create a new file"
""" How to download canopy"""



""" How to get the data from Weibo and view it online """
#Go to "http://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI" to get a list of commands of how to deal with data from Weibo
#Parameters are available online and by stringing all parameters together, we could get access to data

#E.g.
#Note that just by pasting "https://api.weibo.com/2/place/pois/photos.json?", you will receive an error saying that appkey is missing.
#By adding "https://api.weibo.com/2/place/pois/photos.json?access_token=2.00juYUmF0dYhVk4f50df99a8UEuKkD&poiid=B2094757DA6EA4FD4092&count=50&page=1" where necessary parameters are connected using "&" and access token and poiid are required for accessing a website, count means how many results you get at one time, page means which page of the data you want (if the actual results exceeds the count that you've set)
#After that, if the resulting page is hard to recognize, then go to "http://json.parser.online.fr/" and translate the page into a better format.
""" How to get the data from Weibo and view it online """



""" How to get the same data using urllib2 """
#First import all libraries that are needed
import urllib2
import json
import time

#Set a variable for the target URL
baseUrl = "https://api.weibo.com/2/place/pois/photos.json"

#Access Token & Poiid are necessary for accessing a certain URL
accessToken = "2.00juYUmF0dYhVk4f50df99a8UEuKkD"
poiid = "B2094757DA6EA4FD4092"

#Count means the number of results you get at one time, normally 50
count = "50"

#Page means which page of the data you want to check. (For example, if you set the count to 50 and receive 200 data, then there will be 4 pages and you need to choose which page you want to see.)
page = "1"

#By using a format to add up and create the url, a change in each separate variable will result in a change in the url.
url = baseUrl + "?" + "access_token=" + accessToken + "&poiid=" + poiid + "&count=" + count + "&page=" + page

#By copying and pasting the resulting URL, you could get the same result as the above way of accessing web page.
print url


#"def" means function
#Here, function fetch is set and 
def fetch():
    response = urllib2.urlopen(url)
    data = response.read()
    parsedData = json.loads(data)
    
    time.sleep(24)
    
    return parsedData
print data




numPosts = parsedData["total_number"]

print numPosts

posts = parsedData["statuses"]

print len(posts)

for post in posts:
    uid = post["user"]["id"]
    print uid