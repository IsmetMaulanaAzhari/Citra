import cv2
import matplotlib.pyplot as plt
import numpy as np

# Definisi Fungsi
def konversi_grayscale(img, metode):
    # Catatan: Fungsi ini berasumsi 'img' yang masuk adalah format RGB
    if metode == 'opencv':
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    elif metode == 'manual':
        img_f = img.astype(np.float32)
        return (0.299 * img_f[:,:,0] + 0.587 * img_f[:,:,1] + 0.114 * img_f[:,:,2]).astype(np.uint8)
    elif metode == 'green_only':
        return img[:,:,1]
    else:
        return None

# Eksekusi
img_bgr = cv2.imread('pemandangan.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Panggil fungsi untuk ketiga metode
hasil_cv2 = konversi_grayscale(img_rgb, 'opencv')
hasil_man = konversi_grayscale(img_rgb, 'manual')
hasil_grn = konversi_grayscale(img_rgb, 'green_only')

# Tampilkan dalam grid 1x3
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1), plt.imshow(hasil_cv2, cmap='gray'), plt.title('OpenCV'), plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(hasil_man, cmap='gray'), plt.title('Manual'), plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(hasil_grn, cmap='gray'), plt.title('Green Only'), plt.axis('off')
plt.tight_layout()
plt.show()