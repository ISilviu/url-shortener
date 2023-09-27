from flask_restful import Resource
from flask import request
import pyshorteners

urls = {}
url_shortener = pyshorteners.Shortener()


class URLShortener(Resource):
    def post(self):
        url = request.form['url']
        shortened_url = url_shortener.tinyurl.short(url)
        urls[url] = shortened_url
        return {
            'short_url': shortened_url,
            'original_url': url
        }
