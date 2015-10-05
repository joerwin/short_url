from nose.tools import *
from app.UrlEncoder import UrlEncoder
import sys

class TestUrlEncoding():

    def setUp(self):
        self.encoder = UrlEncoder()

    def testEncodeDecode0(self):
        print self.encoder.encode(0)
        eq_(self.encoder.encode(0),self.encoder._CIPHER_MAP[0],"0 should always come back as the first element in the cipher map")
        eq_(self.encoder.decode(self.encoder._CIPHER_MAP[0]),0,"first element in the cipher map should always = 0")


    def testCanHandleMaxInt(self):
        num = sys.maxint
        #Should not throw an exception
        encoded = self.encoder.encode(num)
        eq_(self.encoder.encode(num), encoded, "0 should always come back as the first element in the cipher map")
        eq_(self.encoder.decode(encoded), sys.maxint, "Should decode to max int")

    def testDecodeUnmappedCharacters(self):
        #Should not throw an exception
        encoded = self.encoder.decode("aeiouy")
        eq_(None, encoded, "Invalid string should not decode")
        
        
