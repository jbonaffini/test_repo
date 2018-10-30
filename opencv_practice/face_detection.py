import cv2

# face detection uses a haarcascade that defines the features of
# a certain image, for example the front of a face
# There are other haarcascades for full bodies, eyes, glasses, etc.

face_cascade = cv2.CascadeClassifier(r"D:\dev\practice_workspace\opencv_practice\resources\haarcascade_frontalface_default.xml")

# read in image

# img_rgb = cv2.imread(r"D:\dev\practice_workspace\opencv_practice\resources\photo.jpg")
img_rgb = cv2.imread(r"D:\dev\practice_workspace\opencv_practice\resources\news.jpg")
img_gry = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

# detect faces in the image
# scaleFactor tells the what to scale the window down by each iteration, in this case 5%
# minNeighbors      how many neighbors to search around the window
faces = face_cascade.detectMultiScale(img_gry,
scaleFactor=1.1,
minNeighbors=5)

# faces outputs a list
#       column for pixel start of face
#       row for pixel start of face
#       length and height of box that contains the face

print(faces)
print(type(faces))

# cv2 rectagle takes
#       the image
#       pixels of top left and bottom right
#       rectangle color
#       and rectagle width

for x, y, w, h in faces :
    img=cv2.rectangle(img_rgb, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow("Gray Photo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
