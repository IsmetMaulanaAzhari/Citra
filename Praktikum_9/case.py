import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Baca Citra (Asumsikan objek lebih gelap dari background)
img_prod = cv2.imread('produk.jpg', cv2.IMREAD_GRAYSCALE)

if img_prod is not None:
    # 2. Terapkan Otsu Thresholding (Gunakan INV agar objek gelap menjadi putih/255)
    ret_otsu, thresh_otsu = cv2.threshold(img_prod, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 3. Operasi Morfologi (Closing: Dilasi lalu Erosi, untuk menutup lubang kecil di dalam objek)
    kernel = np.ones((5,5), np.uint8)
    img_clean = cv2.morphologyEx(thresh_otsu, cv2.MORPH_CLOSE, kernel)
    
    # Opsional: Jika ada noise putih kecil di background, tambahkan Opening
    img_clean = cv2.morphologyEx(img_clean, cv2.MORPH_OPEN, kernel)

    # 4. Hitung jumlah piksel putih (Luas Objek)
    area_pixels = cv2.countNonZero(img_clean)
    
    # 5. Thresholding Global Manual sebagai pembanding
    manual_t = 100
    _, thresh_global = cv2.threshold(img_prod, manual_t, 255, cv2.THRESH_BINARY_INV)

    # Visualisasi
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 4, 1)
    plt.imshow(img_prod, cmap='gray')
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(thresh_global, cmap='gray')
    plt.title(f'Global (T={manual_t})')
    plt.axis('off')
    
    plt.subplot(1, 4, 3)
    plt.imshow(thresh_otsu, cmap='gray')
    plt.title(f'Otsu Awal (T={ret_otsu})')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(img_clean, cmap='gray')
    plt.title(f'Setelah Morfologi\n(Luas: {area_pixels} px)')
    plt.axis('off')

    plt.show()
    print(f"Luas area objek terdeteksi: {area_pixels} piksel.")