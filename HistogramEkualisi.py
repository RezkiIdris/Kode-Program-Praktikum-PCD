import cv2
import numpy as np

citra = cv2.imread('gunung.jpg',0)

ekual = cv2.equalizeHist(citra)
hasil = np.hstack((citra, ekual))

cv2.imshow('Contoh Hasil Equalisasi',hasil)
cv2.waitKey(0)
