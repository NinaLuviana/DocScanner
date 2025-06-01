from flask import blueprint, send_file, current_app, render_template
import os
import cv2
from PIL import Image

capture_camera_bp = Blueprint('capture_camera', __name__,url_prefix='/capture')

@capture_camera_bp.route('/')
def capture_pdf():
  cam = cv2.VideoCapture(0)

  if not cam.isOpened():
      return "Tidak Bisa membuka kamera"

  window_name = "Tekan [SPACE] untuk Capture, [ESC] untuk batal"
  cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
  cv2.resizeWindow(Window_name,960,720)

while true:
  ret,frame = cam.read()
  if not ret:
    break

cv2.imshow(window_name, frame)
key = cv2 waitKey(1)

if key ==27:
  cam.realease()
  cv2.destroyAllWindows()
  return "Capture dibatalkan"
elif key == 32
  break

cam.realease()
cv2.destroyAllWinodws()

save_path = os.path.join(current_app_config['UPLOAD_FOLDER'], 'capture.jpg')
cv2.imwrite(save_path, frame)

h,w, _  = frame.shape
cropped = frame[h // 7:9 * h // 7, w // 7:9 * w // 9]
cropped_path = os.path.join(current_app.config['UPLOAD_FOLDER'], "cropped.jpg")
cv2.imwrite(cropped_path, cropped)

image = Image.open(cropped_path).convert(*RGB*)
pdf_path = cropped_path.replace('jpg','.pdf')

  return send_file(pdf_path, as_attachment=True)

@capture_camera_bp.route('/ui')
def capture_ui():
    return render_template('capture.html)
