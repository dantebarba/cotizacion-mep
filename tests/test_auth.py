import context
import cotizacion_mep.model.authentication as authen
import unittest

class AuthTestSuite(unittest.TestCase):
    """ Test auth class """

    def test_expiration(self):
        auth = authen.Authentication("Bearer", "Token", "Mon, 20 Mar 2017 15:44:59 GMT")
        self.assertIs(auth.is_expired(), True, "Auth must be expired")


if __name__ == '__main__':
    unittest.main()