import cv2
import matplotlib.pyplot as plt

def auto_threshold(img, method):
    """
    Fungsi untuk melakukan thresholding berdasarkan metode yang dipilih.
    Return: citra biner (thresh) dan nilai ambang (ret).
    """
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    ret = None
    if method == 'global':
        # Default global threshold
        ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    elif method == 'otsu':
        ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    elif method == 'adaptive_mean':
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                       cv2.THRESH_BINARY, 11, 2)
    elif method == 'adaptive_gauss':
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY, 11, 2)
    else:
        raise ValueError("Metode tidak dikenali!")
        
    return thresh, ret

# --- Cara Mengujinya ---
img_test = cv2.imread('objek.jpg', cv2.IMREAD_GRAYSCALE)
if img_test is not None:
    # Uji metode Otsu
    hasil_biner, nilai_t = auto_threshold(img_test, 'otsu')
    
    plt.imshow(hasil_biner, cmap='gray')
    plt.title(f'Hasil Fungsi auto_threshold (Otsu, T={nilai_t})')
    plt.axis('off')
    plt.show()