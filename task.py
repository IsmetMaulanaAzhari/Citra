import cv2
import os
import matplotlib.pyplot as plt

def jalankan_gallery():
    folder_path = input("Masukkan path folder yang berisi gambar (contoh: ./produk): ")
    
    if not os.path.exists(folder_path):
        print("Folder tidak ditemukan!")
        return

    # Filter hanya file gambar
    valid_ext = ('.jpg', '.jpeg', '.png')
    list_gambar = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_ext)]
    
    if not list_gambar:
        print("Tidak ada file gambar di dalam folder tersebut.")
        return

    while True:
        print("\n--- Daftar Gambar ---")
        for i, nama in enumerate(list_gambar):
            print(f"[{i}] {nama}")
            
        pilihan = input("\nMasukkan nomor indeks gambar (atau ketik 'q' untuk keluar): ")
        
        if pilihan.lower() == 'q':
            print("Keluar dari program. Terima kasih!")
            break
            
        try:
            idx = int(pilihan)
            if idx < 0 or idx >= len(list_gambar):
                print("Indeks di luar jangkauan!")
                continue
                
            # Navigasi Loop
            while True:
                filename = list_gambar[idx]
                filepath = os.path.join(folder_path, filename)
                
                # Baca informasi gambar
                img = cv2.imread(filepath)
                if img is None:
                    print(f"Gagal membaca gambar {filename}.")
                    break
                    
                ukuran_kb = os.path.getsize(filepath) / 1024
                
                # Tampilkan dengan Matplotlib
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                plt.figure("Gallery", figsize=(8, 6))
                plt.imshow(img_rgb)
                plt.title(f"Nama: {filename} | Dimensi: {img.shape} | Ukuran: {ukuran_kb:.2f} KB")
                plt.axis('off')
                
                # plt.show(block=False) agar program terminal tetap berjalan
                plt.show(block=False)
                plt.pause(0.1) # Memberi waktu figure untuk render
                
                navigasi = input("\nKetikan: [n] Next, [p] Prev, [k] Kembali ke daftar: ")
                plt.close() # Tutup jendela gambar saat user memasukkan input
                
                if navigasi.lower() == 'n':
                    idx = (idx + 1) % len(list_gambar)
                elif navigasi.lower() == 'p':
                    idx = (idx - 1) % len(list_gambar)
                elif navigasi.lower() == 'k':
                    break
                else:
                    print("Input tidak valid, kembali ke daftar.")
                    break
                    
        except ValueError:
            print("Input harus berupa angka atau 'q'!")

if __name__ == '__main__':
    jalankan_gallery()