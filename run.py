import cherrypy
import os.path

from  app.ShortUrl import ShortUrl

if __name__ == '__main__':
    cherrypy.config.update("%s/%s" % (os.path.dirname(os.path.abspath(__file__)), 'global_config'))

    cherrypy.tree.mount(
        ShortUrl(), '',
        {'/':
         {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
     }
    )
    
    cherrypy.engine.start()
    cherrypy.engine.block()
