import cv2

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Set up the video capture device
video_capture = cv2.VideoCapture(0)

# Define a function to detect and track faces in real-time video
def detect_faces():
    # Read in a frame of video from the capture device
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use the face cascade classifier to detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the video feed with face detection
    cv2.imshow('Video', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False

    return True

# Loop over the video frames and detect faces in real-time
while True:
    # Exit the loop if the user presses 'q'
    if not detect_faces():
        break

# Release the video capture device and close the window
video_capture.release()
cv2.destroyAllWindows()
