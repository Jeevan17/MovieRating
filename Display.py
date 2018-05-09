import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from random import randint


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

inp = open('movies_scrap.txt','r')
out = open('movies_scraped.txt','w')

photo_link = []
movie_name = []
imdb_rating = []
imdb_votes = []
test = []
MovieRating = {}
#imdb_metascore = []
for j in inp.readlines():
	temp = j.split(',')
	if float(temp[1]) >= 4.0 and int(temp[2]) >= 1000:
		movie_name.append(temp[0])
		imdb_rating.append(float(temp[1]))
		imdb_votes.append(int(temp[2]))
		MovieRating[temp[0]] = float((float(temp[1]))*(int(temp[2])))
		test.append(float((float(temp[1]))*(int(temp[2]))))
		

mean = sum(test[0:len(test)])
mean = round(mean/len(test),3)

for key, value in MovieRating.iteritems():
	#MovieRating[key] = round(value/mean *100,3)
	MovieRating[key] = value/mean *100

#for key, value in MovieRating.iteritems():
#  print key +' : '+ str(value) 
i=1
for key, value in sorted(MovieRating.iteritems(), key=lambda (k,v): (v,k),reverse=True):
	# print key
	file = ''
	file = str(i)+')  '+str(key)+' : '+str(value)+'\n'
	out.write(''.join(file))
	print "%d) %s : %s" % (i, key, value)
	# if i == 100:
	# 	break
	i = i + 1