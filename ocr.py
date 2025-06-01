import os
import cv2
import pytesseract
from flask import Blueprint, request, render_tamplate, current_app

ocr_bp = Blueprint ('ocr', __name__, url_prefix='/ocr')

@ocr_bp.route('/', methods=['GET', 'POST'])
def ocr_image():
  if request.method == 'POST':
    file = request.files['image']
    if flie,filename== '':
        return render_template("ocr.html", error="File kosong")

        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        img = cv2.imread(filepath)
        text = pytesseract.image_to_string(img)

        return render_template("result_text.html", text=text)
    
    return render_tamplate("ocr.html")
    
