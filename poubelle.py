self.checkBox_T2.stateChanged.connect(self.checkViewed)
self.pushButton_Reload.clicked.connect(self.clearData)



                if vu == 0:
                    vu = 'Non'
                elif vu == 1:
                    vu = 'Oui'




        dt = self.tableWidget_M.item(row, 2).text()
        print(row)
        print('id : ' + str(g))
        print('oui : ' + dt)

        if dt == 'Non':
            self.checkBox_T2.setChecked(False)
        elif dt == 'Oui':
            self.checkBox_T2.setChecked(True)



    
def checkViewed(self, state):

    self.conn = sqlite3.connect('movie.db')
    self.c = self.conn.cursor()
    row = self.tableWidget_M.currentRow()

    if self.checkBox_T2.isChecked:
        print('check')
        count = 1

        query = '''UPDATE movie SET vu = ? WHERE id = ?'''
        data = (count, row)
        self.c.execute(query, data)
    else:
        print('Uncheck')
        count = 0

        query = '''UPDATE movie SET vu = ? WHERE id = ?'''
        data = (count, row)
        self.c.execute(query, data)

    self.conn.commit()

    self.clearData()
