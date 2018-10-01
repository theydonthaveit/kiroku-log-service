"""
Quart web server that accepts requests to store logs from any source
"""
import json

from quart import Quart, request, send_from_directory
from quart_cors import cors


app = Quart(__name__)
app = cors(app)


@app.route('/', methods=['POST'])
async def hello():
    """
    An async call serving POST requests from the frontend
    Each request handled is sent to Neo4j for possible modifications
    rtype -> Response()
    """
    if request.method == 'POST':
        data = await request.get_data()
        res = json.loads(data)


if __name__ == '__main__':
    app.run(debug=True,
            port=80,
            host='0.0.0.0')
