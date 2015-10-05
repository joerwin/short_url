class UrlEncoder:

    _CIPHER_MAP = list("23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_");
    BASE = len(_CIPHER_MAP); 

    # Converts an integer ID to a short URL string
    def encode(self, num):
        retc = ""
        if num == 0:
            return self._CIPHER_MAP[0]
        while(num > 0):
            #Prepend the new character to string 
            retc = self._CIPHER_MAP[num % self.BASE] + retc
            num = num / self.BASE
        return retc

    # Converts an back to an integer ID 
    # Uses the provided alphabet and Creates a base BASE number from the offset of the character in the ALPHABET
    def decode(self, string):
        num = 0;
        #Iterate characters in string 
        for char in list(string):
            if char not in self._CIPHER_MAP:
                return None
            #Converts exisitng number to a base BASE number and then adds the index of this character
            num = num * self.BASE + self._CIPHER_MAP.index(char);
        return num
