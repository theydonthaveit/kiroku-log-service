"""
Quart web server that accepts requests to store logs from any source
"""
import json

from quart import Quart, request
from quart_cors import cors
from write_to_sys import log_to_file, retrieve_current_log


app = Quart(__name__)
app = cors(app)


@app.route('/log', methods=['POST'])
async def log():
    """
    An async call serving POST requests
    All logged data sent here logging to sys file
    rtype -> None

    example of request data:
    {
        file_name: example.py,
        pid: 1,
        func: example,
        process: INFO,
        log: example_text
    }
    """
    await log_to_file(
        json.loads(
            await request.get_data()))


@app.route('/active-log', methods=['GET'])
async def log_active():
    """
    An async call serving GET requests
    All logged data accessible via browser
    rtype -> Text
    """
    date = request.args.get('date')
    data = await retrieve_current_log(date)
    return data


if __name__ == '__main__':
    app.run(debug=True,
            port=80,
            host='0.0.0.0')