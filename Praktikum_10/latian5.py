import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gambar2.jpg', cv2.IMREAD_GRAYSCALE)

# 1. Adaptive Thresholding
thresh_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY_INV, 11, 2)

# 2. Operasi Morfologi untuk membersihkan noise
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh_adaptive, cv2.MORPH_OPEN, kernel) # Menghilangkan bintik hitam/putih kecil
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) # Menutup lubang di dalam objek

# Plot Perbandingan
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(thresh_adaptive, cmap='gray'); axes[0].set_title('Sebelum Morfologi')
axes[1].imshow(closing, cmap='gray'); axes[1].set_title('Setelah Morfologi (Clean)')
for ax in axes: ax.axis('off')
plt.show()