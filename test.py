import cv2
import sys

# Open the video capture device (/dev/video0)
gst_pipeline = (
    "v4l2src device=/dev/video0 ! "
    "image/jpeg, width=1920, height=1080, framerate=30/1 ! "
    "jpegdec ! "
    "videoconvert ! "
    "video/x-raw,format=BGR ! "
    "queue max-size-buffers=1 leaky=downstream ! "
    "appsink drop=true max-buffers=1"
)
# Initialize Video Capture
cap = cv2.VideoCapture(gst_pipeline)

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
