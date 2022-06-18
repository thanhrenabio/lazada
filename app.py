from flask import Flask, request, abort
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        file_path = 'output/'+str(datetime.now())+'.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(request.json, f, ensure_ascii=False, indent=4)
        return 'success', 200
    else:
        abort(400)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
