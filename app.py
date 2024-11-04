import numpy as np
from bidict import bidict
from flask import (
    Flask, render_template, request,
    redirect, url_for, session,jsonify
)
from random import choice
from tensorflow import keras
import base64
from io import BytesIO
from PIL import Image, ImageOps
from convert_img2latex import img_to_latex
import cv2
from computer import evaluate_latex_expression
text = ''
ENCODER = bidict({
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
})


app = Flask(__name__)
app.secret_key = 'alphabet_quiz'


@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

# @app.route('/add-data', methods=['GET'])
# def add_data_get():
#     message = session.get('message', '')
#
#     # labels = np.load('data/labels.npy')
#     # count = {k: 0 for k in ENCODER.keys()}
#     # for label in labels:
#     #     count[label] += 1
#     # count = sorted(count.items(), key=lambda x: x[1])
#     # letter = count[0][0]
#
#     letter = choice(list(ENCODER.keys()))
#
#     return render_template("addData.html", letter=letter, message=message)

# @app.route('/add-data', methods=['POST'])
# def add_data_post():
#
#     label = request.form['letter']
#     labels = np.load('data/labels.npy')
#     labels = np.append(labels, label)
#     np.save('data/labels.npy', labels)
#
#     pixels = request.form['pixels']
#     pixels = pixels.split(',')
#     img = np.array(pixels).astype(float).reshape(1, 50, 50)
#     imgs = np.load('data/images.npy')
#     imgs = np.vstack([imgs, img])
#     np.save('data/images.npy', imgs)
#
#     session['message'] = f'"{label}" added to the training dataset'
#
#     return redirect(url_for('add_data_get'))

@app.route('/Get Started', methods=['GET'])
def practice_get():
    letter = choice(list(ENCODER.keys()))
    return render_template("Get Started.html", letter=letter, correct='')

@app.route('/Get Started', methods=['POST'])
def practice_post():
    try:
        pixels = request.form['pixels']
        pixels = pixels.split(',')
        img = np.array(pixels).astype(float)
        pred_letter = img_to_latex(img)
        return render_template("Get Started.html", letter=pred_letter, correct=True)

    except Exception as e:
        print(e)
        return render_template('error.html')
@app.route('/get_text')
def get_text():
    global text
    return jsonify(formula= text)
@app.route('/get_result')
def get_result():
    global text
    t = str(evaluate_latex_expression(text))
    return jsonify(result = t)
@app.route('/save_canvas', methods=['POST'])
def save_canvas():
    data_url = request.json['image']
    # Tách bỏ phần tiền tố 'data:image/png;base64,'
    image_data = data_url.split(",")[1]
    # Giải mã base64 thành dữ liệu ảnh
    image_bytes = BytesIO(base64.b64decode(image_data))
    # Đọc ảnh thành định dạng PIL, rồi chuyển sang np.array
    image = Image.open(image_bytes)
    image_np = np.array(image)
    gray_image = 255 - image_np[:,:,3]
    global text
    text = img_to_latex(gray_image)
    cv2.destroyAllWindows()
    return jsonify(gray_image.tolist())  # Chuyển đổi sang list để có thể trả về JSON
if __name__ == '__main__':
    app.run(debug=True)
