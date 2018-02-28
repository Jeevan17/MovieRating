import urllib2
from bs4 import BeautifulSoup
import re

#quote_page = 'http://www.imdb.com/search/title?title_type=tv_series&sort=user_rating,desc'
quote_page = 'http://www.imdb.com/search/title?title_type=tv_series&sort=user_rating,desc&page=1&ref_=adv_nxt'
#quote_page = 'http://www.imdb.com/search/title?title_type=tv_series&sort=user_rating,desc&page=3&ref_=adv_nxt'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

#name_box = soup.find('h3', attrs={'class': 'lister-item-header'})

name_box = soup.find_all('a', attrs={'href' : re.compile("_tt$")})

count = 0
#link=[]
for name in name_box:
	#link.append(name.get('href'))
	print name.get('href')
	count+=1
#name = name_box.text.strip()
print count
#print name_box
