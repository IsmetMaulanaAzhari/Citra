import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread('coin.jpg', cv2.IMREAD_GRAYSCALE)

if img_gray is not None:
    # Thresholding Global Terbaik (Asumsi dari Latihan 1, misalnya T=150)
    best_t = 150
    _, thresh_global = cv2.threshold(img_gray, best_t, 255, cv2.THRESH_BINARY)

    # Thresholding Otsu
    ret_otsu, thresh_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(thresh_global, cmap='gray')
    plt.title(f'Global Terbaik (T={best_t})')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh_otsu, cmap='gray')
    plt.title(f'Otsu (T Otomatis={ret_otsu:.0f})')
    plt.axis('off')

    plt.show()