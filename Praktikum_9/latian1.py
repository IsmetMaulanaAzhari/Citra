import cv2
import matplotlib.pyplot as plt

# Membaca citra dan konversi ke grayscale
img_bgr = cv2.imread('coin.jpg')
if img_bgr is not None:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Menyiapkan list threshold
    thresholds = [100, 150, 200]
    
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    # Looping untuk setiap nilai threshold
    for i, t in enumerate(thresholds):
        ret, thresh = cv2.threshold(img_gray, t, 255, cv2.THRESH_BINARY)
        plt.subplot(1, 4, i+2)
        plt.imshow(thresh, cmap='gray')
        plt.title(f'Global T={t}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("File coin.jpg tidak ditemukan!")