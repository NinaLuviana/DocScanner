from flask import Flask, render_template, request, redirect, url_for, session, flash
from moduls.upload_image import upload_image_bp
from moduls.capture_camera import capture_camera_bp
from moduls.ocr import ocr_bp
from moduls.pdf_to_excel import pdf_to_excel_bp
from moduls.ocr_to_excel import ocr_to_excel_bp

app = Flask(__name__)
app.secret_key = 'rahasia'

users={
    'admin' : 'admin123'
}

app.config ['UPLOAD_FOLDER] = 'static/uploads'

app.register_bluprint(upload_image_bp)
app.register_blueprint(capture_camera_bp)
app.register_blueprint(ocr_bp)
app.register_blueprint(pdf_to_excel_bp)
app.register_blueprint(ocr_to_excel_bp)

#halaman utama

#halaman login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login berhasil!','success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah.','danger')
    return render_template('login.html')

#logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Berhasil logout.','info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True
