import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Baca citra
    img_bgr = cv2.imread('gedung.jpg')
    if img_bgr is None:
        print("File tidak ditemukan!")
        return
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # 1. Sobel
    sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_mag = np.uint8(np.clip(sobel_mag, 0, 255))

    # 2. Canny
    edges_canny = cv2.Canny(img_gray, 50, 150)

    # 3. Laplacian of Gaussian
    blurred = cv2.GaussianBlur(img_gray, (5,5), 0)
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    laplacian = np.uint8(np.abs(laplacian))

    # Tampilkan semua
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(img_rgb)
    plt.title('Asli')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(sobel_mag, cmap='gray')
    plt.title('Sobel Magnitude')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(edges_canny, cmap='gray')
    plt.title('Canny')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian of Gaussian')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Simpan hasil
    cv2.imwrite('edges_sobel.jpg', sobel_mag)
    cv2.imwrite('edges_canny.jpg', edges_canny)
    cv2.imwrite('edges_laplacian.jpg', laplacian)
    print("Hasil deteksi tepi disimpan.")

if __name__ == '__main__':
    main()
