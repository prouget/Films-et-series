import json
import tvdbsimple as tvdb
import SqlHelperS
tvdb.KEYS.API_KEY = 'c6562840423d4affd1a72bcd7aca75ca'


def serieById(idSerie):
    show = tvdb.Series(idSerie)
    response = show.info()

    idt = response['id']
    nam = response['seriesName']
    sea = response['season']
    sta = response['status']

    series = {
        'id'     : idt,
        'name'   : nam,
        'season' : sea,
        'status' : sta
    }
    name = 'jsonData/' + nam + '.json'

    with open(name, 'w') as json_file:
        json.dump(series, json_file)


def serieEpisode(idSerie, name):
    show = tvdb.Series(idSerie)
    episodes = show.Episodes.all()

    seasonE = []

    for ep in episodes:
        couple = [ep['airedSeason'], ep['airedEpisodeNumber'], ep['episodeName']]
        seasonE.append(couple)   

    print(seasonE)


def serieSearch(name):
    search = tvdb.Search()
    reponse = search.series(name)

    idtv = search.series[0]['id']
    title = search.series[0]['seriesName']
    poster = search.series[0]['banner']
    print(idtv, title, poster)
    serieEpisode(idtv, reponse)
    