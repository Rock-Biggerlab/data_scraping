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
import json             #json makes sure that we could get the useful data from all info that we get
import time             #time is necessary for using time delay which is closely associated with web
import math             #math just provides more math functions

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



#"def" means function
def fetch(url):
#    libraryName.functionName() can use a function that is specific to that library
#    in this case, urlopen takes in the url as input and it gives you whatever data that comes back as an output
    response = urllib2.urlopen(url)
#    read function basically converts everything it takes in into plain text that is readable
    data = response.read()
#    after using json, you should get a well structured data set
    parsedData = json.loads(data)
#    time delay just pause the whole process for 2 seconds(in this case)and then continues to run the project
    time.sleep(2)
    
    return parsedData



#If you look through our example, you should find a key called "total_number" at the bottom of each piece and so by searching the key, we get the specific content that is in the key
numPosts = fetch(url)["total_number"]

#float just converts integers into floats so that the result can also be floats and not rounded value
#math.ceiling just make sure that the result of the division is round up so that we do not miss any page
numPages = int(math.ceil(float(numPosts) / float(count)))

for i in range(numPages):
#    By declaring the variable again you change the value of the variable
    page = str(i + 1)

#    This is the same way with another key
    posts = fetch(url)["statuses"]

#    len function is used to count the number of objects in the array posts
    print len(posts)

#    for is used to loop through all collection of posts

    for post in posts:
#        This means that you first dig into posts to find "user" and then dig into "user" to find "id"
#        Since this is in the for loop, it will print each uid in each posts
#        By using try function: try the thing in the function, if it works well, then that's great, if there is an error, then skip it.
        try:
            uid = post["user"]["id"]
        except:
            print "user id error!"
            uid = " "
        
        print uid

#By copying and pasting the resulting URL, you could get the same result as the above way of accessing web page.
print url