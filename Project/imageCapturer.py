import cv2 as cv
import imutils
import os

capturer = cv.VideoCapture(1, cv.CAP_DSHOW)

x1 = 190
y1 = 80
x2 = 450
y2 = 400

destinationFolder = 'Data/n'

if not os.path.exists(destinationFolder):
    os.makedirs(destinationFolder)
    print(f'{destinationFolder} was created!')

count = len(os.listdir(destinationFolder))

while True:
    ret, frame = capturer.read()
    if ret == False:
        break
    auxFrame = frame.copy()
    cv.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), thickness=2)
    captured = auxFrame[y1:y2,x1:x2] 
    captured = imutils.resize(captured, width=40)
    key = cv.waitKey(2)
    if key == ord('e'):
        break
    elif key == ord('c'):
        cv.imwrite(f'{destinationFolder}/{count}.jpg', captured)
        print(f'Image {count}.jpg was saved!')
        count += 1
    cv.imshow('Frame', frame)

captured.release()
cv.destroyAllWindows()