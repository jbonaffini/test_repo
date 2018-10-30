import cv2,time, pandas
from datetime import datetime

def get_background_photo():
    video=cv2.VideoCapture(0)
    check, frame= video.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"app6_WebcamDetector\resources\Background2.png",frame)
    video.release()



# use this to grab the feed from the webcam (index=0) or from a movie file
video=cv2.VideoCapture(0)

first_frame=None

# grayscale background
# img_b=cv2.imread(r"app6_WebcamDetector\resources\Background2.png",-1)
a=0
t=time.time()
status_list=[None, None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

while True:
    a=a+1
    check, frame= video.read()
    status_list[-1]=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame, gray)
    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta, None, iterations=2)

    (_,cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status_list[-1]=1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)


    if status_list[-1]==1 and status_list[-2]==0 :
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1 :
        times.append(datetime.now())

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_delta)
    cv2.imshow("Countour Frame", frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        if status_list[-1]==1 :
            times.append(datetime.now())
        break


    status_list[-2]=status_list[-1]



# release the camera
print("Time elapsed:", time.time()-t,"   FPS:", a/(time.time()-t))
[print(x) for x in times]
for i in range(0,len(times),2) :
    df=df.append({"Start": times[i], "End":times[i+1]}, ignore_index=True)
print(df)
df.to_csv(r"app6_WebcamDetector\resources\Times.csv")
video.release()
cv2.destroyAllWindows()
