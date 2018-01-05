import sqlite3
import datetime
from config import Database_path
import numpy as np


# Store to Database
class DB:
    def __init__(self,cpu,memory ,uptime,ip):
        try:
            db = sqlite3.connect(Database_path)
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS  statistics
                                (PID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                CLIENT_IP VARCHAR(100),
                                CPU FLOAT,                                                              
                                RAM FLOAT,
                                UPTIME FLOAT,
                                sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)''')
            timestamp = str(datetime.datetime.now())
            params = (ip, np.mean(cpu), memory,uptime, timestamp)
            cursor.execute('''INSERT INTO statistics (CLIENT_IP,CPU,RAM,UPTIME,sqltime) values(?,?,?,?,?)''', params)

            db.commit()
            cursor.close()
        except :
            print "there is an error in connecting to database"