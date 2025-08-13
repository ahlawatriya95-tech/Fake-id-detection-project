import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model('forgery_model.h5')

def predict_forgery(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array)
return "Fake Document" if prediction[0][0] > 0.5 else "Genuine Document"

