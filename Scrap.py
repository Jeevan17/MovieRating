from random import randint
import urllib2
from bs4 import BeautifulSoup
import re
# import json
# import pandas as pd

quote_page = 'https://www.imdb.com/search/title?title_type=feature&sort=num_votes,desc&page=1&ref_=adv_nxt'

#title = 'http://www.imdb.com'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

# pages = soup.find('div', class_ = 'desc')
# pages = pages.text
# pages = pages.split(' ')
# pages = pages[26].replace(",","").encode('utf-8')
# pages = int(pages) + 1
# print pages

pages = 201

photo_link = []
movie_name = []
imdb_rating = []
imdb_votes = []
#imdb_metascore = []
out = open('movies_scrap.txt','w')

for i in range(1,pages):
	j = str(i)
	quote_page = 'https://www.imdb.com/search/title?title_type=feature&sort=num_votes,desc&page='+j+'&ref_=adv_nxt'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')

	movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')
	for first_movie in movie_containers:
		#first_movie = movie_containers[0]
		file = ''
		
		#Scraping photo link
		temp = first_movie.a.img['loadlate']
		photo_link.append(temp)

		#Scraping Name
		temp = first_movie.h3.a.text
		temp = temp.split(',')
		temp = ''.join(temp)
		movie_name.append(temp)
		file +=temp+','

		#Scraping Rating
		#temp = float(first_movie.strong.text)
		temp = first_movie.strong.text
		imdb_rating.append(temp)
		file +=temp+','
		
		#Scraping MetaScore
		# temp = first_movie.find('span', class_ = 'metascore favorable')
		# temp = int(temp.text)
		# imdb_metascore.append(temp)

		#Scraping Votes
		temp = first_movie.find('span', attrs = {'name':'nv'})
		#temp = int(temp['data-value'])
		temp = temp['data-value']
		imdb_votes.append(temp)
		file +=temp+'\n'

		#print file
		out.write(''.join(file.encode('utf-8')))

# test_df = pd.DataFrame({'Title': movie_name,
#                        'IMDB Rating': imdb_rating,
#                        'Number of Votes': imdb_votes})
# print(test_df.info())
# print test_df