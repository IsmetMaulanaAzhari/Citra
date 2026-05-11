import cv2
import matplotlib.pyplot as plt

img_doc = cv2.imread('dokumen.jpg', cv2.IMREAD_GRAYSCALE)

if img_doc is not None:
    # 1. Global Thresholding
    _, thresh_global = cv2.threshold(img_doc, 127, 255, cv2.THRESH_BINARY)

    # 2. Adaptive Mean
    thresh_mean = cv2.adaptiveThreshold(img_doc, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                        cv2.THRESH_BINARY, 11, 2)

    # 3. Adaptive Gaussian
    thresh_gauss = cv2.adaptiveThreshold(img_doc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                         cv2.THRESH_BINARY, 11, 2)

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(thresh_global, cmap='gray')
    plt.title('Global (T=127)')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(thresh_mean, cmap='gray')
    plt.title('Adaptive Mean')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(thresh_gauss, cmap='gray')
    plt.title('Adaptive Gaussian')
    plt.axis('off')

    plt.show()