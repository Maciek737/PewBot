#Subscribe to PewDiePie

import tweepy, ntplib, datetime, requests, math, Tkinter, urllib2, time
from bs4 import BeautifulSoup
import requests
from credentials import *
from apscheduler.schedulers.blocking import BlockingScheduler




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Check if correct account
user = api.me()
print (user.name)


def get_time():
	ntp = ntplib.NTPClient()
	rep = ntp.request('us.pool.ntp.org',version=3)
	print datetime.fromtimestamp(rep.tx_time, timezone.est)



def get_pewdiepie_subs():
	# specify the url
	URL = 'https://socialblade.com/youtube/user/pewdiepie/realtime'
	req = requests.get(URL)
	soup = BeautifulSoup(req.text, 'html.parser')

	# get the live subscriber count from the site 
	pew_subs = soup.find('p',{'id':'rawCount'}).get_text()
	print pew_subs
	return pew_subs


def get_tseries_subs():
	# specify the url
	URL = 'https://socialblade.com/youtube/user/tseries/realtime'
	req = requests.get(URL)

	# get the live subscriber count from the site
	soup = BeautifulSoup(req.text, 'html.parser')
	t_subs = soup.find('p',{'id':'rawCount'}).get_text()
	print t_subs
	return t_subs

if __name__ == "__main__":
	p = int(get_pewdiepie_subs())
	t = int(get_tseries_subs())
	d = p-t

	pew = ('PewDiePie: '+ "{:,}".format(p))
	ts = ('T-Series: '+ "{:,}".format(t))
	dif = ('Difference: '+ "{:,}".format(d))

	with open('temp.txt', 'w') as f:
		f.write(pew +'\n' + ts +'\n' + dif +'\n')
	with open('temp.txt','r') as f:
		api.update_status(f.read())

	sleep(900)

	##api.update_status(pew+ts+dif)
	#print "Hello " + api.me().name



scheduler = BlockingScheduler()
scheduler.add_job(get_pewdiepie_subs, 'interval', minutes=5)

#page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
#soup = BeautifulSoup(page, 'html.parser')

#name_box = soup.find('h1', attrs={"class": "page-realtime-body"})

# get the sub count
#price_box = soup.find('div', attrs={'class':'page-realtime-body'})
#<p id="rawCount" style="display: none;">76087717</p>


#api.update_status('Hello World!')
#print "Hello " + api.me().name