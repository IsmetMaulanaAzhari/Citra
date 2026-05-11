import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Baca citra
    img_bgr = cv2.imread('objek.jpg')
    if img_bgr is None:
        print("File objek.jpg tidak ditemukan!")
        return
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # 1. Global thresholding dengan beberapa nilai
    thresholds = [80, 127, 180]
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Asli')
    plt.axis('off')

    for i, t in enumerate(thresholds):
        ret, thresh = cv2.threshold(img_gray, t, 255, cv2.THRESH_BINARY)
        plt.subplot(2, 3, i+2)
        plt.imshow(thresh, cmap='gray')
        plt.title(f'Global T={t}')
        plt.axis('off')

    # 2. Otsu
    ret_otsu, thresh_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.subplot(2, 3, 5)
    plt.imshow(thresh_otsu, cmap='gray')
    plt.title(f'Otsu (T={ret_otsu:.0f})')
    plt.axis('off')

    # 3. Adaptive (gunakan citra lain jika ada)
    img_doc = cv2.imread('dokumen.jpg', cv2.IMREAD_GRAYSCALE)
    if img_doc is not None:
        thresh_adapt_mean = cv2.adaptiveThreshold(img_doc, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                  cv2.THRESH_BINARY, 11, 2)
        plt.subplot(2, 3, 6)
        plt.imshow(thresh_adapt_mean, cmap='gray')
        plt.title('Adaptive Mean')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Simpan hasil
    cv2.imwrite('hasil_otsu.jpg', thresh_otsu)
    print("Hasil thresholding disimpan.")

if __name__ == '__main__':
    main()