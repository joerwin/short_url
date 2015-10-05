from nose.tools import *
import cherrypy
from cherrypy.test import helper
from run import ShortUrl
import run 
import unittest
from rfc3987 import parse

#helper.CPWebCase
class TestShortUrl():

    def testIsValidUrl(self):
    #     validUrl = "http://example.com"
    #     invalidUrl = "justa random string"
    #     invalidUrl2 = "not A real"
    #     assert(run.is_valid_url(validUrl))
    #     #try:
        print("TEST")
    #     #print(parse(invalidUrl2, rule='absolute_URI'))
    #     # print(bool(parse(invalidUrl2, rule='URI')))
    #     print(run.is_valid_url(invalidUrl2))
    #     eq_(run.is_valid_url(invalidUrl2), False, invalidUrl2 + " should be an invalid URL")



    # def testGetUrl(self):
    #     print("RUNNING A TEST");
    #     helper.CPWebCase.getPage('/');
    #     helper.CPWebCase.assertStatus('302')
    #     helper.CPWebCase.assertHeader('Location', 'http://google.com')

    # def setUp():    
    #     print("STARTING SERVER");
    #     cherrypy.tree.mount(
    #         ShortUrl(), '/',
    #         {'/':
    #          {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    #      }
    #     )
    #     print("STARTING SERVICE")
    #     cherrypy.engine.start()

    # setUp = staticmethod(setUp)

    # def teardown(self): 
    #     print("ENDIONG TESTS");
    #     cherrypy.engine.exit()

