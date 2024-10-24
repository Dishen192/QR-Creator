from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image
    img_path = os.path.join('static', 'qr_code.png')  # Save to the static folder
    img.save(img_path)

    return render_template('result.html', img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
