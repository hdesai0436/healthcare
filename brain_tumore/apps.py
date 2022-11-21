from django.apps import AppConfig
import pathlib
import os
import tensorflow as tf
from tensorflow import keras
model_file = 'models/tumore/brain_tumore.h5'
dest_path = pathlib.Path(model_file).resolve()

class BrainTumoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brain_tumore'
    model = keras.models.load_model(dest_path)
