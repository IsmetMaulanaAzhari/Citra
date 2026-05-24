import cv2
import matplotlib.pyplot as plt

# Baca citra pemandangan/objek jelas
img = cv2.imread('gambar3.jpg', cv2.IMREAD_GRAYSCALE)

# Canny dengan variasi threshold
edges1 = cv2.Canny(img, 30, 100)
edges2 = cv2.Canny(img, 50, 150)
edges3 = cv2.Canny(img, 100, 200)

# Plot Hasil
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(edges1, cmap='gray'); axes[0].set_title('Canny (30, 100)')
axes[1].imshow(edges2, cmap='gray'); axes[1].set_title('Canny (50, 150)')
axes[2].imshow(edges3, cmap='gray'); axes[2].set_title('Canny (100, 200)')
for ax in axes: ax.axis('off')
plt.show()