import numpy as np
import os
import io
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
from flask import Flask, request, jsonify

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

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
          
model = keras.models.load_model('xception_relic_classifier.h5')

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files['imagefile']
        file_path = "./images/" + file.filename
        file.save(file_path)

        try:
            img = image.load_img(file_path, target_size=(150, 150))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img = preprocess_input(img)
            img = np.vstack([img])

            prob = model.predict(img)
            classes = int(prob.argmax(axis=-1))
            result = LABELS[classes]

            data = {"prediction": str(result)}
            os.remove(file_path)

            return jsonify(data)
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)})

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
