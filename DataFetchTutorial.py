__author__ = 'LilyDu'

#Tutorial -- How to fetch data from Sina Weibo

""" How to download canopy"""
#Go to https://www.enthought.com/canopy-express/ and click "download free"
#After that, open canopy and click on "create a new file"
""" How to download canopy"""

#Go to "open.weibo.com/wiki/微博API" to get a list of commands of how to deal with data from Weibo

#First set a variable for the target URL
baseUrl = "https://api.weibo.com/2/place/pois/photos.json"

#Access Token & Poiid are necessary for accessing a certain URL
accessToken = "2.00juYUmF0dYhVk4f50df99a8UEuKkD"
poiid = "B2094757DA6EA4FD4092"

#Count means the
count = "50"
page = "1"

url = baseUrl + "?" + "access_token=" + accessToken + "&poiid=" + poiid + "&count=" + count + "&page=" + page

print url


import urllib2
import json
import time

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