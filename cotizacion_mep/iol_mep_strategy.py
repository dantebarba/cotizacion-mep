import datetime
import requests
import model.authentication as auth
import model.bond as bond
import cotizacion_mep.mep_api_strategy as strategy


class IolMEPStrategy(strategy.MEPApiStrategy):
    _authentication = None
    _URL = 'https://api.invertironline.com/'
    _PLAZO = "t0"

    def __init__(self, credentials={}):
        self._credentials = credentials

    def _do_auth(self):
        params = {"username": self._credentials["username"],
                  "password": self._credentials["password"], "grant_type": "password"}
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.post(
            self._URL + 'token', data=params, headers=headers)
        if (response.status_code != 200):
            raise StandardError("Login incorrecto")
        response = response.json()
        return auth.Authentication(response["access_token"], response["refresh_token"], response[".expires"])

    def authenticate(self):
        if (self._authentication is None or self._authentication.is_expired()):
            self._authentication = self._do_auth()
        return self._authentication

    def _currency(self, moneda):
        return "USD" if moneda == "dolar_Estadounidense" else "ARS"

    def get_bonds(self, bonds_list):
        auth = self.authenticate()
        bonds = []
        for bond_name in bonds_list:
            query_params = "?plazo=" + self._PLAZO
            endpoint = "api/v2/bcba/titulos/" + bond_name + "/Cotizacion" + query_params
            headers = {"Authorization": "Bearer "+auth.token()}
            response = requests.get(self._URL + endpoint, headers=headers)
            if (response.status_code != 200):
                raise StandardError("No se ha podido recuperar el bono")
            response = response.json()
            bonds.append(bond.Bond(bond_name, response["ultimoPrecio"], self._currency(
                response["moneda"]), response["montoOperado"], response["cantidadOperaciones"], response["puntas"], response["fechaHora"]))
        return bonds
