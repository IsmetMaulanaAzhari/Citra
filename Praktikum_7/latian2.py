import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise

img_bgr = cv2.imread('bunga.jpg')
if img_bgr is not None:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Menambahkan noise salt-and-pepper
    noise_img = random_noise(img_gray, mode='s&p', amount=0.05)
    # skimage menghasilkan float [0, 1], kembalikan ke uint8 [0, 255]
    noise_img = np.array(255 * noise_img, dtype='uint8')

    # Median blur
    median_3 = cv2.medianBlur(noise_img, 3)
    median_5 = cv2.medianBlur(noise_img, 5)
    median_7 = cv2.medianBlur(noise_img, 7)

    titles = ['Citra + Noise', 'Median (3)', 'Median (5)', 'Median (7)']
    images = [noise_img, median_3, median_5, median_7]

    plt.figure(figsize=(15, 5))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()