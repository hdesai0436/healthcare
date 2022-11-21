from django.apps import AppConfig
import tensorflow as tf
from tensorflow import keras
import os
import pathlib
model_file= 'models/chest/chest.h5'
dest_path=pathlib.Path(model_file).resolve()



class ChestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chest'
    chest_model= keras.models.load_model(dest_path)
