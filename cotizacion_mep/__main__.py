from flask import Flask
from flask import request
from flask import jsonify
from flask import json
import mep_api as api
import sys
import cotizacion_mep.api_scheduler as scheduler
import cotizacion_mep.mep_api as mep_api
import cotizacion_mep.iol_mep_strategy as iol_mep_strategy
import ast
"""This module serves as the entry point of cotizacion_mep."""

app = Flask(__name__)
api = None


@app.route("/api/v1/mepvalue")
def get_cotizacion_mep():
    ''' Obtiene la mejor cotizacion del dolar MEP '''
    frm = int(request.args.get('from')) if request.args.get('from') else 0
    to = int(request.args.get('to')) if request.args.get('to') else 100
    response = app.response_class(
        response=json.dumps([element.to_json() for element in api.calculate(get_bonds_from_cmd())[frm:to]]),
        status=200,
        mimetype='application/json'
    )
    # response = jsonify([element.to_json() for element in api.calculate(get_bonds_from_cmd())[frm:to]])
    return response


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
