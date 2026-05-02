import cv2
import matplotlib.pyplot as plt
import numpy as np

img_bgr = cv2.imread('bunga.jpg')
if img_bgr is not None:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    amount = 1.5

    # Metode 1: Sharpening per channel RGB
    blur_rgb = cv2.GaussianBlur(img_rgb, (5, 5), 0)
    sharp_rgb = cv2.addWeighted(img_rgb.astype(np.float32), 1.0 + amount,
                                blur_rgb.astype(np.float32), -amount, 0)
    sharp_rgb = cv2.convertScaleAbs(sharp_rgb)

    # Metode 2: Sharpening pada channel Y (Luminance) dari YUV
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(img_yuv)

    blur_y = cv2.GaussianBlur(y, (5, 5), 0)
    sharp_y = cv2.addWeighted(y.astype(np.float32), 1.0 + amount,
                              blur_y.astype(np.float32), -amount, 0)
    sharp_y = cv2.convertScaleAbs(sharp_y)

    # Gabungkan kembali
    merged_yuv = cv2.merge([sharp_y, u, v])
    sharp_yuv_rgb = cv2.cvtColor(merged_yuv, cv2.COLOR_YUV2RGB)

    titles = ['Asli RGB', 'Sharpen RGB', 'Sharpen YUV']
    images = [img_rgb, sharp_rgb, sharp_yuv_rgb]

    plt.figure(figsize=(15, 5))
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.show()