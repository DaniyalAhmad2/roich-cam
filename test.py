import cv2
import sys

# Open the video capture device (/dev/video0)
cap = cv2.VideoCapture("/dev/video0")

if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

# Set a window name for display
window_name = "Camera Stream"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Display the resulting frame
    cv2.imshow(window_name, frame)

    # Wait for 1ms and check if 'q' is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
