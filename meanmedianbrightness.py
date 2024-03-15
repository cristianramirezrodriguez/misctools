#Code to find the mean and median brightness of an image

from PIL import Image
import numpy as np

def pix_rgb(img_path,x,y):
  im=Image.open(img_path).convert('RGB')
  r,g,b = im.getpixel((x,y))
  a=(r,g,b)
  return(a)

def pix_brightness(path,x,y):
  I=np.sum(np.asarray(pix_rgb(path,x,y)))/3
  return(I)

def brightnessarray(path):
  photo = Image.open(path)
  width = photo.size[0]
  height = photo.size[1]
  brightlist=[]
  for x in range(0, width):
    for y in range(0, height):
      bright=pix_brightness(path,x,y)
      brightlist.append(bright)
  return(np.array(brightlist))

def meanmedbright(path):
  state = brightnessarray(path)
  mean = np.mean(state)
  median = np.median(state)
  return([mean,median])
