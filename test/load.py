import numpy as np
import os
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) ,'xception_relic_classifier.h5')
model = keras.models.load_model(model_path)
labels = [
    'gedung_gonggong',
    'monpera',
    'monumen_merpati_perdamaian',
    'tugu_keris_siginjai',
    'tugu_nol_km_indonesia',
    'monumen pattimura',
    'Monumen Jogja Kembali',
    'Tugu Yogyakarta',
    'Monumen Simpang Lima Gumul',
    'Monumen Bambu Runcing',
    'Monumen Bajra Sandhi',
    'Monumen Panca Benua',
    'Monumen Bandung Lautan Api',
    'Monumen Pers Nasional',
    'monumen_tirosa',
    'Monumen Nasional'
]

img_path = os.path.join(os.getcwd(), 'test/example_images/tugu_keris_siginjai.jpeg')
print(img_path)
img = image.load_img(img_path, target_size=(150,150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

images = np.vstack([x])
prob = model.predict(images)
classes = int(prob.argmax(axis=-1))

print(labels[classes])
