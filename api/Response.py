import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE, sensor_details

app = Flask(__name__)

msg=[{
    "HomeId":1,
     "msg":"hello client"
}]

@app.route('/sensor_data')
def sensor():
    response = Response(json.dumps(msg),status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.route('/sensor_data/<int:HomeId>')
def sensor_detail(HomeId):
    sd= sensor_details(msg,HomeId)
    if sd is None:
        abort(404)

    content = json.dumps(sd)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.errorhandler(404)
def not_found(e):
    return '', 404
