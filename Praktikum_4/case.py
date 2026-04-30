import os
import cv2
import glob

def preprocess_dataset():
    input_folder = 'bunga/'
    output_folder = 'preprocessed/'

    # Buat folder output jika belum ada
    os.makedirs(output_folder, exist_ok=True)

    # Ambil semua file jpg dan png di dalam folder bunga/ [cite: 228, 229]
    image_files = glob.glob(os.path.join(input_folder, '*.*'))
    processed_count = 0

    for file_path in image_files:
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)

        img = cv2.imread(file_path)
        if img is None:
            continue

        # 1. Resize ke 224x224
        img_resized = cv2.resize(img, (224, 224))

        # Simpan hasil resize utama
        cv2.imwrite(os.path.join(output_folder, filename), img_resized)

        # 2. Augmentasi Rotasi
        # Rotasi 90
        img_rot90 = cv2.rotate(img_resized, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(output_folder, f"{name}_rot90{ext}"), img_rot90)

        # Rotasi 180
        img_rot180 = cv2.rotate(img_resized, cv2.ROTATE_180)
        cv2.imwrite(os.path.join(output_folder, f"{name}_rot180{ext}"), img_rot180)

        # Rotasi 270 (Sama dengan 90 CCW)
        img_rot270 = cv2.rotate(img_resized, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(os.path.join(output_folder, f"{name}_rot270{ext}"), img_rot270)

        processed_count += 1

    print(f"Studi Kasus Selesai! Laporan: {processed_count} gambar asli berhasil diproses menjadi {processed_count * 4} gambar (termasuk augmentasi).")

preprocess_dataset()