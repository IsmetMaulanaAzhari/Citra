import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

def process_image():
    filename = input("Masukkan nama file gambar (cth: bunga.jpg): ")
    img_bgr = cv2.imread(filename)
    
    if img_bgr is None:
        print("File tidak ditemukan.")
        return

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    while True:
        print("\n=== MENU FILTER ===")
        print("1. Averaging Blur")
        print("2. Gaussian Blur")
        print("3. Median Blur")
        print("4. Laplacian Sharpening")
        print("5. Unsharp Masking")
        print("0. Keluar")
        
        pilihan = input("Pilih filter (0-5): ")
        
        if pilihan == '0':
            break
            
        start_time = time.time()
        result = None
        title = ""
        laplacian_only = None # Khusus opsi 4
        
        if pilihan == '1':
            k = int(input("Masukkan ukuran kernel (cth: 5): "))
            result = cv2.blur(img_gray, (k, k))
            title = f"Averaging Blur ({k}x{k})"
            
        elif pilihan == '2':
            k = int(input("Masukkan ukuran kernel ganjil (cth: 5): "))
            sigma = float(input("Masukkan nilai sigma (cth: 0): "))
            result = cv2.GaussianBlur(img_gray, (k, k), sigma)
            title = f"Gaussian Blur ({k}x{k})"
            
        elif pilihan == '3':
            k = int(input("Masukkan ukuran kernel ganjil (cth: 5): "))
            result = cv2.medianBlur(img_gray, k)
            title = f"Median Blur ({k})"
            
        elif pilihan == '4':
            scale = float(input("Masukkan faktor penajaman (cth: 1.0): "))
            kernel_laplacian = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)
            laplacian = cv2.filter2D(img_gray, cv2.CV_32F, kernel_laplacian)
            laplacian_only = cv2.convertScaleAbs(laplacian)
            result = cv2.addWeighted(img_gray.astype(np.float32), 1.0, laplacian, scale, 0)
            result = cv2.convertScaleAbs(result)
            title = "Laplacian Sharpening"
            
        elif pilihan == '5':
            amount = float(input("Masukkan nilai amount (cth: 1.5): "))
            blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
            result = cv2.addWeighted(img_gray.astype(np.float32), 1.0 + amount, 
                                     blur.astype(np.float32), -amount, 0)
            result = cv2.convertScaleAbs(result)
            title = f"Unsharp Masking (amount={amount})"
            
        else:
            print("Pilihan tidak valid!")
            continue
            
        end_time = time.time()
        print(f"-> Waktu pemrosesan: {end_time - start_time:.4f} detik")
        
        # Tampilkan
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 3 if laplacian_only is not None else 2, 1)
        plt.imshow(img_gray, cmap='gray')
        plt.title("Asli")
        plt.axis('off')
        
        if laplacian_only is not None:
            plt.subplot(1, 3, 2)
            plt.imshow(laplacian_only, cmap='gray')
            plt.title("Tepi Laplacian")
            plt.axis('off')
            plt.subplot(1, 3, 3)
            plt.imshow(result, cmap='gray')
        else:
            plt.subplot(1, 2, 2)
            plt.imshow(result, cmap='gray')
            
        plt.title(title)
        plt.axis('off')
        plt.show()
        
        simpan = input("Simpan hasil ini? (y/n): ")
        if simpan.lower() == 'y':
            cv2.imwrite(f'hasil_{title.replace(" ", "_")}.jpg', result)
            print("Gambar disimpan.")

if __name__ == '__main__':
    process_image()
    pass