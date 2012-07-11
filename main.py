import webapp2
import time
import cgi
import json

from bma import Berlekamp_Massey_algorithm as BMA


def process_input(s):
    ret = []
    for c in s:
        if c.isdigit():
            if int(c) not in (0, 1):
                return None
            else:
                ret.append(int(c))
    return ret


class ComputationHandler(webapp2.RequestHandler):
    def post(self):
        input_str = self.request.body
        sequence = process_input(cgi.escape(input_str))
        if not sequence:
            self.response.headers['Content-Type'] = 'application/json'
            result = json.dumps({
                'poly': 'Invalid input... Please try again.',
                'span': '',
                'time': '',
            })
            self.response.write(result)
            return

        start_time = time.clock()
        polynomial, linear_span = BMA(sequence)
        elapsed_time = '%.2f sec' % (time.clock() - start_time)

        self.response.headers['Content-Type'] = 'application/json'
        result = json.dumps({
            'poly': str(polynomial),
            'span': str(linear_span),
            'time': str(elapsed_time),
        })
        self.response.write(result)


app = webapp2.WSGIApplication([
        ('/compute', ComputationHandler),
], debug=True)
