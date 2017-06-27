import sys
from flask import Flask, render_template
import os
import datetime
import logging
path = os.getcwd()
path += '/lib'
sys.path.append(path)
from setup import SetupGraph
app = Flask(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S', filename='applog.log', level=logging.DEBUG, filemode='w' )

def main():
    logging.info('Application started')
    try:
        app.run()
    except RuntimeError as err:
        logging.error('Application not starting: %s' % (err))

@app.route('/')
@app.route('/<house>')
def index(house=None):
    graph = SetupGraph("House=%s" % (house.title())).newGraph()
    logging.info('%s route launched' % (house))
    return render_template('index.html', data=graph)

# @app.route('/lords')
# def lords():
#     graph = SetupGraph("House=Lords").newGraph()
#     logging.info('Lords route launched')
#     return render_template('lords.html', data=graph)

if __name__ == "__main__":
    main()
    #app.run()

