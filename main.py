"""
A task utility and argument parser to initiate Propensity model training and hyperparameter tuning.
"""
from flask import Flask, request, jsonify
from proppredict import predictor
import numpy as np
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"


@app.route("/predict", methods=['POST'])
def predict():
    try:
        instances = request.json.get("instances")
        instances = np.asarray(instances)
        model = predictor.CprPredictor()
        model.load(os.environ["AIP_STORAGE_URI"])
        
        predictions = model.predict(instances)
        
        response = {"predictions": predictions}
        
    except Exception as e:
        response = {'error': str(e)}

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=os.environ.get("PORT", 8080),
            debug=True,
            use_reloader=True)