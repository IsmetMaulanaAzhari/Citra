import cv2

cap = cv2.VideoCapture(0)

print("Tekan 'q' untuk keluar dari kamera.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal mengambil frame dari kamera.")
        break
        
    cv2.imshow('Kamera Webcam', frame)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()