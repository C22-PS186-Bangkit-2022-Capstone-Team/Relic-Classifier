import numpy as np
import os
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) ,'xception_relic_classifier.h5')
model = keras.models.load_model(model_path)

LABELS = ['Candi Brahu',
          'Candi Mendut',
          'Candi Prambanan',
          'Monumen Jogja Kembali',
          'Tugu Yogyakarta',
          'Candi Borobudur',
          'Monumen Solidaritas Asia Afrika',
          'Monumen Jalesveva Jayamahe',
          'Monumen Simpang Lima Gumul',
          'Monumen Jayandaru',
          'Monumen Serangan Umum 1 Maret',
          'Monumen Bambu Runcing',
          'Monumen Bajra Sandhi',
          'Monumen Panca Benua',
          'Monumen Bandung Lautan Api',
          'Monumen Pers Nasional',
          'Monumen Rawa Gede',
          'Tugu Khatulistiwa',
          'Monumen Nasional',
          'Gedung Gonggong',
          'Monumen Perjuangan Rakyat (Palembang)',
          'Monumen Pattimura',
          'Monumen Tirosa',
          'Monumen Merpati Perdamaian',
          'Tugu Keris Siginjai',
          'Tugu 0 KM Indonesia',
          'Monumen Mandala',
          'Monumen Nani Wartabone',
          'Monumen Palagan']

img_path = os.path.join(os.getcwd(), 'test/example_images/tugu_keris_siginjai.jpeg')
print(img_path)
img = image.load_img(img_path, target_size=(150,150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

images = np.vstack([x])
prob = model.predict(images)
classes = int(prob.argmax(axis=-1))

print(LABELS[classes])
