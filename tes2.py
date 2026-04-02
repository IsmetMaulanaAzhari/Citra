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