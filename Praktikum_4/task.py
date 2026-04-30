import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def show_image(img, title="Image"):
    """Fungsi pembantu untuk menampilkan gambar"""
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6, 4))
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show(block=False)
    plt.pause(1)
    plt.close()

def main_editor():
    current_img = None
    
    while True:
        print("\n=== APLIKASI EDITOR CITRA SEDERHANA ===")
        print("1. Load Gambar")
        print("2. Resize")
        print("3. Crop")
        print("4. Rotate")
        print("5. Simpan")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            path = input("Masukkan path gambar (contoh: bunga.jpg): ")
            if not os.path.exists(path):
                print("Error: File tidak ditemukan!")
                continue
            current_img = cv2.imread(path)
            h, w = current_img.shape[:2]
            print(f"Gambar berhasil dimuat. Ukuran: {w}x{h} piksel.")
            show_image(current_img, "Loaded Image")
            
        elif pilihan == '2':
            if current_img is None:
                print("Error: Load gambar terlebih dahulu!")
                continue
            try:
                new_w = int(input("Masukkan lebar baru: "))
                new_h = int(input("Masukkan tinggi baru: "))
                current_img = cv2.resize(current_img, (new_w, new_h))
                print("Resize berhasil!")
                show_image(current_img, "Hasil Resize")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                
        elif pilihan == '3':
            if current_img is None:
                print("Error: Load gambar terlebih dahulu!")
                continue
            h, w = current_img.shape[:2]
            try:
                print(f"Batas maksimal: x={w}, y={h}")
                x1 = int(input("Masukkan x1 (kiri): "))
                y1 = int(input("Masukkan y1 (atas): "))
                x2 = int(input("Masukkan x2 (kanan): "))
                y2 = int(input("Masukkan y2 (bawah): "))
                
                # Validasi input crop
                if 0 <= x1 < x2 <= w and 0 <= y1 < y2 <= h:
                    current_img = current_img[y1:y2, x1:x2]
                    print("Crop berhasil!")
                    show_image(current_img, "Hasil Crop")
                else:
                    print("Koordinat crop tidak valid/melebihi batas citra! ")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                
        elif pilihan == '4':
            if current_img is None:
                print("Error: Load gambar terlebih dahulu!")
                continue
            print("Pilih Rotasi:")
            print("a. 90° CW")
            print("b. 90° CCW")
            print("c. 180°")
            print("d. Sudut Bebas")
            rot_choice = input("Pilih (a/b/c/d): ").lower()
            
            if rot_choice == 'a':
                current_img = cv2.rotate(current_img, cv2.ROTATE_90_CLOCKWISE)
            elif rot_choice == 'b':
                current_img = cv2.rotate(current_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            elif rot_choice == 'c':
                current_img = cv2.rotate(current_img, cv2.ROTATE_180)
            elif rot_choice == 'd':
                try:
                    angle = float(input("Masukkan sudut (derajat): "))
                    # Menggunakan fungsi rotate_free dari modul
                    current_img = rotate_free(current_img, angle)
                except ValueError:
                    print("Sudut tidak valid.")
                    continue
            else:
                print("Pilihan tidak valid.")
                continue
            print("Rotasi berhasil!")
            show_image(current_img, "Hasil Rotasi")
                
        elif pilihan == '5':
            if current_img is None:
                print("Error: Tidak ada gambar yang bisa disimpan!")
                continue
            save_path = input("Masukkan nama file untuk menyimpan (contoh: hasil.jpg): ")
            cv2.imwrite(save_path, current_img)
            print(f"Gambar berhasil disimpan di {save_path}")
            
        elif pilihan == '6':
            print("Keluar dari program. Terima kasih!")
            break
            
        else:
            print("Pilihan tidak ada di menu. Silakan coba lagi.")

# Uncomment untuk menjalankan editor
if __name__ == '__main__':
     main_editor()