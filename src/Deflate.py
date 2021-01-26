import cv2
''' "deflate" an image by moving the edges of the bounding
box in one pixel at a time, stopping each edge when there
is a nonzero image gradient somewhere along its length'''
class Deflate:

    def __init__(self, file_path) :
        self.img = cv2.imread(file_path)
        self.img_canny = cv2.Canny(self.img, 100, 100)

    # Find top edge
    def find_top(self):
        top = 0
        while top < self.img_canny.shape[0]-1:
            # if top row contains white pixel
            if 255 in self.img_canny[top, 0:self.img_canny.shape[1]-1]:
                return top
            else:
                top += 1
        return top

    # Find bottom edge
    def find_bottom(self) :
        bottom = self.img_canny.shape[0] - 1
        while bottom > 0 :
            # if bottom row contains white pixel
            if 255 in self.img_canny[bottom, 0 :self.img_canny.shape[1] - 1] :
                return bottom
            else :
                bottom -= 1
        return bottom

    # Find left edge
    def find_left(self) :
        left = 0
        while left < self.img_canny.shape[1]-1 :
            pixels = self.img_canny[:, left]
            # if left column contains white pixel
            if 255 in pixels :
                return left
            else :
                left += 1
        return left

    # Find right edge
    def find_right(self) :
        right = self.img_canny.shape[1]-1
        while right > 0:
            pixels = self.img_canny[:, right]
            # if right column contains white pixel
            if 255 in pixels :
                return right
            else :
                right -= 1
        return right

    # Deflate the region
    def deflate(self) :
        return [self.find_top(), self.find_bottom(), self.find_left(), self.find_right()]

    # Show image with deflated borders
    def show_def(self, top, bottom, left, right) :
        cv2.rectangle(self.img, (left, top), (right, bottom), (255,0,0), 1)
        cv2.imshow("Image with Deflated Border", self.img)
        cv2.waitKey(0)

d = Deflate("square_pink.jpg")
d.show_def(d.deflate()[0],d.deflate()[1],d.deflate()[2],d.deflate()[3])
