import cv2
import matplotlib.pyplot as plt
import numpy as np

def tampilkan_histogram(img, judul):
    plt.hist(img.ravel(), bins=256, range=[0,256])
    plt.title(f'Histogram - {judul}')
    plt.show()

def main_menu():
    img = None
    img_gray_active = None
    
    while True:
        print("\n--- Aplikasi Konversi Warna ---")
        print("1. Load Gambar")
        print("2. Tampilkan Informasi")
        print("3. Konversi ke Grayscale (OpenCV) & Histogram")
        print("4. Konversi Saluran Tunggal & Histogram")
        print("5. Simpan Hasil")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            path = input("Masukkan nama file (contoh: bunga.jpg): ")
            img = cv2.imread(path)
            if img is None:
                print("Error: File tidak ditemukan!")
            else:
                print("Gambar berhasil dimuat.")
                
        elif pilihan == '2':
            if img is not None:
                h, w, c = img.shape
                print(f"Dimensi: {w} x {h}")
                print(f"Jumlah saluran: {c}")
            else:
                print("Load gambar terlebih dahulu!")
                
        elif pilihan == '3':
            if img is not None:
                img_gray_active = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                mean, std = cv2.meanStdDev(img_gray_active)
                median = np.median(img_gray_active)
                
                print(f"Statistik - Mean: {mean[0][0]:.2f}, Median: {median}, Std Dev: {std[0][0]:.2f}")
                
                plt.imshow(img_gray_active, cmap='gray')
                plt.title('Grayscale OpenCV')
                plt.show()
                tampilkan_histogram(img_gray_active, "OpenCV")
            else:
                print("Load gambar terlebih dahulu!")
                
        elif pilihan == '4':
             if img is not None:
                 saluran = input("Pilih saluran (R/G/B): ").upper()
                 # Ingat OpenCV formatnya BGR (0=B, 1=G, 2=R)
                 idx = {'B': 0, 'G': 1, 'R': 2}.get(saluran, -1)
                 
                 if idx != -1:
                     img_gray_active = img[:,:,idx]
                     plt.imshow(img_gray_active, cmap='gray')
                     plt.title(f'Grayscale Saluran {saluran}')
                     plt.show()
                     tampilkan_histogram(img_gray_active, f"Saluran {saluran}")
                 else:
                     print("Saluran tidak valid!")
             else:
                print("Load gambar terlebih dahulu!")
                
        elif pilihan == '5':
            if img_gray_active is not None:
                nama_simpan = input("Masukkan nama file untuk menyimpan (contoh: hasil.jpg): ")
                cv2.imwrite(nama_simpan, img_gray_active)
                print(f"Disimpan sebagai {nama_simpan}")
            else:
                print("Belum ada citra grayscale yang dikonversi!")
                
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_menu()