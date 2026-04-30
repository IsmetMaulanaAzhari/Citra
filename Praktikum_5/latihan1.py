import cv2
import matplotlib.pyplot as plt

# 1. Baca citra pemandangan.jpg
img_bgr = cv2.imread('pemandangan.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # Konversi BGR ke RGB untuk Matplotlib

# 2. Konversi ke grayscale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 3. Simpan sebagai pemandangan_gray.jpg
cv2.imwrite('pemandangan_gray.jpg', img_gray)
print("Berhasil disimpan sebagai pemandangan_gray.jpg")

# 4. Tampilkan dalam satu figure (2 kolom)
plt.figure(figsize=(10, 5))

# Kolom 1
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Asli (RGB)')
plt.axis('off')

# Kolom 2
plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.tight_layout()
plt.show()