# 1. Resizing to 224, 224, 3

import cv2

# Assuming 'image' is your original image
resized_image = cv2.resize(image, (224, 224))

# 2. Grayscale Conversion

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Cropping to Extract Only Dog

# Assuming x, y, w, h, are the coordinatesog the dog bounding box
cropped image = image[y:y + h, x:x + h]

# 4. Rotation by 45 degrees

rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# 5. Flip Left to Right

flipped_image = cv2.flip(image, 1)

# 6. Gaussian & Median Blurring

# Gaussian Blurring
gaussian_blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Median Blurring
median_blurred_image = cv2.medianBlur(image, 5)

# 7. Edge Detection Techniques

# Canny Edge Detection
edges = cv2.Canny(image, 100, 200)

# Other edge detection techniques like Sobel, Laplacian, etc. can also be used

# 8. Background Subtraction

# Assuming 'background' is the background image
foreground_mask = cv2.absdiff(background, image)