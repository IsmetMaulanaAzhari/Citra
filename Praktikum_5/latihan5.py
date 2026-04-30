import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('pemandangan.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar dan histogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Citra Grayscale')
plt.axis('off')

plt.subplot(1, 2, 2)
# Gunakan parameter bins=256 untuk rentang 0-255
plt.hist(img_gray.ravel(), bins=256, range=[0, 256], color='gray')
plt.title('Histogram')
plt.xlabel('Intensitas (0 = Hitam, 255 = Putih)')
plt.ylabel('Frekuensi / Jumlah Piksel')

plt.tight_layout()
plt.show()