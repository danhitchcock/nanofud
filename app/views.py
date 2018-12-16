from app import app
from flask import render_template, request, send_file
import os


@app.route('/')
def index():
    fud = request.args.get('fud')
    if fud is None:
        return render_template('index.html', searchItem='')
    return render_template('index.html', searchItem=fud)


@app.route('/<topic>')
def topic(topic):
    if topic == 'nanote.txt':
        return send_file(
            os.path.join(app.root_path, 'static/nanote.txt'))
    if topic == 'favicon.ico':
        return ''
    return render_template('%s.html'%topic)

"""
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


@app.route('/decentralization')
def decentralization():
    return render_template('decentralization.html')


@app.route('/spam_attacks')
def spam_attacks():
    return render_template('spam_attacks.html')

@app.route('/bitgrail')
def bitgrail():
    return render_template('bitgrail.html')
"""

