import cv2.cv as cv
import os
import glob
from pytesser import *
import Image
import epubCreator
import ez_epub
import ocrprep
from math import degrees

drawingBox = False
extension = '.png'
crop = 0
box = [0,0,0,0]
cropedFolder = 'croped'
scanFolder = 'imagenes'

def camera_Capture(cam):
    global extension
    folder = 'captures/'
    os.system('rm -r '+folder)
    os.system('mkdir '+folder)
    name = 'out'
    n = 0
    cv.NamedWindow("Camera", cv.CV_WINDOW_AUTOSIZE)
    while True:
        try:
            frame = cv.QueryFrame(cam)
            cv.ShowImage("Camera", frame)
            key = cv.WaitKey(10)
            if key == 13:
                image = name+str(n)+extension
                cv.SaveImage(folder+image, frame)
                print 'Se guardo imagen: ',image
                n += 1
            if key == 27:
                cv.DestroyWindow('Camera')
                break
        except:
            print "Hubo un problema con la camara"
            break

def open_Images(path = 'captures', extension = 'png'):
    pictures = []
    pics = glob.glob(os.path.join(path, '*.'+extension))
    for pic in pics:
        pictures.append(pic)
    return pictures
                         
def crop_Images(images):
    global drawingBox
    folder = 'croped/'
    os.system('rm -r '+folder)
    os.system('mkdir '+folder)
    cv.NamedWindow('Crop')
    for im in images:
        print im
        try:
            image = cv.LoadImage(im)
            temp = cv.CloneImage(image)
            cv.SetMouseCallback('Crop', mouse_Callback, image)
            while True:
                cv.Copy(image,temp)
                if drawingBox:
                    draw_box(temp)
                cv.ShowImage('Crop', temp)
                key = cv.WaitKey(10)
                if key == 13:
                    break
        except:
            print 'Ocurrio un error'
        cv.DestroyWindow('Crop')

def mouse_Callback(event, x,y, flags, im):
    global drawingBox, extension, crop, box, cropedFolder
    name = 'crop'
    if event==cv.CV_EVENT_MOUSEMOVE:
        if (drawingBox == True):
            box[2] = x - box[0]
            box[3] = y - box[1]
    elif event == cv.CV_EVENT_LBUTTONDOWN:
        drawingBox = True
        [box[0], box[1], box[2], box[3]] = [x, y, 0, 0]
    elif event == cv.CV_EVENT_LBUTTONUP:
        drawingBox = False
        if box[2] < 0:
            box[0] += box[2]
            box[2] *= -1
        if box[3] < 0:
            box[1] += box[3]
            box[3] *= -1
        rect = (box[0], box[1], box[2], box[3])
        roi = cv.GetSubRect(im, rect)
        image = name+str(crop)+extension
        crop += 1
        cv.SaveImage(cropedFolder+'/'+image,roi)

def draw_box(im):
    cv.Rectangle(im,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),cv.RGB(0,255,0))

def grab_Text(tmpFile, folder = 'tmp', camera = True):
    global extension
    name = 'tmp'
    os.system('mkdir '+folder)
    if camera:
        images = open_Images(path = cropedFolder, extension = 'png')
    else:
        images = open_Images(path = scanFolder, extension = 'jpg')
    n = 0
    images.sort()
    text = ''
    for im in images:
        image = cv.LoadImage(im)
        out = preprocessing(image)
        tmp = folder+'/'+name+str(n)+extension
        cv.SaveImage(tmp, out)
        image = Image.open(tmp)
        text += image_to_string(image)
        n += 1
    os.system('rm -r '+folder)
    create_Txt(text,tmpFile)

def preprocessing(im):
    gray = cv.CreateImage((im.width, im.height), 8, 1)
    out = cv.CreateImage((im.width,im.height),cv.IPL_DEPTH_8U,1)
    cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
    cv.Threshold(gray,out,110,255,cv.CV_THRESH_BINARY_INV)
    return gray
    '''
    thresh = ocrprep.preprocessing(im)
    lines = ocrprep.find_Lines(thresh)
    ang = degrees(ocrprep.avg_Angle(lines)) 
    rotation= ocrprep.rotate(thresh, ang )
    out = cv.CreateImage(cv.GetSize(rotation), 8, 3)
    cv.CvtColor(rotation, out, cv.CV_GRAY2BGR)
    return out
    '''

def create_Txt(text, tmpFile):
    text = text.decode('utf-8')
    txtFile = open(tmpFile, 'a')
    txtFile.write(text.encode('ASCII', 'ignore'))
    txtFile.close()

def create_epub():
    title = raw_input('Titulo del libro: ')
    author = raw_input('Autor del libro: ')
    book = ez_epub.Book()
    book.title = title
    book.authors = [author]
    book.sections = epubCreator.parseBook(r'temp.txt', 1, 100)
    book.make(r'%s' % book.title) 
    

if __name__ == '__main__':
    txtFile = 'temp.txt'
    option = int(raw_input('Elige una opcion (1 o 2):\n\t1. Tomar image desde camara\n\t2. Importar imagen\n'))
    cv.NamedWindow('ocr',1)
    os.system('rm '+txtFile)
    if option == 1:
        try:
            cam = cv.CreateCameraCapture(-1)
            camera_Capture(cam)
            images = open_Images()
            crop_Images(images)
            text = grab_Text(txtFile)
            create_epub()
        except:
            print 'No se detecto camara web'
    if option == 2:
        try:
            ext = raw_input('Que extension son las imagenes? ')
        #images = open_Images(path=folder, extension = '*.'+ext)
        #crop_Images(images)
            grab_Text(txtFile, camera = False)
        #create_Txt(text)
            create_epub()
        except:
            print 'Hay un problema con las imagenes'
