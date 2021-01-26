import cv2
import Deflate

''' "inflate" a region by moving the edges of the bounding
box out one pixel at a time (used after deflate), stopping each edge when there
is a nonzero image gradient somewhere along its length'''

class Inflate :

    def __init__(self, file_path) :
        self.img = cv2.imread(file_path)
        self.img_canny = cv2.Canny(self.img, 100, 100)
        d = Deflate(file_path)
        self.top, self.bottom, self.left, self.right = d.deflate();

    def __init__(self, file_path, node_dim) :
        self.img = cv2.imread(file_path)
        self.img_canny = cv2.Canny(self.img, 100, 100)
        self.top, self.bottom, self.left, self.right = node_dim

    # Find top edge
    def find_top(self) :
        if self.top == 0: return self.top
        else: new_top = self.top - 1
        while new_top > 0 :
            # if row contains white pixel
            if 255 in self.img_canny[new_top, self.left : self.right] :
                return new_top
            else :
                new_top -= 1
        return new_top

    # Find bottom edge
    def find_bottom(self) :
        if self.bottom == self.img_canny.shape[0] - 1: return self.bottom
        else: new_bottom = self.bottom + 1
        while new_bottom < self.img_canny.shape[0] :
            if 255 in self.img_canny[new_bottom, self.left :self.right] :  # if row contains white pixel
                return new_bottom
            else :
                new_bottom += 1
        return new_bottom

    def find_left(self) :
        if self.left == 0: return self.left
        else: new_left = self.left - 1
        while new_left > 0 :
            if 255 in self.img_canny[self.top:self.bottom, new_left] :  # if column contains white pixel
                return new_left
            else :
                new_left -= 1
        return new_left

    def find_right(self) :
        if self.right == self.img_canny.shape[1] - 1: return self.right
        else: new_right = self.right + 1
        while new_right < self.img_canny.shape[1] - 1 :
            if 255 in self.img_canny[self.top:self.bottom, new_right] :  # if column contains white pixel
                return new_right
            else :
                new_right += 1
        return new_right

    # Inflate the region
    def inflate(self) :
        return [self.find_top(), self.find_bottom(), self.find_left(), self.find_right()]

    # Show image with inflated borders
    def show_inf(self, top, bottom, left, right) :
        cv2.rectangle(self.img, (left, top), (right, bottom), (255,0,0), 1)
        cv2.imshow("Image with Inflated Border", self.img)
        cv2.waitKey(0)

# i = Inflate("square_pink.jpg")
# i.show_inf(i.inflate()[0],i.inflate()[1],i.inflate()[2],i.inflate()[3])