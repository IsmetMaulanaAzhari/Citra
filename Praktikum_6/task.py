import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew # Untuk menghitung skewness

def run_app():
    img_path = input("Masukkan nama file gambar (misal: bunga.jpg): ")
    img = cv2.imread(img_path)
    if img is None:
        print("Gambar tidak ditemukan. Pastikan nama file dan foldernya benar.")
        return
        
    print(f"Info Citra: Dimensi {img.shape}, Tipe Data {img.dtype}")
    
    while True:
        print("\nPilih Mode:\n1. Grayscale (Histogram & Eq)\n2. RGB (Per Saluran)\n3. YUV (Eq Luminance)\n4. CLAHE (Grayscale)\n5. Keluar")
        pilihan = input("Pilihan (1-5): ")
        
        if pilihan == '1':
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            eq = cv2.equalizeHist(gray)
            
            # Hitung metrik
            print(f"Mean: {np.mean(eq):.2f}, Std Dev: {np.std(eq):.2f}, Skewness: {skew(eq.ravel()):.2f}")
            
            # Visualisasi
            plt.figure(figsize=(10, 4))
            plt.subplot(1, 2, 1)
            plt.imshow(eq, cmap='gray')
            plt.title('Grayscale Equalized')
            plt.axis('off')
            
            plt.subplot(1, 2, 2)
            plt.hist(eq.ravel(), 256, [0,256], color='black')
            plt.title('Histogram Equalized')
            plt.show()
            
        elif pilihan == '2':
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            colors = ('red', 'green', 'blue')
            
            plt.figure(figsize=(6, 4))
            for i, color in enumerate(colors):
                hist = cv2.calcHist([img_rgb], [i], None, [256], [0, 256])
                plt.plot(hist, color=color)
            plt.title('Histogram RGB')
            plt.xlim([0, 256])
            plt.show()
            
        elif pilihan == '3':
            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
            img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
            img_eq_yuv = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.imshow(img_rgb)
            plt.title('Asli (RGB)')
            plt.axis('off')
            
            plt.subplot(1, 2, 2)
            plt.imshow(img_eq_yuv)
            plt.title('Equalized (Luminance YUV)')
            plt.axis('off')
            plt.show()
            
        elif pilihan == '4':
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            clahe_img = clahe.apply(gray)
            
            plt.figure(figsize=(10, 4))
            plt.subplot(1, 2, 1)
            plt.imshow(clahe_img, cmap='gray')
            plt.title('CLAHE Grayscale')
            plt.axis('off')
            
            plt.subplot(1, 2, 2)
            plt.hist(clahe_img.ravel(), 256, [0,256], color='blue')
            plt.title('Histogram CLAHE')
            plt.show()
            
        elif pilihan == '5':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Input tidak valid. Silakan masukkan angka 1-5.")

run_app()