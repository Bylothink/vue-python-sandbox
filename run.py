#!/usr/bin/env python
#

import json
import traceback

from flask import Flask, Response, request

try:
    from app import web_python_sandbox

except Exception as exc:
    EXCEPTION = exc

    def web_python_sandbox(*args, **kwargs):
        raise EXCEPTION

STATIC_DIR = 'dist'


def format_traceback(exc):
    return "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))


app = Flask(__name__, static_folder=STATIC_DIR)

@app.route('/application.json', methods=['OPTIONS'])
def run_app_preflight():
    return Response(
        headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*'
        },
        mimetype='application/json')

@app.route('/application.json', methods=['POST'])
def run_app():
    try:
        result = {
            'type': 'success',
            'data': web_python_sandbox(*request.get_json())
        }

    except Exception as exc:
        result = {
            'type': 'error',
            'message': format_traceback(exc)
        }

    return Response(
        json.dumps(result),
        headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*'
        },
        mimetype='application/json')

@app.route('/')
@app.route('/<path:filepath>')
def serve_static_files(filepath='index.html'):
    return app.send_static_file(filepath)

app.run(host='0.0.0.0', port=8080, debug=True)
