import cv2
import argparse
import numpy as np
import time

start_time = time.time()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True,
                help = "Chemin vers le tableau")
ap.add_argument("-v", "--video", required = True,
                help = "Chemin vers le fichier video")
ap.add_argument("-o", "--output", required = True)
args = ap.parse_args()
video = args.video
input = args.input
output = args.output
R = 0.7


r = np.load(input)
cap = cv2.VideoCapture(video)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter(output,
        cv2.VideoWriter_fourcc('M','J','P','G'),
        10, (frame_width,frame_height))

# Check if camera opened successfully
j=0
if (cap.isOpened()== False):
  print("Error opening video stream or file")

ret0, oldframe = cap.read()
#Pour garde l'ordre du lecteur

while(cap.isOpened() and ret0):
    ret, frame = cap.read()
    if ret == True:

        if ~np.isnan(r[j]) and r[j]>R :
            cv2.imshow('Frame',frame)
            out.write(frame)
            print j, r[j],
            interval = time.time() - start_time
            FPS = j/interval #Attention division d'entier
            print "FPS", FPS
        j+=1
    # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

  # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()
