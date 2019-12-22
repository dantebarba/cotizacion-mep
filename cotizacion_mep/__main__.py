from flask import Flask
import mep_api as api
import sys
import json
import mep_calculator as mep_calc
import ast
"""This module serves as the entry point of cotizacion_mep."""

app = Flask(__name__)
mep_calculator = None


@app.route("/api/v1/mepvalue")
def get_cotizacion_mep():
    ''' Obtiene la mejor cotizacion del dolar MEP '''
    response = app.response_class(
        response=mep_calculator.calculate(ast.literal_eval(sys.argv[3])).to_json(),
        status=200,
        mimetype='application/json'
    )
    return response

def main():
    """The actual entry point."""
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    mep_calculator = mep_calc.MEP_Calculator(sys.argv[1], sys.argv[2])
    main()
