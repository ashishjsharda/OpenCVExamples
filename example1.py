import cv2

# Read an image
image = cv2.imread('R.jpeg')

# Check if image is loaded properly
if image is not None:
    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)

    # Save the image
    cv2.imwrite('R1.jpeg', image)  # Replace with your desired path

    # Close all OpenCV windows
    cv2.destroyAllWindows()
else:
    print("Error: Image not found")
