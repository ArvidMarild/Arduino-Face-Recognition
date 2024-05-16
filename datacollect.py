import cv2 

# Start capturing video from the default camera
video = cv2.VideoCapture(0)

# Load Haar cascade classifier for face detection
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Prompt user to enter their ID
id = input("Enter Your ID: ")

# Initialize counter for captured images
count = 0

# Main loop for capturing dataset
while True:
    # Read frame from video feed
    ret, frame = video.read()
    
    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    # Loop through detected faces
    for (x, y, w, h) in faces:
        # Increment counter for each detected face
        count += 1
        
        # Save the detected face as an image with format: User.<ID>.<Count>.jpg
        cv2.imwrite('datasets/User.' + str(id) + "." + str(count) + ".jpg", gray[y:y+h, x:x+w])
        
        # Draw rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    # Display the frame with rectangles
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Break the loop if 500 images have been captured
    if count > 500:
        break

# Release video capture object and destroy OpenCV windows
video.release()
cv2.destroyAllWindows()

# Print message indicating dataset collection is done
print("Dataset Collection Done..................")
