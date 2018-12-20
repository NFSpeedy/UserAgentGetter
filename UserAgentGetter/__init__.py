# import requests as re, json, time, random, os
# from bs4 import BeautifulSoup as bs
# from UserAgentGetter.UserAgentGetter import UserAgentGetter

name = "UserAgentGetter"
import requests as re, json, time, random, os
from bs4 import BeautifulSoup as bs
from pprint import pprint

"""UserAgentGetter is a simple package which provides"""
def newUA():
    data = {}
    resp = re.get("https://techblog.willshouse.com/2012/01/03/most-common-user-agents/", params={
        'Host':'techblog.willshouse.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'en-US,en;q=0.5',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
    })
    soup = bs(resp.text, "lxml")
    div = soup.select('.useragent')
    i = 0
    for row in div[1:21]:
        data[i]=row.text
        i+=1
    data['time'] = time.time()
    file = open(os.path.join(os.path.dirname(__file__), 'ua.json'), "w+")
    file.write(json.dumps(data))
    file.close()
def UA():
    #try:
    json_ua = open(os.path.join(os.path.dirname(__file__), "ua.json"), "r")
    ua = json.loads(json_ua.read())
    json_ua.close()
    #except:
     #   print("except")
      #  self.newUA()
       # file = open("ua.json", "r")
        #ua = json.loads(file.read())
        #file.close()
    # print(ua['time']+60 < time.time())
    if ua['time']+3*30*24*60*60 < time.time():
    #if ua['time']+60 < time.time():
        newUA()
    return ua[str(random.randint(0,len(ua)-2))]
    # return ua[str(0)]

#ua = UserAgentGetter()

#print(ua.UA())
