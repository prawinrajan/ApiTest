import json
from flask import Flask, Response, abort,request
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)

@app.route('/hai', methods=['POST'])
def create_data():
    try:
        d = request.json
        #print(d)
        mdata = request.data
        #mydata = mdata.decode('utf8')
        s = json.loads(mdata)
        da = json.dumps(s)
        remove_lef = da.replace('[', '')
        remove_right = remove_lef.replace(']', '')
        data = ast.literal_eval(remove_right)
        # print(data)
        msg = data['msg']
        sensor_data=[{
            "msg":"you sent"+msg
        }]
        response = Response(json.dumps(sensor_data), status=200, mimetype=JSON_MIME_TYPE)
        return response


    except Exception as e:
        print(e)
        print('process failed')
        return json_response(status=500)
