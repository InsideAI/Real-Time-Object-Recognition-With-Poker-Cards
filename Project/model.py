import cv2 as cv

capturer = cv.VideoCapture(1, cv.CAP_DSHOW)

pokerCardDetector = cv.CascadeClassifier('Data/classifier/cascade.xml')

while True:
    ret, frame = capturer.read()
    grayScaledFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grayScaledBlurredFrame = cv.GaussianBlur(grayScaledFrame, (3,3), 0)
    pokerCard = pokerCardDetector.detectMultiScale( grayScaledBlurredFrame,
                                                    scaleFactor = 3.5,
                                                    minNeighbors = 150,
                                                    minSize = (45,60) )
    for (x,y,w,h) in pokerCard:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        cv.putText(frame, 'Poker Card', (x,y-10), 2, 0.7, (0,255,0), 2, cv.LINE_AA)
    cv.imshow('Image', frame)
    key = cv.waitKey(1)
    if key == ord('e'):
        break

capturer.release()
cv.destroyAllWindows()