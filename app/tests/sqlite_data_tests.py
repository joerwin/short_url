from nose.tools import *
from app.UrlEncoder import UrlEncoder
from app.database.impl.ShortUrlDaoSqlLiteImpl import ShortUrlDaoSqlLiteImpl
import os 
class TestDataAccess():
    """This is more of an integration test than a unit test"""

    def setUp(self):
        self.dao = ShortUrlDaoSqlLiteImpl()
        self.dao.install_tables()
        self.encoder = UrlEncoder()

    def tearDown(self):
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "REMOVING DB"
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        os.remove(".shorturls.sqlite3")

    def testCreateReturnsIncrementingId(self):
        print "================================================================================"
        print "IT = %s " % self.dao.create("http://myUrl")
        print "================================================================================"
        eq_(u'3', self.dao.create("http://myUrl"), "First insert should be encoded to 3");
        eq_(u'4', self.dao.create("http://myUrl2"), "Second insert should be encoded to 4");


    def testCreateAndFind(self):
        url = "http://example.com/some/path"
        encoded = self.dao.create(url)
        eq_(url, self.dao.find(encoded), "should retrieve the full url")

    def testFindReturnsNone(self):
        encoded = self.encoder.encode(9999)
        eq_(None, self.dao.find(encoded), "should retrieve None if it is not in the database")


    def testDeleteExisting(self):
        url = "http://example.com/some/path"
        encodedReference = self.dao.create(url)
        ok_(self.dao.find(encodedReference) != None, "Url should be in the database")
        self.dao.delete(encodedReference)
        ok_(self.dao.find(encodedReference) == None, "Url should hve been removed from  the database")


    def testDeleteNonExistent(self):
        encodedReference = self.encoder.encode(9999)
        #Should not throw exception
        self.dao.delete(encodedReference)
        ok_(self.dao.find(encodedReference) == None, "Url should hve been removed from  the database")
        
