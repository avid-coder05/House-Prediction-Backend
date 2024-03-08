from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_price
from login import add_cred, check_cred
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def process_post_request():
    data = request.json

    if data:
        if(len(data)==4):
            prediction = predict_price(data)
        elif(data['login']==1):
            if(check_cred(data)):
                return jsonify({'login':True}), 200
            else:
                return jsonify({'error': 'Credentials not found'}), 200
        elif(data['login']==0):
            add_cred(data)
            return jsonify({'login': True}), 200
        return jsonify({'prediction': prediction}), 200
    else:
        return jsonify({'error': 'Input data not found'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)