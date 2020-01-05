import requests
import json

# -----------------
# ----- FILMS -----
# -----------------


def searchMovie(name):
    key = '24d8d681a05bd7818f3622afee784c45'
    query = name
    r = requests.get('https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(key, query))
    data = r.json()
    return data

def searchMovieD(id):
    key = '24d8d681a05bd7818f3622afee784c45'
    data = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(id, key))
    r = data.json()
    return data

def movie(name):
    tm = searchMovie(name)
    data = []
    result_length = tm['total_results']

    if result_length == 0:
        return 'pas de réponses'
    else:
        for each in tm['results']:
            r = [each['title'], each['release_date'][0:4], str(each['id'])]
            data.append(r)
    return data

def movieDescription(id):
    key = '24d8d681a05bd7818f3622afee784c45'
    data = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=fr'.format(id, key))
    tm = data.json()

    r = [tm['title'], tm['release_date'][0:4], tm['overview'], tm['poster_path']]
    return r


# ------------------
# ----- SERIES -----
# ------------------


# def searchSerie(name):
#     key = '24d8d681a05bd7818f3622afee784c45'
#     query = name
#     r = requests.get('https://api.thetvdb.com/search/series?name={}'.format(query))
#     print(r)
#     data = r.json()
#     print(data)
#     # return data

# searchSerie('fringe')