import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert to grayscale and invert
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = 255 - gray  

    # Apply Otsu's threshold
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Compute rotated bounding box
    coords = np.column_stack(np.where(thresh > 0))
    if len(coords) == 0:
        continue  # Skip if no foreground pixels detected

    angle = cv2.minAreaRect(coords)[-1]

    # Adjust angle
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    print("Skew angle: ", angle)

    # Rotate image to deskew
    (h, w) = frame.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(frame, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Display the original and rotated frames
    cv2.imshow('Webcam Feed', frame)
    cv2.imshow('Rotated', rotated)
    time.sleep(1)
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
