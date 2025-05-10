from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder='./templates')

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer no' 
} # ask me for api key

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # call runpod api
        content = request.form['content']
        data = {
            "input": {
                "messages": [
                    {"role": "system", "content": "You are a specialist in the field of rare diseases. You will be provided and asked about a complicated clinical case; read it carefully and then provide a diverse and comprehensive differential diagnosis"},
                    {"role": "user", "content": content}
                ],
            "sampling_params": {"temperature": 0.15, "repetition_penalty":1.18,  "max_tokens": 2000}
            }
        }

        response = requests.post('https://api.runpod.ai/v2/ojtigeh8zjfllq/runsync', headers=headers, json=data)
        return jsonify(response.json())
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True, port = 5001)
