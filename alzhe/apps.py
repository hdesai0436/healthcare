from django.apps import AppConfig
import pathlib
from tensorflow import keras

model_file='models/alz/classification.h5'
dest_path=pathlib.Path(model_file).resolve()

class AlzheConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alzhe'
    alz_model= keras.models.load_model(dest_path)
