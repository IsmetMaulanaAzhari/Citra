import cv2
import os
import matplotlib.pyplot as plt

folder_path = 'produk/'
valid_images = []

print("=== Laporan Verifikasi Dataset ===")
if not os.path.exists(folder_path):
    print(f"Folder '{folder_path}' tidak ditemukan!")
else:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Melewati direktori, hanya memproses file
        if os.path.isdir(file_path):
            continue
            
        img = cv2.imread(file_path)
        
        if img is None:
            print(f"[INVALID] {filename} -> Gagal dibaca. (Mencatat ke log...)")
            # Simulasi catat log (bisa ditulis ke txt/csv dalam praktiknya)
        else:
            print(f"[VALID]   {filename} -> Dimensi: {img.shape}")
            valid_images.append(img)

# Menampilkan 5 gambar pertama dalam satu grid figure
if valid_images:
    limit = min(5, len(valid_images))
    fig, axes = plt.subplots(1, limit, figsize=(15, 3))
    
    # Jika hanya 1 gambar, axes tidak berbentuk list/array
    if limit == 1:
        axes = [axes]
        
    for i in range(limit):
        # Konversi BGR ke RGB untuk visualisasi yang benar
        img_rgb = cv2.cvtColor(valid_images[i], cv2.COLOR_BGR2RGB)
        axes[i].imshow(img_rgb)
        axes[i].set_title(f"Gambar {i+1}")
        axes[i].axis('off')
        
    plt.tight_layout()
    plt.show()