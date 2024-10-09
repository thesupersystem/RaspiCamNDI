# Import necessary libraries
import cv2  # OpenCV library for accessing webcam feed
import ndi  # NDI library for sending video feed over the network

# Initialize the NDI sender
ndi.initialize()
sender_name = "Raspberry Pi Webcam"  # NDI stream name
sender = ndi.send_video(sender_name)

# Define the webcam source (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Frame dimensions (optional: set your preferred dimensions)
frame_width = 640
frame_height = 480

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# Capture webcam frames and send over NDI
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to RGB format (NDI requires RGB format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Send the frame via NDI
    sender.send(frame_rgb)  # Send the RGB frame

    # Display the frame locally (optional)
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to exit the loop and close the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
ndi.destroy()  # Clean up NDI resources
