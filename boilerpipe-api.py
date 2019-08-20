#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import json
import argparse

import cherrypy
from boilerpipe.extract import Extractor


class BoilerPipeExtract(object):
    @cherrypy.expose
    def index(self):
        return 'Hi, API is working\n'

    @cherrypy.expose
    def extractText(self, url=None, html=None, extractor='ArticleExtractor'):
        cherrypy.response.headers['Content-Type'] = "text/json"

        if url:
            extractor = Extractor(extractor=extractor, url=url)
            extracted_text = extractor.getText()
            return json.dumps({'url': url,
                               'extractedText': extracted_text})
        elif html:
            extractor = Extractor(extractor=extractor, html=html)
            extracted_text = extractor.getText()
            return json.dumps({'html': html[:15],
                               'extractedText': extracted_text})

    @cherrypy.expose
    def extractHTML(self, url=None, html=None, extractor='ArticleExtractor'):
        cherrypy.response.headers['Content-Type'] = "text/json"

        if url:
            extractor = Extractor(extractor=extractor, url=url)
            extracted_html = extractor.getHTML()
            return json.dumps({'url': url,
                               'extractedHTML': extracted_html})
        elif html:
            extractor = Extractor(extractor=extractor, url=url)
            extracted_html = extractor.getHTML()
            return json.dumps({'html': html[:15],
                               'extractedHTML': extracted_html})


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080
    })
    cherrypy.quickstart(BoilerPipeExtract())
