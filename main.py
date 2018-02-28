import urllib2
from bs4 import BeautifulSoup

quote_page = 'http://www.imdb.com/search/title?title_type=tv_series'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

#name_box = soup.find('h3', attrs={'class': 'lister-item-header','href' : '/title/tt2261227/?ref_=adv_li_tt'})

name_box = soup.find_all('a', attrs={'href' : '/title/tt2261227/?ref_=adv_li_tt'})

#name = name_box.text.strip()

print name_box