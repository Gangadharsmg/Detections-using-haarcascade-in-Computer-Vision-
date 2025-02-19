# -*- coding: utf-8 -*-
"""Eyes detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXQWpr3LLX_BmD_ahDp4L9cpCzfO0xzK

# **Eyes Detection using OpenCV**

Import cv2 library
"""

import cv2

"""**haarcascade_eye.xml** is a haar cascade designed by OpenCV to detect the eyes."""

!pip install wget
import requests
import wget
url = 'https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml'
filename = wget.download(url)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + filename)

def detect(gray, frame):
  eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
  for (x, y , w, h) in eyes:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 , 0), 3)
    roi_gray = gray[y:y+h, x:x+w]
  return frame

# Uncomment below code to open webcam and run in terminal
"""
video_capture = cv2.VideoCapture(0)
print(video_capture.isOpened())
while True:
  _, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  canvas = detect(gray, frame)
  cv2.imshow("Video", canvas)

  if cv2.waitkey(1) & 0xFF == ord('q'):
   break

video_capture.release()
cv2.destroyAllWindows()
"""

from google.colab.patches import cv2_imshow
img_url = 'https://gangadhars.files.wordpress.com/2020/05/dsc_7737.jpg'
image = wget.download(img_url)
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canvas = detect(gray, image)
cv2_imshow(canvas)

