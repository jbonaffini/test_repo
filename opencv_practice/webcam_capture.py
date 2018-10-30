import cv2, time

# use this to grab the feed from the webcam (index=0) or from a movie file
video=cv2.VideoCapture(0)
a=0
t=time.time()
while True:
    a=a+1
    check, frame= video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break


# release the camera
print("Time elapsed:", time.time()-t,"   FPS:", a/(time.time()-t))
video.release()
cv2.destroyAllWindows()
