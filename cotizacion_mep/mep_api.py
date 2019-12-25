import requests
import model.authentication as auth
import model.bond as bond
import model.mep_value as mep_value
import datetime

class IOL_MEP_Api():

    _authentication = None
    _URL = 'https://api.invertironline.com/'

    def __init__(self, credentials = {}):
        self._credentials = credentials

    def _do_auth(self):
        params = {"username" : self._credentials["username"], "password" : self._credentials["password"], "grant_type" : "password"}
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.post(self._URL + 'token', data=params, headers=headers)
        if (response.status_code != 200):
            raise StandardError("Login incorrecto")
        response = response.json()
        return auth.Authentication(response["access_token"], response["refresh_token"], response[".expires"])

    def authenticate(self): 
        if (self._authentication is None or self._authentication.expired()):
            self._authentication = self._do_auth()
        return self._authentication

    def _currency(self, moneda):
        return "USD" if moneda == "dolar_Estadounidense" else "ARS"

    def get_bonds(self, *args):
        auth = self.authenticate()
        bonds = []
        for bond_name in args:
            endpoint = "api/v2/bcba/titulos/" + bond_name + "/Cotizacion"
            headers = {"Authorization" : "Bearer "+auth.token()}
            response = requests.get(self._URL + endpoint, headers=headers)
            if (response.status_code != 200):
                raise StandardError("No se ha podido recuperar el bono")
            response = response.json()
            bonds.append(bond.Bond(bond_name, response["ultimoPrecio"], self._currency(response["moneda"]), response["fechaHora"]))
        return bonds

    def is_auth_expired(self):
        self._authentication.is_expired()


class MEP_Api():

    _strategy = None

    def __init__(self, credentials = {}):
        self._strategy = IOL_MEP_Api(credentials)

    def get_bonds(self):
        return self._strategy.get_bonds()

    def get_bonds_pair(self, ars_bond, usd_bond):
        return mep_value.MepValue(self._strategy.get_bonds(usd_bond)[0], self._strategy.get_bonds(ars_bond)[0],datetime.datetime.now())





