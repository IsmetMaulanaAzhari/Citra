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