import os
import logging
import webapp2

from google.appengine.ext.webapp import template


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


class MainPage(webapp2.RequestHandler):

    def get(self):
        path = TEMPLATE_DIR + '/index.html'
        logging.info(path)
        self.response.write(template.render(path, {}))

class FeaturesPage(webapp2.RequestHandler):

    def get(self):
        path = TEMPLATE_DIR + '/features.html'
        logging.info(path)
        self.response.write(template.render(path, {}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/features', FeaturesPage),
], debug=True)
