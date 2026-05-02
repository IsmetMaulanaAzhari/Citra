import cv2
import matplotlib.pyplot as plt

# Membaca citra
img_bgr = cv2.imread('bunga.jpg')
if img_bgr is not None:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Averaging blur dengan berbagai kernel
    blur_3x3 = cv2.blur(img_rgb, (3, 3))
    blur_7x7 = cv2.blur(img_rgb, (7, 7))
    blur_11x11 = cv2.blur(img_rgb, (11, 11))

    # Menampilkan hasil
    titles = ['Asli', 'Averaging 3x3', 'Averaging 7x7', 'Averaging 11x11']
    images = [img_rgb, blur_3x3, blur_7x7, blur_11x11]

    plt.figure(figsize=(15, 5))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()
else:
    print("Gambar bunga.jpg tidak ditemukan!")