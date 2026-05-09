import cv2
import matplotlib.pyplot as plt
import numpy as np

img_bgr = cv2.imread('gedung.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

edges_canny = cv2.Canny(img_gray, 100, 200)

# Membuat kernel untuk morfologi
kernel = np.ones((3,3), np.uint8)
# Dilasi untuk menebalkan dan menyambung tepi yang putus
edges_dilated = cv2.dilate(edges_canny, kernel, iterations=1)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(edges_canny, cmap='gray')
plt.title('Canny Sebelum Morfologi')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_dilated, cmap='gray')
plt.title('Canny Sesudah Dilasi (Tersambung)')
plt.axis('off')

plt.show()