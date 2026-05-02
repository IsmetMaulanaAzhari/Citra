import cv2
import matplotlib.pyplot as plt
import numpy as np

def custom_blur(img, kernel):
    # Dapatkan dimensi gambar dan kernel
    h, w = img.shape
    kh, kw = kernel.shape

    # Hitung padding
    pad_h, pad_w = kh // 2, kw // 2

    # Tambahkan padding pada gambar menggunakan mode 'edge'
    padded_img = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    output = np.zeros_like(img, dtype=np.float32)

    # Loop konvolusi
    for i in range(h):
        for j in range(w):
            # Ambil region/jendela dari gambar ber-padding
            region = padded_img[i:i+kh, j:j+kw]
            # Kalikan dengan kernel dan jumlahkan
            output[i, j] = np.sum(region * kernel)

    return np.clip(output, 0, 255).astype(np.uint8)

# Uji coba
img_bgr = cv2.imread('bunga.jpg')
if img_bgr is not None:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Kernel Averaging 3x3
    kernel_avg = np.ones((3, 3), np.float32) / 9.0

    # Terapkan custom blur
    result_custom = custom_blur(img_gray, kernel_avg)

    plt.subplot(1, 2, 1), plt.imshow(img_gray, cmap='gray'), plt.title('Asli')
    plt.subplot(1, 2, 2), plt.imshow(result_custom, cmap='gray'), plt.title('Custom Averaging Blur')
    plt.show()