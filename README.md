Deflate.py : 
"deflate" an image by moving the edges in one pixel at a time, stopping each edge when there is a nonzero image gradient somewhere along its length 

Inflate.py :
"inflate" an region by expanding the edges out one pixel at a time, stopping each edge when there is a nonzero image gradient somewhere along its length 
- Requires starting dimensions (ex: "deflated" dimensions of the image) 

Below is an image demonstrating the deflate method, drawing a blue border along the "deflated" region. 
![Image with Border](w_border.jpg?raw=true "Image with Border")
