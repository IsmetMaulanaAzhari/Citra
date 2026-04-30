import cv2
import matplotlib.pyplot as plt
import numpy as np

img_bgr = cv2.imread('pemandangan.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_gray_std = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY) # Standar OpenCV

# Konversi manual dengan bobot berbeda
img_rgb_float = img_rgb.astype(np.float32)
R = img_rgb_float[:,:,0]
G = img_rgb_float[:,:,1]
B = img_rgb_float[:,:,2]

# Rumus bobot latihan 2
gray_custom = (0.3 * R + 0.6 * G + 0.1 * B).astype(np.uint8)

# Tampilkan perbandingan
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_gray_std, cmap='gray')
plt.title('Standar OpenCV')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_custom, cmap='gray')
plt.title('Custom (0.3R + 0.6G + 0.1B)')
plt.axis('off')

plt.tight_layout()
plt.show()