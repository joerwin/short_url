import cherrypy
import uuid
from app.database.impl.ShortUrlDaoSqlLiteImpl import ShortUrlDaoSqlLiteImpl
from app.UrlEncoder import UrlEncoder

class ShortUrl:

    exposed = True

    def __init__(self):
        self.dao = ShortUrlDaoSqlLiteImpl()
        self.encoder = UrlEncoder()

    def GET(self, encodedUrl):
        real_url = self.dao.find(encodedUrl)
        if real_url != None:
            cherrypy.log("REDIRECTING TO " + real_url)
            raise cherrypy.HTTPRedirect(real_url, 302)
        else:
            cherrypy.response.status = "404" #Not found
            return "%s: NOT FOUND" % encodedUrl

    def POST(self, url): 
        try:
            id = self.dao.create(url)
            cherrypy.response.status = "201" #Created
            return "http://%s/%s" % (cherrypy.request.headers['host'], id);
        except Exception, e:
            cherrypy.log("ERROR CREATING SHORT URL", traceback=True )
            cherrypy.response.status = "500" #Created
            return "error creating a short URL"
            
    def DELETE(self, shortPath):
        self.dao.delete(shortPath)
        cherrypy.response.status = "204" #Success but No Contenta
        return "DELETE"
