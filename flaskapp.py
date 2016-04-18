from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

@app.route('/stock/<code>')
def price_lookup(code):
    html = urllib.urlopen(address).read() # READ IT ALL
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('span')
    result = None
    for tag in tags:
        if tag.get('id', None) == 'quote_val':
            cont = str(tag.contents)
            result = re.findall('[0-9.]+', cont)

    if result is not None:
        data = {}
        data[str(code)] = str(result[0])
        return flask.jsonify(**data)

    data = {}
    data[str(code)] = "Not Found"
    return flask.jsonify(**data)
