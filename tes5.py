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