import cv2

# 1. Load an image from file
# Replace 'image.jpg' with the path to your actual image
image = cv2.imread(r"C:\Users\kazim\Downloads\BTECH DEGREE_page-0001.jpg")

# 2. Display the image in a window
cv2.imshow('Original Image', image)

# 3. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

# 4. Save the grayscale image to a new file
cv2.imwrite('grayscale_output.jpg', gray_image)

# 5. Wait for any key press to close the windows
# Passing 0 means it waits indefinitely until a key is pressed  
cv2.waitKey(0)

# 6. De-allocate all window memory
cv2.destroyAllWindows()