# A very simple Flask Hello World app for you to get started with...

#from flask import Flask
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'K-Means Clustering Society Status!'

@app.route('/api/predict',methods=['POST'])
def predict():
    #open file
    file = open("modelkmeans.sav","rb")
    #load trained model
    trained_model = joblib.load(file)
    
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    pred = []

    # Make prediction using model loaded from disk as per the data.
    for data in datas:
        prediction = trained_model.predict([np.array([data["jumlah_anak"],data["penghasilan"]])])

        # Take the first value of prediction
        output = prediction[0]
        out = 'Tidak Layak' if output==1 else 'Layak'
        pred.append(out)
    return jsonify(pred)
