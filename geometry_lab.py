from mat import Mat
from matutil import *
from image_mat_util import *
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels,labels),{ (label,label):1 for label in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    id = identity()
    id[('x','u')]=x;
    id[('y','u')]=y;
    return id;

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    id = identity()
    id[('x','x')]=a
    id[('y','y')]=b
    return id

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    id = identity()
    id[('x','x')]=math.cos(angle)
    id[('x','y')]=-math.sin(angle)
    id[('y','x')]=math.sin(angle)
    id[('y','y')]=math.cos(angle)
    return id

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''

    return translation(x,y)*rotation(angle)*translation(-x,-y)
## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    return scale(-1,1)

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    return scale(1,-1)
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    id = identity({'r','g','b'})
    id[('r','r')]=scale_r
    id[('g','g')]=scale_g
    id[('b','b')]=scale_b
    return id

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    id = identity({'r','g','b'})
    transdict = { 'r':77.0/256.0 ,'g':151.0/256.0,'b':28.0/256.0}
    for k1 in transdict:
        for k2 in transdict:
            id[(k1,k2)]=transdict[k2]
    return id


## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass




