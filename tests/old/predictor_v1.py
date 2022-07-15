"""
A predictor to facilitate model serving in Vertex AI.
"""

from pandas import DataFrame
import numpy as np
import os
import joblib
import pickle

from google.cloud import storage


class Predictor(object):
    def __init__(self, model, scaler):
        self._model = model
        self._scaler = scaler

    def predict(self, instances: np.ndarray):
        inputs = np.asarray(instances)
        scaled_inputs = self._scaler.transform(inputs)
        probabilities = self._model.predict_proba(scaled_inputs)[:, 1]

        return probabilities.tolist()

    @classmethod
    def from_path(cls, gcs_artifacts_uri: str):
        gcs_client = storage.Client()

        with open('model.joblib', 'wb') as gcs_model, open('scaler.pkl',
                                                           'wb') as gcs_scaler:
            gcs_client.download_blob_to_file(
                f"{gcs_artifacts_uri}/model.joblib", gcs_model)
            gcs_client.download_blob_to_file(f"{gcs_artifacts_uri}/scaler.pkl",
                                             gcs_scaler)
        with open('model.joblib', 'rb') as mod, open('scaler.pkl',
                                                     'rb') as scal:
            model = joblib.load(mod)
            scaler = pickle.load(scal)

        return cls(model, scaler)
