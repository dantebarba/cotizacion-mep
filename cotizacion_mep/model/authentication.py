import dateutil.parser as dateparser
import datetime

class Authentication():

    _DATE_FORMAT = "%a, %d %b %yyyy %H:%M:%S %Z"

    def __init__(self, bearer, refresh_token, expiration):
        self._bearer = bearer
        self._refresh_token = refresh_token
        self._expiration = expiration
    
    def expires_in(self):
        return self._expiration
    
    def token(self):
        return self._bearer

    def is_expired(self):
        expiration_date = dateparser.parse(self.expires_in(), ignoretz=True)
        return (datetime.datetime.utcnow() > expiration_date)

    
