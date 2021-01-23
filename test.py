# pip install beautifulsoup4
# pip install omdbapi

from bs4 import BeautifulSoup
import codecs
from omdbapi.movie_search import GetMovie
import csv

f=codecs.open("imdb_most_popular_movies_dump.html", 'r', 'utf-8')
document = BeautifulSoup(f.read(), 'html.parser')

movies = document.select('td.titleColumn a')

movie_list = []

for index in range(0, len(movies)):
    movie_name = movies[index].get_text()
    movie_list.append(movie_name)
    
movie_details = []

for title in movie_list:
    # API KEY - http://www.omdbapi.com/apikey.aspx
    movie_info = GetMovie(title=title, api_key='')
    mv = movie_info.get_all_data()
    movie_details.append(mv)

i = 0

with open('info.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(movie_details[0].keys())
    for item in movie_details:
        writer.writerow(movie_details[i].values())
        i += 1