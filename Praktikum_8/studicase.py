import cv2
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread('plat_nomor.jpg')
if img_bgr is not None:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # 1. Gaussian Blur
    blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # 2. Canny Edge Detection
    edges = cv2.Canny(blurred, 30, 150)

    # 3. Morfologi Close untuk menyambung tepi plat
    kernel = np.ones((5, 5), np.uint8)
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(closed_edges, cmap='gray')
    plt.title('Edges setelah Morph Close')
    plt.axis('off')

    plt.show()
else:
    print("Siapkan file plat_nomor.jpg terlebih dahulu.")