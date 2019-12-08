import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Ready to gird your loins with some runderwear?')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
