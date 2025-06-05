from flask import Blueprint, request, send_file, current_app, render_template
import os
from PIL import Image

upload_image_bp = Blueprint ( 'upload_image', __name__, url_prefix = '/upload')

@upload_image_bp.route('/', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        file = request.files ['image']
        if file.filename == '':
            return "Tidak ada file dipilih"

        filepath = os.path.join(current_app.config ['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        image = Image.open(filepath).convert("RGB")
        pdf_path = filepath.rsplit('.', 1)[0]+ ".pdf"
        image.save(pdf_path)

        return send_file(pdf_path,as_attachment=True)

  #render halaman upload jika GET
  return render_template('upload_image.html')
