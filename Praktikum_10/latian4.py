import cv2
import numpy as np

# Baca gambar koin banyak
img = cv2.imread('gambar1.jpg', cv2.IMREAD_GRAYSCALE)

# Segmentasi dengan Otsu
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Cari kontur objek
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Jumlah objek yang terdeteksi: {len(contours)}")
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    print(f"Objek ke-{i+1} -> Luas: {area} piksel")