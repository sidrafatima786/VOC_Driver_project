import cv2
print("Starting camera test...")
cap = cv2.VideoCapture(0)
print(f"Camera opened: {cap.isOpened()}")

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

print("Reading frame...")
ret, frame = cap.read()
print(f"Frame read success: {ret}")

if ret:
    print("Displaying frame...")
    cv2.imshow('Camera Test', frame)
    print("Press any key to exit")
    cv2.waitKey(0)

print("Cleaning up...")
cap.release()
cv2.destroyAllWindows()
print("Test complete")
