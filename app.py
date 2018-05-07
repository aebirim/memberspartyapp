import os
path = os.getcwd()
path += '/lib'
import sys
sys.path.append(path)
from setup import SetupGraph
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/commons')
def commons():
    graph = SetupGraph()
    return render_template('index.html', data = graph.newGraph())

@app.route('/lords')
def lords():
    graph = SetupGraph("House=Lords")
    return render_template('index.html', data = graph.newGraph())

if __name__ == "__main__":
      app.run()

