from flask import Flask
from flask import jsonify
from flask import request
from bs4 import BeautifulSoup
import urllib
import re

app = Flask(__name__, static_url_path='')

@app.route('/')
def load_index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()

@app.route('/stock/<code>')
def price_lookup(code):
    address = 'http://quotes.wsj.com/PH/' + str(code)
    html = urllib.urlopen(address).read() # READ IT ALL
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('span')
    result = None
    for tag in tags:
        if tag.get('id', None) == 'quote_val':
            cont = str(tag.contents)
            result = re.findall('[0-9.]+', cont)

    data = {}
    print result
    if result is not None:
        data[str(code)] = str(result[0])
        return jsonify(**data)
    else:
        data[str(code)] = "Not Found"
        return jsonify(**data)
