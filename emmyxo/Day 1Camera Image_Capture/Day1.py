import cv2
import matplotlib.pyplot as plt
import os

def get_highest_image_number():
    image_numbers = []
    for filename in os.listdir("."):
        if filename.startswith("image") and filename.endswith(".jpg"):
            try:
                number = int(filename[5:-4])  # Extract the number from the filename
                image_numbers.append(number)
            except ValueError:
                pass

    if image_numbers:
        return max(image_numbers)
    else:
        return 0

def capture_and_save_image():
    highest_number = get_highest_image_number()
    new_image_number = highest_number + 1

    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    # Convert the BGR frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Save the RGB frame as an image with the new incremented number
    plt.imsave(f"image{new_image_number}.jpg", frame_rgb)

    cam.release()

# Usage: Call the function to capture and save a new image with the next number
capture_and_save_image()
