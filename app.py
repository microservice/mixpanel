# -*- coding: utf-8 -*-
import json
import os
import sys

from mixpanel import Mixpanel

from flask import Flask, make_response, request


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.mp = Mixpanel(os.getenv('PROJECT_TOKEN'))

    def track(self):
        req = request.get_json()
        event_name = req.get('event')
        properties = req.get('properties')
        distinct_id = req['distinct_id']

        self.mp.track(distinct_id, event_name, properties)

        return self.end({'success': True})

    def people_set(self):
        req = request.get_json()
        properties = req.get('properties')
        distinct_id = req['distinct_id']

        self.mp.people_set(distinct_id, properties)

        return self.end({'success': True})

    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    if os.getenv('PROJECT_TOKEN') is None:
        print('Environment variable PROJECT_TOKEN not found.')
        sys.exit(1)

    handler = Handler()
    handler.app.add_url_rule('/track', 'track', handler.track,
                             methods=['post'])
    handler.app.add_url_rule('/people_set', 'people_set', handler.people_set,
                             methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
