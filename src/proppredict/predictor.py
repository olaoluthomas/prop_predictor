"""
A Custom Predictor Routine to facilitate model serving in Vertex AI.
"""

import numpy as np
import joblib
import pickle

from google.cloud import storage


class CprPredictor(object):
    def __init__(self):
        return

    def load(self, gcs_artifacts_uri: str):
        gcs_client = storage.Client()
        with open('model.joblib', 'wb') as gcs_model, open('scaler.pkl', 'wb') as gcs_scaler:
            gcs_client.download_blob_to_file(
                f"{gcs_artifacts_uri}/model.joblib", gcs_model)
            gcs_client.download_blob_to_file(f"{gcs_artifacts_uri}/scaler.pkl",
                                             gcs_scaler)
        with open('scaler.pkl', 'rb') as scal:
            scaler = pickle.load(scal)

        self._model = joblib.load("model.joblib")
        self._scaler = scaler

    def predict(self, instances: np.ndarray):
        scaled_inputs = self._scaler.transform(instances)
        probabilities = self._model.predict_proba(scaled_inputs)

        return probabilities.tolist()