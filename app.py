from flask import Flask, render_template, request, send_file
import base64
import io
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Nhận dữ liệu từ yêu cầu POST
        data = request.form['imageData']

        # Loại bỏ phần đầu 'data:image/png;base64,' của chuỗi base64
        data = data.split(',')[1]
        img_data = base64.b64decode(data)

        # Mở ảnh từ dữ liệu nhị phân
        image = Image.open(io.BytesIO(img_data))

        # Lưu ảnh vào bộ nhớ tạm
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        # Trả ảnh dưới dạng tệp để tải xuống
        return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='drawing.png')
    except Exception as e:
        return f"Error: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
