import cv2
import os
import time

def create_img_folder():
    folder_name = "img"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def capture_images(interval=10):
    folder = create_img_folder()
    cap = cv2.VideoCapture(0)  # Open the webcam
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    img_count = 0
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                break
            
            img_name = os.path.join(folder, f"image_{img_count}.jpg")
            cv2.imwrite(img_name, frame)
            print(f"Saved: {img_name}")
            
            img_count += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopping image capture...")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()