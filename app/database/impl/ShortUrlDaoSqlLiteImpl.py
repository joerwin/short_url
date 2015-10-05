from app.database.shortUrlDAO import ShortUrlDAO
from app.UrlEncoder import UrlEncoder
import cherrypy
import sqlite3

class ShortUrlDaoSqlLiteImpl(ShortUrlDAO):

    def __init__(self):
        self.encoder = UrlEncoder()

    def _conn(self):
        return sqlite3.connect('.shorturls.sqlite3',
                               detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        
    def install_tables(self):
        conn = self._conn().cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS URLS(
        ID INTEGER PRIMARY KEY, URL TEXT, ENCODED_URL TEXT)''')
        conn.close()
        
    def find(self, encodedPath):
        conn = self._conn().cursor()
        lookupId = self.encoder.decode(encodedPath)
        query = "SELECT URL FROM URLS WHERE id = ?"
        conn.execute(query, (lookupId,))
        url = conn.fetchone()
        if url != None:
            url = url[0]
        conn.close() 
        return url;

    def find_by_decoded(self, decodedPath):
        print decodedPath
        conn = self._conn().cursor()
        query = "SELECT ENCODED_URL FROM URLS WHERE URL = ?"
        conn.execute(query, (decodedPath,))
        encoded_url = conn.fetchone()
        if encoded_url != None:
            encoded_url = encoded_url[0]
        conn.close() 
        return encoded_url;

    def create(self, url):
        encoded_path = self.find_by_decoded(url) 
        if encoded_path != None:
            return encoded_path;
        else:
            conn = self._conn()
            cursor = conn.cursor()
            insert = "INSERT INTO URLS (URL) VALUES(?)"
            update = "UPDATE URLS SET ENCODED_URL = ? WHERE ID = ?" 
            cursor.execute(insert, (url,))
            encoded_path = self.encoder.encode(cursor.lastrowid)
            cursor.execute(update, (encoded_path, cursor.lastrowid))
            conn.commit()
            conn.close()
            return encoded_path

    def delete(self, encodedPath):
        conn = self._conn()
        delete = "DELETE FROM URLS WHERE encoded_url = ?" 
        conn.execute(delete, (encodedPath,))
        conn.commit()
        conn.close()
