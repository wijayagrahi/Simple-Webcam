import cv2

# Use the Webcam
cap = cv2.VideoCapture(0)

# Define the width. 3 means ID
cap.set(3, 640)

# Define the height
cap.set(4, 480)

# Change the brightness
cap.set(10, 100)

image_no = 1

while True:
    success, img = cap.read()
    cv2.imshow('Coconut', img)

    # Save the images and renamed as 'Hii_1', 'Hii_2'
    if cv2.waitKey(1) & 0XFF == ord('c'):
        print("C was pressed")
        cv2.imwrite(f'Hii_{image_no}.jpg', img)
        image_no +=1
        cv2.waitKey(2000)

    # Add a delay and if we press q the loop break and video is stopped
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

