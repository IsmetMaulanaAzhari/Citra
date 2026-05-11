import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def show_with_histogram(img_gray, thresh_img, threshold_value, title):
    """Menampilkan gambar asli, hasil biner, dan histogram dengan garis batas threshold."""
    plt.figure(figsize=(15, 4))
    
    # Gambar Asli
    plt.subplot(1, 3, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Citra Grayscale')
    plt.axis('off')
    
    # Histogram
    plt.subplot(1, 3, 2)
    plt.hist(img_gray.ravel(), bins=256, range=[0, 256], color='gray')
    if threshold_value is not None:
        plt.axvline(x=threshold_value, color='r', linestyle='dashed', linewidth=2, label=f'T={threshold_value}')
        plt.legend()
    plt.title('Histogram')
    
    # Hasil Biner
    plt.subplot(1, 3, 3)
    plt.imshow(thresh_img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def main_app():
    img_gray = None
    
    while True:
        print("\n" + "="*40)
        print(" APLIKASI THRESHOLDING INTERAKTIF")
        print("="*40)
        print("1. Load Gambar")
        print("2. Pilih Metode Thresholding")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-3): ")
        
        if pilihan == '1':
            filepath = input("Masukkan path/nama file gambar (cth: objek.jpg): ")
            if os.path.exists(filepath):
                img = cv2.imread(filepath)
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                print(f"[+] Gambar '{filepath}' berhasil dimuat.")
            else:
                print("[-] File tidak ditemukan! Pastikan nama file benar.")
                
        elif pilihan == '2':
            if img_gray is None:
                print("[-] Load gambar terlebih dahulu (Pilih menu 1).")
                continue
                
            print("\nMetode Thresholding:")
            print("a. Global Binary")
            print("b. Global Inverse")
            print("c. Otsu")
            print("d. Adaptive Mean")
            print("e. Adaptive Gaussian")
            
            metode = input("Pilih metode (a/b/c/d/e): ").lower()
            result_img = None
            
            if metode == 'a':
                t = int(input("Masukkan nilai Threshold (0-255): "))
                _, result_img = cv2.threshold(img_gray, t, 255, cv2.THRESH_BINARY)
                show_with_histogram(img_gray, result_img, t, f'Global Binary (T={t})')
                
            elif metode == 'b':
                t = int(input("Masukkan nilai Threshold (0-255): "))
                _, result_img = cv2.threshold(img_gray, t, 255, cv2.THRESH_BINARY_INV)
                show_with_histogram(img_gray, result_img, t, f'Global Inverse (T={t})')
                
            elif metode == 'c':
                ret, result_img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                show_with_histogram(img_gray, result_img, ret, f'Otsu (T={ret:.0f})')
                
            elif metode in ['d', 'e']:
                print("\n[INFO] Block Size harus berupa angka GANJIL (cth: 3, 5, 11) [cite: 233]")
                block_size = int(input("Masukkan blockSize: "))
                c_val = int(input("Masukkan nilai konstanta C: "))
                
                if block_size % 2 == 0:
                    print("[-] Block size harus ganjil! Menggunakan default 11.")
                    block_size = 11
                    
                if metode == 'd':
                    result_img = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                                       cv2.THRESH_BINARY, block_size, c_val)
                    title = 'Adaptive Mean'
                else:
                    result_img = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                       cv2.THRESH_BINARY, block_size, c_val)
                    title = 'Adaptive Gaussian'
                
                # Adaptive tidak memiliki 1 garis threshold tetap untuk histogram
                show_with_histogram(img_gray, result_img, None, title)
                
            else:
                print("[-] Pilihan metode tidak valid.")
                continue

            # Simpan hasil
            if result_img is not None:
                simpan = input("Apakah Anda ingin menyimpan hasil ini? (y/n): ").lower()
                if simpan == 'y':
                    nama_file = input("Masukkan nama file untuk menyimpan (cth: hasil.jpg): ")
                    cv2.imwrite(nama_file, result_img)
                    print(f"[+] Hasil berhasil disimpan sebagai {nama_file} [cite: 229]")
                    
        elif pilihan == '3':
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("[-] Pilihan tidak valid.")

if __name__ == "__main__":
    main_app()