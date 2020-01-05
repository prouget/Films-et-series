import sqlite3

class SqlHelperM:

    def __init__(self, name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except sqlite3.Error as e:
            print("Connexion Impossible..." + e)

    def create_table(self):
        c = self.cursor
        c.execute('''CREATE TABLE IF NOT EXISTS movie(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                id_tmdb TEXT,
                title TEXT,
                image TEXT,
                vu INTEGER DEFAULT 0)
                ''')
                
    def edit(self, g, title, img):#INSERT & UPDATE
        c = self.cursor
        data = (g, title, img)
        c.execute('''INSERT INTO movie (id_tmdb, title, image) VALUES (?, ?, ?)''', (data))
        self.conn.commit()

    def select(self,query):#SELECT
        c = self.cursor
        c.execute(query)
        return c.fetchall()
