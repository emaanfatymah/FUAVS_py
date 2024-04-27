from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

# from flask import Flask, Response, render_template
# from djitellopy import tello
# import cv2
# import numpy as np
# import io
#
# app = Flask(__name__)
#
# me = tello.Tello()
# me.connect()
# print(me.get_battery())
#
# me.streamon()
#
#
# def generate_frames():
#     while True:
#         img = me.get_frame_read().frame
#         img = cv2.resize(img, (360, 240))
#         ret, buffer = cv2.imencode('.jpg', img)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/video_feed')
# def video_feed_route():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)
#     # app.run(ssl_context=('cert.pem', 'key.pem'))
