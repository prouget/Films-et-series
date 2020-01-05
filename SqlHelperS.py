import sqlite3

class SqlHelperS:

    def __init__(self,name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            # print(sqlite3.version)
        except sqlite3.Error as e:
            print("Connexion Impossible...")

    def create_table(self):
        c = self.cursor
        c.execute('''CREATE TABLE IF NOT EXISTS serie (
                    serieid INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    poster TEXT,
                    idtv TEXT)''')

        c.execute('''CREATE TABLE IF NOT EXISTS season (
                    episodeid INTEGER PRIMARY KEY AUTOINCREMENT,
                    seaon INTEGER,
                    episode INTEGER,
                    episodetitle TEXT,
                    episodeview INTEGER DEFAULT 0,
                    FOREIGN KEY (episodeid) REFERENCES serie (serieid))''')

    def editSerie(self, g, serieid, title, img, idtv):#INSERT & UPDATE
        c = self.cursor
        data = (g, title, img, idtv)
        c.execute('''INSERT INTO serie (serieid, title, poster, idtv) VALUES (?, ?, ?, ?)''', (data))
        self.conn.commit()
                
    def editSeason(self, g, season, episode, episodetitle, episodeview):#INSERT & UPDATE
        c = self.cursor
        data = (g, season, episode, episodetitle, episodeview)
        c.execute('''INSERT INTO season (episodeid, episode, episodetitle, episodeview) VALUES (?, ?, ?, ?)''', (data))
        self.conn.commit()

    def select(self,query):#SELECT
        c = self.cursor
        c.execute(query)
        return c.fetchall()


# test = SqlHelperS("serie.db")
# test.create_table()

#test.edit("INSERT INTO users (name,year,admin) VALUES ('john',1992,0) ")
