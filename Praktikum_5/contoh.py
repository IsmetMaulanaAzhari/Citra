# Latihan 1: Membaca dan Menampilkan Citra dengan OpenCV
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca citra
img_bgr = cv2.imread('bunga.jpg')
if img_bgr is None:
    print("File tidak ditemukan!")
    exit()

# Informasi
h, w, c = img_bgr.shape
print(f"Dimensi: {w} x {h}")
print(f"Jumlah saluran: {c}")

# Tampilkan dengan OpenCV (jendela terpisah)
cv2.imshow('BGR (OpenCV)', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Latihan 2: Menampilkan Citra dengan Matplotlib
# Konversi BGR ke RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Tampilkan dengan Matplotlib
plt.imshow(img_rgb)
plt.title('Citra RGB (Matplotlib)')
plt.axis('off')
plt.show()

# Latihan 3: Konversi ke Grayscale
# Konversi ke grayscale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Tampilkan dengan Matplotlib (perlu cmap='gray')
plt.imshow(img_gray, cmap='gray')
plt.title('Grayscale (OpenCV)')
plt.axis('off')
plt.show()

print(f"Dimensi grayscale: {img_gray.shape}")  # (h, w) tanpa channel

# Latihan 4: Konversi Grayscale Manual
# Pastikan citra dalam format RGB (bukan BGR)
# Konversi ke float agar perhitungan akurat
img_rgb_float = img_rgb.astype(np.float32)

# Hitung grayscale manual dengan bobot
R = img_rgb_float[:, :, 0]
G = img_rgb_float[:, :, 1]
B = img_rgb_float[:, :, 2]

gray_manual = 0.299 * R + 0.587 * G + 0.114 * B
gray_manual = gray_manual.astype(np.uint8)

# Bandingkan dengan hasil OpenCV
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Grayscale (OpenCV)')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_manual, cmap='gray')
plt.title('Grayscale (Manual)')
plt.axis('off')
plt.tight_layout()
plt.show()

# Periksa apakah hasil sama
diff = np.abs(img_gray.astype(np.int16) - gray_manual.astype(np.int16))
print(f"Perbedaan maksimum antara kedua metode: {np.max(diff)}")

# Latihan 5: Menyimpan Citra
cv2.imwrite('bunga_grayscale.jpg', img_gray)
print("Citra grayscale disimpan sebagai 'bunga_grayscale.jpg'")