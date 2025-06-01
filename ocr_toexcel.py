from flask import Blueprint, request, render_template, send_file
import os
import pytesseract
from PIL import Image
from openpyx1 import workbook

ocr_ to_ excel_bp = Blueprint('ocr_to_excel', _name_)

@ocr_to_excel_bp.route('?ocr_to_excel',methods=['GET', 'POST'])
def ocr_to_excel():
  if request.metod == 'post':
    if 'image' not in request.files:
      return "Gambar tidak ditemukan", 400

image = request.files['image']
if image.filetame == '':
  return "Tidak ada file yang dipilih", 400

#simpan gambar
image_path = os.path.join('static/uploads', image.filename)
image,save(image_path)

#ocr dengan tesseract
text = pytesseract.image_to_string(Image.open(image_path))

#simpan ke excel
wb = workbook()
ws = wb.active
ws.titele = "Hasil OCR"
for i, line in enumerate(text.splitlines(), start=1):
  ws.cell(row=i, column=1, value=line)

output_excel = os.path.join('static/uploads', 'ocr_output.x1sx')
wb.save(output_excel)

return send_file(output_excel, as_attachment=True)

return render_template('ocr_to_excel.html')
