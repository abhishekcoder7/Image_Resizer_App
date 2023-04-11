import cv2


scale = int(input("Enter Scaling percentage : "))

img = cv2.imread('source_img.jpg', cv2.IMREAD_UNCHANGED)

new_height = int(img.shape[0] * scale / 100)
new_width = int(img.shape[1] * scale / 100)

output_img = cv2.resize(img, (new_width, new_height))

cv2.imwrite('output.jpg', output_img)
