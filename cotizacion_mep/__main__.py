from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import abort
import mep_api as api
import sys
import os
import cotizacion_mep.api_scheduler as scheduler
import cotizacion_mep.mep_api as mep_api
import cotizacion_mep.iol_mep_strategy as iol_mep_strategy
import ast
"""This module serves as the entry point of cotizacion_mep."""

app = Flask(__name__)
api = None


@app.route("/api/v2/mepvalue")
def get_cotizacion_mep():
    ''' Obtiene la mejor cotizacion del dolar MEP '''
    auth(request.headers.get('X-Auth-Pass'))
    frm = int(request.args.get('from')) if request.args.get('from') else 0
    to = int(request.args.get('to')) if request.args.get('to') else 100
    volume_ars = int(request.args.get('volume_ars')) if request.args.get(
        'volume_ars') else 100000
    volume_usd = int(request.args.get('volume_usd')) if request.args.get(
        'volume_usd') else 10000
    operations_ars = int(request.args.get('ops_ars')
                         ) if request.args.get('ops_ars') else 10
    operations_usd = int(request.args.get('ops_usd')
                         ) if request.args.get('ops_usd') else 30
    json_list = [element.to_json() for element in api.calculate(
        get_bonds_from_cmd(), min_volume_ars=volume_ars, min_operations_ars=operations_ars, min_volume_usd=volume_usd, min_operations_usd=operations_usd)[frm:to]]
    # response = app.response_class(
    #     response=json.dumps(json_list),
    #     status=200,
    #     mimetype='application/json'
    # )
    response = jsonify(json_list)
    return response

def auth(password=''):
    if not password == os.environ['API_PASSWORD']:
        abort(401)

def get_bonds_from_cmd():
    return ast.literal_eval(sys.argv[3])


def main():
    """The actual entry point."""
    # start scheduling for mep value recovery.
    # api = mep_api.MEPApi(scheduler.SchedulerStrategy(
    # {"username": sys.argv[1], "password": sys.argv[2]}, bonds=get_bonds_from_cmd()))
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    api = mep_api.MEPApi(iol_mep_strategy.IolMEPStrategy(
        {"username": sys.argv[1], "password": sys.argv[2]}))
    main()
