import cv2
import numpy as np
import matplotlib.pyplot as plt

img_color = cv2.imread('coin.jpg') # Gunakan citra berwarna apa saja yang Anda miliki

if img_color is not None:
    # Konversi ke grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Adaptive Thresholding (Gunakan Inverse agar objek putih, background hitam)
    thresh_adapt = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                         cv2.THRESH_BINARY_INV, 11, 2)

    # Operasi Morfologi untuk membersihkan noise
    kernel = np.ones((3,3), np.uint8)
    
    # Erosion untuk menghapus noise kecil (titik-titik putih di background)
    img_eroded = cv2.erode(thresh_adapt, kernel, iterations=1)
    
    # Dilation untuk mengembalikan ukuran objek setelah di-erode
    img_dilated = cv2.dilate(img_eroded, kernel, iterations=1)
    
    # Alternatif: Bisa langsung menggunakan cv2.MORPH_OPEN yang merupakan gabungan erosi lalu dilasi
    img_morph = cv2.morphologyEx(thresh_adapt, cv2.MORPH_OPEN, kernel)

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(thresh_adapt, cmap='gray')
    plt.title('Adaptive Thresholding (Banyak Noise)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(img_morph, cmap='gray')
    plt.title('Setelah Morfologi (Opening)')
    plt.axis('off')

    plt.show()