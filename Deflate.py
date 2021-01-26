import cv2

''' "deflate" an image by moving the edges in one pixel at a time, stopping each edge when there
is a nonzero image gradient somewhere along its length'''

# Find top edge
def find_top(img_canny) :
    top = 0
    while top < img_canny.shape[0] - 1 :
        # if top row contains white pixel
        if 255 in img_canny[top, 0 :img_canny.shape[1] - 1] :
            return top
        else :
            top += 1
    return top

# Find bottom edge
def find_bottom(img_canny) :
    bottom = img_canny.shape[0] - 1
    while bottom > 0 :
        # if bottom row contains white pixel
        if 255 in img_canny[bottom, 0 :img_canny.shape[1] - 1] :
            return bottom
        else :
            bottom -= 1
    return bottom

# Find left edge
def find_left(img_canny) :
    left = 0
    while left < img_canny.shape[1] - 1 :
        pixels = img_canny[:, left]
        # if left column contains white pixel
        if 255 in pixels :
            return left
        else :
            left += 1
    return left

# Find right edge
def find_right(img_canny) :
    right = img_canny.shape[1] - 1
    while right > 0 :
        pixels = img_canny[:, right]
        # if right column contains white pixel
        if 255 in pixels :
            return right
        else :
            right -= 1
    return right

# Deflate the region
def deflate(filepath) :
    img = cv2.imread(filepath)
    img_canny = cv2.Canny(img, 100, 100)
    return [find_top(img_canny), find_bottom(img_canny),
            find_left(img_canny), find_right(img_canny)]



