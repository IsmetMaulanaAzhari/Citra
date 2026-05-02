import cv2
import matplotlib.pyplot as plt
import numpy as np

img_bgr = cv2.imread('bunga.jpg')
if img_bgr is not None:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    amounts = [0.5, 1.0, 2.0]
    unsharp_results = []

    for amount in amounts:
        # Formula: sharp = original + amount * (original - blurred)
        unsharp = cv2.addWeighted(img_gray.astype(np.float32), 1.0 + amount,
                                  blur.astype(np.float32), -amount, 0)
        unsharp_results.append(cv2.convertScaleAbs(unsharp))

    titles = ['Asli'] + [f'Unsharp (amount={a})' for a in amounts]
    images = [img_gray] + unsharp_results

    plt.figure(figsize=(15, 5))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()