from django.apps import AppConfig
import pathlib
from tensorflow import keras
import tensorflow.keras.backend as K
import tensorflow as tf

model_file = 'models/ployps/poly.h5'
dest_path = pathlib.Path(model_file).resolve()

def tversky(y_true, y_pred):
    y_true_pos = K.flatten(y_true)
    y_pred_pos = K.flatten(y_pred)
    true_pos = K.sum(y_true_pos * y_pred_pos)
    false_neg = K.sum(y_true_pos * (1-y_pred_pos))
    false_pos = K.sum((1-y_true_pos)*y_pred_pos)
    alpha = 0.7
    return (true_pos + 1)/(true_pos + alpha*false_neg + (1-alpha)*false_pos + smooth)

def focal_tversky(y_true,y_pred):
    y_true = tf.cast(y_true, tf.float32)
    y_pred = tf.cast(y_pred, tf.float32)
    
    pt_1 = tversky(y_true, y_pred)
    gamma = 0.75
    return K.pow((1-pt_1), gamma)

class PolypsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polyps'
    polyps_model = keras.models.load_model(dest_path,custom_objects={'focal_tversky':                   
focal_tversky},compile=False)
