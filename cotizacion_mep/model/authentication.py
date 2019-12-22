class Authentication():
    def __init__(self, bearer, refresh_token, expiration):
        self._bearer = bearer
        self._refresh_token = refresh_token
        self._expiration = expiration
    
    def expires_in(self):
        return self._expiration

    def expired(self):
        ''' mocked '''
        return False
    
    def token(self):
        return self._bearer
    
