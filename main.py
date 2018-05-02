import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import urllib2
from bs4 import BeautifulSoup
import re

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

quote_page = 'https://www.imdb.com/search/title?title_type=feature&sort=num_votes,desc'

title = 'http://www.imdb.com'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')


name_box = soup.find_all('a', attrs={'href' : re.compile("_tt$")})

count = 0
url=[]
for name in name_box:
    url.append(name.get('href'))

MovieRating = {}
R=[]
V=[]
M=[]

for link in url:
    quote_page = title+link
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find('h1', attrs={'itemprop' : 'name'})
    
    Mname = []
    #name = name.string
    for x in name:
      if x!= '<':
        Mname.append(x)
      elif x=='<':
        break
    name = Mname[0]
    #name = ''.join(Mname)
    rating = soup.find('span', attrs={'itemprop' : 'ratingValue'})
    rating = rating.string
    votes = soup.find('span', attrs={'itemprop' : 'ratingCount'})
    votes = votes.string
    votes = votes.replace(",","")
    #print name+" : "+rating+" "+votes
    M.append(name)
    R.append(float(rating.encode('utf-8')))
    V.append(int(votes.encode('utf-8')))
    temp = float((float(rating.encode('utf-8')))*(int(votes.encode('utf-8'))))
    MovieRating[name] = temp

#print MovieRating

#R.sort()
#V.sort()
#print R
#print V
mean = sum(V[0:len(V)])

for key, value in MovieRating.iteritems():
  MovieRating[key] = round(value/mean *100,3)

ax.plot(R,V,'ro')
p=0
for xy in zip(R, V):
  ax.annotate('%s' % M[p], xy=xy, textcoords='data')
  p=p+1

fig.savefig('graph.png')

#for key, value in MovieRating.iteritems():
#  print key +' : '+ str(value) 

for key, value in sorted(MovieRating.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
