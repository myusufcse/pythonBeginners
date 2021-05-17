import requests
import re

url = "https://jsonmock.hackerrank.com/api/movies"
year = '2000'
query = "harry*"
querystring = {"Year": year, "page": "1"}

headers = {}

response = requests.request("GET", url, headers=headers, params=querystring)
respJson = response.json()
movies = []
# print(resjs)
totalPage = respJson['total_pages']
movies += respJson['data']
for i in range(2, totalPage + 1):
    querystring = {"Year": year, "page": i}
    response = requests.request("GET", url, headers=headers, params=querystring)
    respJson = response.json()
    movies += respJson['data']
p = re.compile(query, re.IGNORECASE)
yourMovies = []
for movie in movies:
    # print(movie)
    if p.match(movie['Title']):
        temp = [movie['imdbID'], movie['Title']]
        yourMovies += [temp]

print(*yourMovies, sep="\n")
# print(movies)
# print(movies[0])
'''
chech https://www.slideshare.net/HammadAli89/presentations/2 & geeks4geeks
for studying algorithm
'''
