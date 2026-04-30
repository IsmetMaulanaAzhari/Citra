import cv2
import matplotlib.pyplot as plt

# Membaca citra objek_warna.jpg
# (Ganti 'objek_warna.jpg' dengan nama file Anda jika berbeda)
img_bgr = cv2.imread('objek_warna.jpg')

# Pastikan gambar berhasil dimuat
if img_bgr is None:
    print("File gambar tidak ditemukan!")
else:
    # Konversi BGR ke RGB untuk keperluan visualisasi Matplotlib
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # --- Tugas 1: Konversi metode standar (OpenCV) ---
    gray_std = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # --- Tugas 2: Konversi dengan hanya mengambil saluran hijau ---
    # Pada array img_rgb (Red, Green, Blue), indeks untuk Green adalah 1
    gray_green = img_rgb[:, :, 1]

    # --- Tugas 3: Tampilkan kedua hasil secara berdampingan ---
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(gray_std, cmap='gray')
    plt.title('Grayscale Standar (OpenCV)')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(gray_green, cmap='gray')
    plt.title('Grayscale (Saluran Hijau Saja)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()