import cv2
import matplotlib.pyplot as plt

# Baca citra dokumen berbayang
img = cv2.imread('gambar2.png', cv2.IMREAD_GRAYSCALE)

# Otsu Thresholding
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive Thresholding (Gaussian)
thresh_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 11, 2)

# Plot Hasil
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(thresh_otsu, cmap='gray'); axes[0].set_title('Otsu Thresholding')
axes[1].imshow(thresh_adaptive, cmap='gray'); axes[1].set_title('Adaptive Gaussian')
for ax in axes: ax.axis('off')
plt.show()