import cv2
import matplotlib.pyplot as plt

# Membaca citra (hasilnya dalam format BGR)
img = cv2.imread('contoh.jpg')

# Cek apakah citra berhasil dibaca
if img is None:
    print("Error: File tidak ditemukan")
else:
    # Konversi BGR ke RGB agar warna tampil normal di matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Menampilkan citra
    plt.imshow(img_rgb)
    plt.title('Citra Asli')
    plt.axis('off')  # Menghilangkan sumbu
    plt.show()

    # Menampilkan informasi dimensi
    print(f"Dimensi citra: {img.shape}")

"""Konversi ke Grayscale"""

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menampilkan hasil grayscale
plt.imshow(img_gray, cmap='gray')
plt.title('Citra Grayscale')
plt.axis('off')
plt.show()

"""Mengubah Ukuran Citra (Resize)"""

# Informasi dimensi grayscale
print(f"Dimensi grayscale: {img_gray.shape}")

img_resize = cv2.resize(img_rgb, (300, 300))

plt.imshow(img_resize)
plt.title('Citra Setelah Resize (300x300)')
plt.axis('off')
plt.show()

print(f"Dimensi setelah resize: {img_resize.shape}")

"""Menyimpan Citra Hasil"""

cv2.imwrite('hasil_grayscale.jpg', img_gray)
print("Citra grayscale berhasil disimpan sebagai 'hasil_grayscale.jpg'")

"""Kode Program (Lengkap)"""

import cv2
import matplotlib.pyplot as plt

def main():
    # 1. Membaca citra
    img = cv2.imread('contoh.jpg')
    if img is None:
        print("File tidak ditemukan!")
        return

    # 2. Konversi BGR ke RGB untuk ditampilkan
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 3. Menampilkan citra asli
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('Asli')
    plt.axis('off')

    # 4. Konversi ke grayscale dan tampilkan
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.subplot(1, 3, 2)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Grayscale')
    plt.axis('off')

    # 5. Resize dan tampilkan
    img_resize = cv2.resize(img_rgb, (150, 150))
    plt.subplot(1, 3, 3)
    plt.imshow(img_resize)
    plt.title('Resize 150x150')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # 6. Simpan hasil
    cv2.imwrite('hasil_grayscale.jpg', img_gray)
    print("Program selesai. Hasil tersimpan.")

if __name__ == "__main__":
    main()

"""Latihan 1 (Mudah)"""

import cv2

# Membaca citra
img_latihan1 = cv2.imread('contoh2.jpg')

# Memastikan gambar berhasil dibaca
if img_latihan1 is not None:
    # Mengambil dimensi dan channel dari atribut .shape
    tinggi, lebar, channel = img_latihan1.shape

    print("--- Latihan 1 ---")
    print(f"Dimensi citra: {tinggi} x {lebar} piksel")
    print(f"Jumlah channel: {channel}")

    # Menyimpan citra dengan nama baru
    cv2.imwrite('citra_salinan.jpg', img_latihan1)
    print("Citra berhasil disimpan sebagai 'citra_salinan.jpg'")
else:
    print("Error: File 'contoh2.jpg' tidak ditemukan!")

"""Latihan 2 (Sedang)"""

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

"""Latihan 3 (Sedang)"""

import cv2
import matplotlib.pyplot as plt

img_latihan3 = cv2.imread('contoh2.jpg')

if img_latihan3 is not None:
    # Konversi warna BGR ke RGB
    img_rgb = cv2.cvtColor(img_latihan3, cv2.COLOR_BGR2RGB)

    # Melakukan rotasi 90 derajat searah jarum jam
    img_rotated = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)

    # Menampilkan hasil rotasi
    plt.imshow(img_rotated)
    plt.title('Rotasi 90 Derajat Searah Jarum Jam')
    plt.axis('off')
    plt.show()

"""Latihan 2 (Sedang)"""

import cv2
import matplotlib.pyplot as plt

img_latihan4 = cv2.imread('contoh2.jpg')

if img_latihan4 is not None:
    # Konversi warna BGR ke RGB
    img_rgb = cv2.cvtColor(img_latihan4, cv2.COLOR_BGR2RGB)

    # Mendapatkan ukuran citra untuk mencari titik tengah
    tinggi, lebar, _ = img_rgb.shape
    tengah_y, tengah_x = tinggi // 2, lebar // 2

    # Menghitung batas crop untuk 100x100 piksel
    # Tarik 50 piksel ke atas, bawah, kiri, dan kanan dari titik tengah
    start_y = tengah_y - 50
    end_y = tengah_y + 50
    start_x = tengah_x - 50
    end_x = tengah_x + 50

    # Melakukan pemotongan (slicing array Numpy)
    img_cropped = img_rgb[start_y:end_y, start_x:end_x]

    # Menampilkan hasil crop
    plt.imshow(img_cropped)
    plt.title('Hasil Crop Bagian Tengah (100x100)')
    plt.axis('off')
    plt.show()

