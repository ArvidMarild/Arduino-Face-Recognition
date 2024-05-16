import cv2
import serial

# Start capturing video from the default camera
video = cv2.VideoCapture(0)

# Load Haar cascade classifier for face detection
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize LBPH face recognizer and load pre-trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer.yml')

# List to map recognized face indices to corresponding names
name_list = ["", "Arvid"]

# Open serial connection to communicate with external hardware
port = serial.Serial('COM7', 9600)

# Main loop for video processing
while True:
    # Read frame from video feed
    ret, frame = video.read()
    
    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    # Loop through detected faces
    for (x, y, w, h) in faces:
        # Recognize the face using LBPH recognizer
        ser, conf = recognizer.predict(gray[y:y+h, x:x+w])
        print(conf)
        
        # If confidence level is below 50, consider it a recognized face
        if conf < 50:
            # Draw green rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            
            # Display name associated with recognized index
            cv2.putText(frame, name_list[ser], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
            # Write '1' to the serial port
            port.write(str.encode('1'))
        else:
            # If confidence level is 50 or above, consider it an unknown face
            # Draw red rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 4)
            
            # Display "Unknown" text
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
            # Write '0' to the serial port
            port.write(str.encode('0'))

    # Display the processed frame
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video capture object and destroy OpenCV windows
video.release()
cv2.destroyAllWindows()