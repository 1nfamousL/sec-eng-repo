from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f"./uploads/{file.filename}")
    return jsonify({"message": "File uploaded successfully"}), 200

@app.route('/fetch-url', methods=['GET'])
def fetch_url():
    url = request.args.get('url')
    response = requests.get(url)
    return response.text, response.status_code

app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/external-api', methods=['POST'])
def external_api():
    external_url = request.json.get('url')
    response = requests.get(external_url) 
    return response.json()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)