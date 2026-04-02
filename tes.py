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

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menampilkan hasil grayscale
plt.imshow(img_gray, cmap='gray')
plt.title('Citra Grayscale')
plt.axis('off')
plt.show()

# Informasi dimensi grayscale
print(f"Dimensi grayscale: {img_gray.shape}")

img_resize = cv2.resize(img_rgb, (300, 300))

plt.imshow(img_resize)
plt.title('Citra Setelah Resize (300x300)')
plt.axis('off')
plt.show()

print(f"Dimensi setelah resize: {img_resize.shape}")


cv2.imwrite('hasil_grayscale.jpg', img_gray)
print("Citra grayscale berhasil disimpan sebagai 'hasil_grayscale.jpg'")
