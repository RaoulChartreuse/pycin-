import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import time

start_time = time.time()

# l'argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True,
                help = "Chemin vers le fichier video")
ap.add_argument("-o", "--output", required = True,
                help = "Fichier de sortie en .npy")
ap.add_argument("--verbosity",
                action="store_true",
                help = "increase output verbosity")
ap.add_argument("-d", "--display", help = "Sortie video",
                action="store_true")
args = ap.parse_args()
input = args.input
output = args.output
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Tester la persence des fichiers !!!!

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
#cap = cv2.VideoCapture('geant.avi')
cap = cv2.VideoCapture(input)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")




# Read until video is completed
ret0, oldframe = cap.read()
skip=0

j=0
p_x=[]
p_y=[]
fig, ax = plt.subplots()


while(cap.isOpened() and ret0):
  # Capture frame-by-frame
  ret, frame = cap.read()

  for i in range(skip):
    ret_1, f1 =cap.read()
    if not ret_1:
      break


  if ret == True:

    #on fait la somme des canneaux de couleur
    r=np.corrcoef( np.add.reduce(frame,0).flatten(),
                   np.add.reduce(oldframe,0).flatten())[0,1]
    r=1-r
    #print  r, cv2.norm(np.add.reduce(frame,0).flatten(),
    #            np.add.reduce(oldframe,0).flatten())

    p_x.append(j)
    p_y.append(r)
    j+=1

    #print  np.array(frame).flatten(), np.array(oldframe).flatten()
    #print np.shape(frame),  np.shape(np.add.reduce(frame,2) )



    oldframe=frame

    if r>.2 and args.display:


      # Display the resulting frame
      cv2.imshow('Frame',frame)
      print r
      ax.cla()
      ax.plot(p_x, p_y, label='Correlation')
      plt.pause(0.1)
      plt.show()

    #FPS count
    if args.verbosity :
        interval = time.time() - start_time
        FPS = j/interval #Attention division d'entier
        print "FPS", FPS

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break



  # Break the loop
  else:
    break

interval = time.time() - start_time
print j," images en ", interval, "s : ",  j/interval



# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

#sauvegarde du tableau

filename = output
np.save(filename, p_y)
