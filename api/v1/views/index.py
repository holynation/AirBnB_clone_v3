#!/usr/bin/python3
'''
    flask with general routes
    routes:
        /status:    display "status":"OK"
'''
from api.v1.views import app_views


@app_views.route("/status")
def status():
    '''
        return JSON of OK status
    '''
    return jsonify({'status': 'OK'})
