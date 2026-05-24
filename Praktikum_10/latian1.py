import cv2
import matplotlib.pyplot as plt

# Baca citra koin (Latar seragam)
img = cv2.imread('gambar1.jpg', cv2.IMREAD_GRAYSCALE)

# Thresholding dengan berbagai nilai T
_, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
_, thresh3 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Plot Hasil
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(thresh1, cmap='gray'); axes[0].set_title('T = 100')
axes[1].imshow(thresh2, cmap='gray'); axes[1].set_title('T = 150')
axes[2].imshow(thresh3, cmap='gray'); axes[2].set_title('T = 200')
for ax in axes: ax.axis('off')
plt.show()