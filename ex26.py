import cv2
import numpy as np

# Load the original image and watermark
image = cv2.imread('nive.jpg')
watermark = "nive"

# Extract the alpha channel from the watermark
alpha_channel = watermark[:, :, 3]

# Resize the watermark to match the size of the original image
watermark = cv2.resize(watermark, (image.shape[1], image.shape[0]))

# Create a mask from the alpha channel
mask = watermark[:, :, 3] / 255.0

# Convert the mask to 3 channels
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

# Multiply the watermark and mask to get the alpha-blended watermark
watermarked = (1 - mask) * image + mask * watermark[:, :, :3]

# Convert the result to uint8 type
watermarked = watermarked.astype(np.uint8)

# Display the watermarked image
cv2.imshow('Watermarked Image', watermarked)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
