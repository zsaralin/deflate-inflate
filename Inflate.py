import cv2

''' "inflate" a region by moving the edges out one pixel at a time, stopping each edge when there
is a nonzero image gradient somewhere along its length'''

# Find top edge
def find_top(img_canny, node_dim) :
    if node_dim[0] == 0 :
        return node_dim[0]
    else :
        new_top = node_dim[0] - 1
    while new_top > 0 :
        # if row contains white pixel
        if 255 in img_canny[new_top, node_dim[2] : node_dim[3]] :
            return new_top
        else :
            new_top -= 1
    return new_top


# Find bottom edge
def find_bottom(img_canny, node_dim) :
    if node_dim[1] == img_canny.shape[0] - 1 :
        return node_dim[1]
    else :
        new_bottom = node_dim[1] + 1
    while new_bottom < img_canny.shape[0] :
        if 255 in img_canny[new_bottom, node_dim[2] : node_dim[3]] :
            return new_bottom
        else :
            new_bottom += 1
    return new_bottom


def find_left(img_canny, node_dim) :
    if node_dim[2] == 0 :
        return node_dim[2]
    else :
        new_left = node_dim[2] - 1
    while new_left > 0 :
        if 255 in img_canny[node_dim[0] :node_dim[1], new_left] :  # if column contains white pixel
            return new_left
        else :
            new_left -= 1
    return new_left


def find_right(img_canny, node_dim) :
    if node_dim[3] == img_canny.shape[1] - 1 :
        return node_dim[3]
    else :
        new_right = node_dim[3] + 1
    while new_right < img_canny.shape[1] - 1 :
        if 255 in img_canny[node_dim[0] :node_dim[1], new_right] :  # if column contains white pixel
            return new_right
        else :
            new_right += 1
    return new_right


# Inflate the region
def inflate(file_path, node_dim) :
    img = cv2.imread(file_path)
    img_canny = cv2.Canny(img, 100, 100)
    return [find_top(img_canny, node_dim), find_bottom(img_canny, node_dim),
            find_left(img_canny, node_dim), find_right(img_canny, node_dim)]

