import cv2
import numpy as np

# The number of pixels that are black
beam_width = 1

# The maximum number of padding pixels
max_padding = 3

# The number of lines of the same interval that are being drawn.
repeats = 5

# We are generating a square pattern, this is the length of a side:
side_length = 0

for padding in range(max_padding, 0, -1):
    print("padding: ", padding)
    for repeat in range(repeats):
        side_length += (beam_width + padding)
        print("side_length: ", side_length)
side_length = side_length * 2 + 1
print("side_length: ", side_length)

image = np.ones((side_length, side_length), dtype=np.uint8)

print("xxxxxxxxxxxxxx")
index = 0
for padding in range(max_padding, 0, -1):
    print("padding: ", padding)
    for repeat in range(repeats):
        image[index, :] = 0
        image[:, index] = 0
        index += beam_width + padding
        print("index: ", index)

for padding in range(1, max_padding + 1):
    print("padding: ", padding)
    for repeat in range(repeats):
        image[index, :] = 0
        image[:, index] = 0
        index += beam_width + padding
        print("index: ", index)

image[side_length - 1, :] = 0
image[:, side_length - 1] = 0
image *= 255

cv2.imwrite(f"beam_width_{beam_width}.png", image)