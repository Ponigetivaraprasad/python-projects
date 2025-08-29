#importing the required packages
import pyautogui
import cv2
import numpy as np
#specify the resolution
resolution = (1920,1080)
#specify the video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
#SPECIFY NAME OF OUTPUTFILE
filename = "Recording.avi"
#specify frames per second
fps = 60.0
#creating a video writer object
out = cv2.VideoWriter(filename, codec, fps, resolution)
#create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
#rESIZE THIS WINDOW
cv2.resizeWindow("Live", 480, 270)
while True:
    #take a screenshot
    img = pyautogui.screenshot()
    #convert the screenshot into a numpy array
    frame = np.array(img)
    #convert it from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #write the frame
    out.write(frame)
    #show the live recording screen
    cv2.imshow("Live", frame)
    #if user clicks q then quit
    if cv2.waitKey(1) == ord("q"):
        break
#release the video writer object
out.release()
#Destroy all windows
cv2.destroyAllWindows()
print("Recording Stopped")