"""Studi Kasus"""

import cv2
import matplotlib.pyplot as plt

# 1. Ambil gambar jalan.jpg
img_jalan = cv2.imread('jalan.jpg')

if img_jalan is not None:
    # Konversi BGR ke RGB untuk tampilan citra asli di matplotlib
    img_jalan_rgb = cv2.cvtColor(img_jalan, cv2.COLOR_BGR2RGB)

    # 2. Ubah ukuran menjadi 512x512 piksel
    img_resized = cv2.resize(img_jalan_rgb, (512, 512))

    # 3. Konversi ke grayscale
    # Catatan: Kita gunakan img_resized yang masih RGB untuk dikonversi ke GRAY di matplotlib,
    # atau kita bisa ambil dari citra asli BGR lalu resize dan grayscale.
    # Agar lebih aman dari format OpenCV:
    img_bgr_resized = cv2.resize(img_jalan, (512, 512))
    img_gray = cv2.cvtColor(img_bgr_resized, cv2.COLOR_BGR2GRAY)

    # 4. Simpan dengan format jalan_preprocessed.jpg
    cv2.imwrite('jalan_preprocessed.jpg', img_gray)
    print("Citra berhasil disimpan sebagai 'jalan_preprocessed.jpg'")

    # 5. Tampilkan citra asli dan hasil preprocessing dalam satu figure (2 kolom)
    plt.figure(figsize=(12, 6))

    # Kolom 1: Citra Asli (RGB)
    plt.subplot(1, 2, 1)
    plt.imshow(img_jalan_rgb)
    plt.title('Citra Asli (Jalan)')
    plt.axis('off')

    # Kolom 2: Citra Preprocessed (Grayscale, 512x512)
    plt.subplot(1, 2, 2)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Hasil Preprocessing (Grayscale, 512x512)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Error: File 'jalan.jpg' tidak ditemukan!")

"""Tugas Mandiri"""

import cv2
import matplotlib.pyplot as plt

def apply_filter(image_path):
    # Membaca gambar dari direktori lokal
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Gambar tidak ditemukan!")
        return

    # Menu Interaktif di Terminal
    print("=== Aplikasi Web/CLI Sederhana Preview Filter Citra ===")
    print("Pilih Filter:")
    print("1. Grayscale")
    print("2. Blur (Gaussian 5x5)")
    print("3. Deteksi Tepi (Canny)")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    img_result = None
    title = ""
    is_gray_cmap = False

    if pilihan == '1':
        # Grayscale
        img_result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        title = "Filter: Grayscale"
        is_gray_cmap = True

    elif pilihan == '2':
        # Blur (GaussianBlur dengan kernel 5x5)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_result = cv2.GaussianBlur(img_rgb, (5, 5), 0)
        title = "Filter: Gaussian Blur"

    elif pilihan == '3':
        # Deteksi Tepi (Canny Edge Detection)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_result = cv2.Canny(img_gray, 100, 200)
        title = "Filter: Deteksi Tepi (Canny)"
        is_gray_cmap = True

    else:
        print("Pilihan tidak valid.")
        return

    # Menampilkan Hasil
    plt.figure(figsize=(6, 6))
    if is_gray_cmap:
        plt.imshow(img_result, cmap='gray')
    else:
        plt.imshow(img_result)

    plt.title(title)
    plt.axis('off')

    # PERBAIKAN: Gunakan block=False agar terminal jalan terus
    plt.show(block=False)
    # PERBAIKAN: Beri jeda sedikit agar jendela gambar merender visualnya
    plt.pause(0.1)

    # Opsi Menyimpan (sekarang muncul di terminal meski gambar masih terbuka)
    simpan = input("Apakah Anda ingin menyimpan hasil filter ini? (y/n): ").lower()

    if simpan == 'y':
        nama_file_simpan = "hasil_filter_" + pilihan + ".jpg"

        # Jika hasil adalah RGB (dari pilihan Blur), kembalikan ke BGR sebelum disimpan OpenCV
        if pilihan == '2':
            img_result_bgr = cv2.cvtColor(img_result, cv2.COLOR_RGB2BGR)
            cv2.imwrite(nama_file_simpan, img_result_bgr)
        else:
            cv2.imwrite(nama_file_simpan, img_result)

        print(f"Gambar berhasil disimpan sebagai '{nama_file_simpan}'")
    else:
        print("Gambar tidak disimpan.")

    # PERBAIKAN: Tutup jendela matplotlib secara otomatis setelah input selesai
    plt.close()

# Jalankan program
apply_filter('contoh.jpg')