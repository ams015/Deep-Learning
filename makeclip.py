import argparse
import numpy as np
import cv2
import os



#input
#python getHumanCentroids.py --input  ./clip/clip.mp4  --clipimages  ./clipimages/


# ------------construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input clip")
ap.add_argument("-a", "--clipimages", required=True,
             help="path to  image directory")

#ap.add_argument("-t", "--template", required=True,
   #          help="path to template")
args = vars(ap.parse_args())




#------------------create video file
vidcap = cv2.VideoCapture((args["input"]))
success,image = vidcap.read()
count = 0
success = True
#rint type
while success:

  image= image[75:350, 24:610, :]
  if count<10:
  #  print args["clipimages"]+"/frame00%d.jpg" % count
    cv2.imwrite(args["clipimages"]+"/frame00%d.jpg" % count, image)     # save frame as JPEG file
  elif count <100:

    cv2.imwrite(args["clipimages"]+"/frame0%d.jpg" % count, image)     # save frame as JPEG file
  else:
    cv2.imwrite(args["clipimages"]+"/frame%d.jpg" % count, image)  # save frame as JPEG file
  success,image = vidcap.read()
  #print 'Read a new frame: ', success
  count += 1


