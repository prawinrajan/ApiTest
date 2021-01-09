import os

from api.POST import app
#from api.Response import app


if __name__ == '__main__':
    app.debug = True
    #app.config['DATABASE_NAME'] = 'Home.sqlite'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port,threaded=True)
