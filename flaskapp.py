from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import urllib
import re

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

@app.route('/stock/<code>')
def price_lookup(code):
    address = 'http://quotes.wsj.com/PH/' + str(code)
    html = urllib.urlopen(address).read() # READ IT ALL
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('span')

    for tag in tags:
        if tag.get('id', None) == 'quote_val':
            cont = str(tag.contents)
            result = re.findall('[0-9.]+', cont)

    data = {}
    if result is not None:
        data[str(code)] = str(result[0])
        print jsonify(**data)
        return jsonify(**data)

    data[str(code)] = "Not Found"
    return jsonify(**data)
