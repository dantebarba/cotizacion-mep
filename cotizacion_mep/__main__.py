from flask import Flask
import mep_api as api
import sys
import json
import mep_calculator as mep_calc
import cotizacion_mep.api_scheduler as scheduler
import cotizacion_mep.mongodb_mep_strategy as mongodb_mep_strategy
import ast
"""This module serves as the entry point of cotizacion_mep."""

app = Flask(__name__)


@app.route("/api/v1/mepvalue")
def get_cotizacion_mep():
    ''' Obtiene la mejor cotizacion del dolar MEP '''
    response = app.response_class(
        response=mep_calc.MEPCalculator(mongodb_mep_strategy.MongodbMepStrategy(
            "mongodb://mongodb:27017/")).calculate(ast.literal_eval(sys.argv[3])).to_json(),
        status=200,
        mimetype='application/json'
    )
    return response

def get_bonds_from_cmd():
    return ast.literal_eval(sys.argv[3])

def main():
    """The actual entry point."""
    # start scheduling for mep value recovery.
    print "Starting scheduler ..."
    sched = scheduler.Scheduler(
        {"username": sys.argv[1], "password": sys.argv[2]}, interval=60, bonds=get_bonds_from_cmd())
    sched.start()
    print "Scheduler started ..."
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
