import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('gedung.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Konversi BGR ke YUV
img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)
# Ekstrak channel Y (Luminance)
y_channel = img_yuv[:, :, 0]

edges_gray = cv2.Canny(img_gray, 50, 150)
edges_yuv = cv2.Canny(y_channel, 50, 150)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(edges_gray, cmap='gray')
plt.title('Canny on Grayscale')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges_yuv, cmap='gray')
plt.title('Canny on Y-Channel (YUV)')
plt.axis('off')

plt.show()