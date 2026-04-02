import cv2
import matplotlib.pyplot as plt

def tampilkan_resize(nama_file, ukuran_target):
    # Membaca citra
    img = cv2.imread(nama_file)
    if img is None:
        print(f"File {nama_file} tidak ditemukan!")
        return

    # Konversi BGR ke RGB agar warna sesuai di Matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Melakukan resize citra sesuai target (lebar, tinggi)
    img_resized = cv2.resize(img_rgb, ukuran_target)

    # Menyiapkan canvas figure untuk menampilkan berdampingan
    plt.figure(figsize=(10, 5))

    # Subplot 1: Citra Asli
    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title('Citra Asli')
    plt.axis('off')

    # Subplot 2: Citra Resize
    plt.subplot(1, 2, 2)
    plt.imshow(img_resized)
    plt.title(f'Citra Resize {ukuran_target}')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Memanggil fungsi untuk Latihan 2
# Contoh: Mengubah ukuran menjadi 200x200
tampilkan_resize('contoh2.jpg', (200, 200))