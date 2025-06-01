from flask import Blueprint, request, redirect, url_for, send_file, render_template
import os
import pdfplumber
import pandas as pd
from werkzeug.utils import secure_filename

pdf_to_exel_bp = Blueprint('pdf_to_exel'__name__)

@pdf_to_exel_bp.route('/pdf-to-exel', methods=['GET','POST'])
def pdf_to_exel():
  if request.method == 'GET':
    # Alihkan ke halaman utama (karena form ada di index.html)
    return render_template(pdf_to_exel.html') # tampilkan form upload

  # Proses POST (upload dan konversi PDF)
  if 'pdf_file' not in request.files:
    return "No selected file"

  if file:
    filename = secure_filename(file.filename)
    filepath = os.path.join('static/upload', filename)
    file.save(filepath)

    tables = []
    with pdfplumber.open(filepath) as pdf:
      for page in pdf.pages:
        table = page.extract_table()
        if table:
          df = pd.DataFrame(table[1:], columns=table[0])
          tables.append(df)
    if not tables:
      return "No tables found in PDF"

    combined_df = pd.concat(tables, ignore_index=True)
    exel_path = filepath.replace('.pdf', '.xlsx')
    combined_df.to_exel(exel_path, index=False

    return send-file(exel_path ,as_attachment=True)
