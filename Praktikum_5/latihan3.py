import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('pemandangan.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_gray_std = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Mengambil HANYA saluran Green (indeks 1 pada array RGB)
gray_green = img_rgb[:,:,1]

# Tampilkan perbandingan
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_gray_std, cmap='gray')
plt.title('Standar Grayscale')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_green, cmap='gray')
plt.title('Saluran Hijau Saja (Green Only)')
plt.axis('off')

plt.tight_layout()
plt.show()