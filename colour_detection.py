
import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam!")
        break

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red color
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Find objects in the mask
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        # Ignore small areas
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            # Draw a rectangle around the object
            cv2.rectangle(
                frame, (x, y), (x + w, y + h),
                (0, 255, 0), 2
            )

            cv2.putText(
                frame, "Red Object",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2
            )

    # Display webcam and mask
    cv2.imshow("Color Detection", frame)
    cv2.imshow("Red Color Mask", mask)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()