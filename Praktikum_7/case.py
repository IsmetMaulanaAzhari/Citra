import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca citra dokumen (asumsikan nama file dokumen.jpg)
doc_bgr = cv2.imread('dokumen.jpg')
if doc_bgr is not None:
    doc_gray = cv2.cvtColor(doc_bgr, cv2.COLOR_BGR2GRAY)

    # 1. Menghilangkan noise dengan Median Blur
    denoised = cv2.medianBlur(doc_gray, 3)

    # 2. Sharpening dengan Unsharp Masking (amount 1.0)
    blur_for_unsharp = cv2.GaussianBlur(denoised, (5, 5), 0)
    final_result = cv2.addWeighted(denoised.astype(np.float32), 2.0,
                                   blur_for_unsharp.astype(np.float32), -1.0, 0)
    final_result = cv2.convertScaleAbs(final_result)

    # 3. Bandingkan dengan Sharpening TANPA blur (hanya langsung ditajamkan)
    blur_direct = cv2.GaussianBlur(doc_gray, (5, 5), 0)
    direct_sharp = cv2.addWeighted(doc_gray.astype(np.float32), 2.0,
                                   blur_direct.astype(np.float32), -1.0, 0)
    direct_sharp = cv2.convertScaleAbs(direct_sharp)

    titles = ['Asli (Noisy)', 'Hanya Sharpen (Buruk)', 'Median Blur', 'Median + Sharpen (Akhir)']
    images = [doc_gray, direct_sharp, denoised, final_result]

    plt.figure(figsize=(15, 5))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()