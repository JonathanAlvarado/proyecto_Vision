import cv2.cv as cv
import sys
from math import sin, cos, sqrt, pi, degrees
from  numpy import median

def find_Lines(im):
    out = cv.CreateImage(cv.GetSize(im), 8, 1)
    tmp = cv.CreateImage(cv.GetSize(im), 8, 3)
    storage = cv.CreateMemStorage(0)
    cv.Canny(im, out, 50, 200, 3)
    cv.CvtColor(out, tmp, cv.CV_GRAY2BGR)
    return cv.HoughLines2(out, storage, cv.CV_HOUGH_STANDARD, 1, pi / 180, 100, 0, 0)

def snd((a,b)):
    return b

def avg_Angle(lines):
    angles = [(snd (a)) for a in lines[:10] ]
    return median(angles)
    
def draw_Lines(lines,img):
    for (rho, theta) in lines[:5]:
        a = cos(theta)
        b = sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (cv.Round(x0 + 1000*(-b)), cv.Round(y0 + 1000*(a)))
        pt2 = (cv.Round(x0 - 1000*(-b)), cv.Round(y0 - 1000*(a)))
        cv.Line(img, pt1, pt2, cv.RGB(255, 0, 0), 3, 8)

def rotate(im, angle):
    center = (im.width/2.0, im.height/2.0)
    mat = cv.CreateMat(2, 3, cv.CV_32FC1)
    cv.GetRotationMatrix2D(center, angle, 1.0,mat)
    out = cv.CreateImage( cv.GetSize(im), cv.IPL_DEPTH_8U, 1)
    cv.WarpAffine(im, out, mat, fillval=255)
    return out

def preprocessing(im):
    out = cv.CreateImage( cv.GetSize(im), cv.IPL_DEPTH_8U, 1)
    cv.CvtColor(im, out, cv.CV_BGR2GRAY)
    cv.AdaptiveThreshold(out, out, 255.0, cv.CV_THRESH_BINARY, cv.CV_ADAPTIVE_THRESH_MEAN_C,11)
    return out
'''
image =  sys.argv[1]
im = cv.LoadImage(image)
thresh = threshhold(im)

lines = find_Lines(thresh)
ang = degrees(avg_Angle(lines)) 
rotation= rotate(thresh, ang )
out = cv.CreateImage(cv.GetSize(rotation), 8, 3)
cv.CvtColor(rotation, out, cv.CV_GRAY2BGR)

cv.SaveImage("skew_fix.jpg",out)
'''
