import cv2

def nothing(x):
    pass

def canny_with_trackbar():
    img_bgr = cv2.imread('gedung.jpg')
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    cv2.namedWindow('Canny Interactive')
    cv2.createTrackbar('Low', 'Canny Interactive', 50, 255, nothing)
    cv2.createTrackbar('High', 'Canny Interactive', 150, 255, nothing)

    while True:
        low = cv2.getTrackbarPos('Low', 'Canny Interactive')
        high = cv2.getTrackbarPos('High', 'Canny Interactive')
        
        edges = cv2.Canny(img_gray, low, high)
        cv2.imshow('Canny Interactive', edges)
        
        # Tekan 'q' atau 'ESC' untuk keluar
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            break

    cv2.destroyAllWindows()

canny_with_trackbar()