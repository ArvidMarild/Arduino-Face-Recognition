import cv2
import numpy as np
from PIL import Image
import os

# Create LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to the dataset directory
path = "datasets"

# Function to get IDs and face data from images in the dataset directory
def getImageID(path):
    # List all image paths in the dataset directory
    imagePath = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []  # List to store face images
    ids = []    # List to store corresponding IDs
    for imagePaths in imagePath:
        # Open image and convert it to grayscale
        faceImage = Image.open(imagePaths).convert('L')
        # Convert image to NumPy array
        faceNP = np.array(faceImage)
        # Get the ID from the filename
        Id = (os.path.split(imagePaths)[-1].split(".")[1])
        # Convert ID to integer
        Id = int(Id)
        # Append face data and ID to lists
        faces.append(faceNP)
        ids.append(Id)
        # Display the training image
        cv2.imshow("Training", faceNP)
        cv2.waitKey(1)
    # Return the IDs and face data
    return ids, faces

# Get IDs and face data from images
IDs, facedata = getImageID(path)

# Train the recognizer with the face data and corresponding IDs
recognizer.train(facedata, np.array(IDs))

# Save the trained recognizer to a file
recognizer.write("Trainer.yml")

# Close OpenCV windows
cv2.destroyAllWindows()

# Print message indicating training completion
print("Training Completed............")
