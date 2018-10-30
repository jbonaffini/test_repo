import cv2
import glob2

def practice_one():
    # read in image
    # read as grayscale (argument 0) or RGB (argument -1)
    img=cv2.imread(r"opencv_practice\resources\galaxy.jpg",0)

    print(type(img))
    print(img)
    print(img.shape)    # number of points in each dimension
    print(img.ndim)     # number of dimensions

    cv2.imshow("Galaxy", img)   # display the image
    cv2.waitKey(0)          # how long to display the image (0 implies the user presses a button)
    cv2.destroyAllWindows()             # destroy the window

    resized_image=cv2.resize(img,(1000,500))
    cv2.imshow("Galaxy Resized", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    cv2.imshow("Galaxy Resized 2", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(r"opencv_practice\resources\galaxy_resized.jpg",resized_image)


def practice_batchresize():
    filenames = glob2.glob(r"opencv_practice\resources\*.jpg")
    print(filenames)
    for file in filenames :
        img=cv2.imread(file,0)
        cv2.imshow("Resized", cv2.resize(img,(100,100)))
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

def get_background_photo():
    video=cv2.VideoCapture(0)
    check, frame= video.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"app6_WebcamDetector\resources\Background2.png",frame)
    video.release()


# practice_batchresize()
get_background_photo()
