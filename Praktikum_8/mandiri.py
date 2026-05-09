import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def count_edge_pixels(edge_img):
    # Menghitung piksel non-zero (putih/tepi)
    return cv2.countNonZero(edge_img)

def main_app():
    img_path = ""
    img_gray = None
    img_rgb = None

    while True:
        print("\n--- Aplikasi Deteksi Tepi ---")
        print("1. Load Gambar")
        print("2. Sobel (Magnitude)")
        print("3. Canny")
        print("4. Laplacian of Gaussian (LoG)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            img_path = input("Masukkan nama file gambar (cth: gedung.jpg): ")
            if os.path.exists(img_path):
                img_bgr = cv2.imread(img_path)
                img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
                print("[INFO] Gambar berhasil dimuat.")
            else:
                print("[ERROR] File tidak ditemukan!")
                img_gray = None

        elif pilihan == '2':
            if img_gray is None: print("[ERROR] Load gambar dulu!"); continue
            sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
            sobel_mag = np.uint8(np.clip(np.sqrt(sobel_x**2 + sobel_y**2), 0, 255))

            pixels = count_edge_pixels(sobel_mag)
            print(f"[INFO] Jumlah piksel tepi: {pixels}")

            plt.imshow(sobel_mag, cmap='gray'); plt.title('Sobel Magnitude'); plt.axis('off'); plt.show()
            cv2.imwrite('hasil_sobel.jpg', sobel_mag)
            print("[INFO] Hasil disimpan sebagai hasil_sobel.jpg")

        elif pilihan == '3':
            if img_gray is None: print("[ERROR] Load gambar dulu!"); continue
            low = int(input("Masukkan ambang rendah Canny: "))
            high = int(input("Masukkan ambang tinggi Canny: "))
            edges = cv2.Canny(img_gray, low, high)

            pixels = count_edge_pixels(edges)
            print(f"[INFO] Jumlah piksel tepi: {pixels}")

            plt.imshow(edges, cmap='gray'); plt.title(f'Canny ({low}, {high})'); plt.axis('off'); plt.show()
            cv2.imwrite('hasil_canny.jpg', edges)
            print("[INFO] Hasil disimpan sebagai hasil_canny.jpg")

        elif pilihan == '4':
            if img_gray is None: print("[ERROR] Load gambar dulu!"); continue
            ksize = int(input("Masukkan ukuran kernel Gaussian (harus ganjil, cth: 3, 5, 7): "))
            if ksize % 2 == 0: print("[ERROR] Kernel harus ganjil!"); continue

            blurred = cv2.GaussianBlur(img_gray, (ksize, ksize), 0)
            laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
            laplacian = np.uint8(np.abs(laplacian))

            pixels = count_edge_pixels(laplacian)
            print(f"[INFO] Jumlah piksel tepi: {pixels}")

            plt.imshow(laplacian, cmap='gray'); plt.title(f'LoG (Kernel={ksize})'); plt.axis('off'); plt.show()
            cv2.imwrite('hasil_log.jpg', laplacian)
            print("[INFO] Hasil disimpan sebagai hasil_log.jpg")

        elif pilihan == '5':
            print("Keluar dari aplikasi.")
            break
        else:
            print("[ERROR] Pilihan tidak valid.")

if __name__ == '__main__':
    main_app()
    pass