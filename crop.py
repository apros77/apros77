import cv2
 
def drawCircle(event, x, y, flags, param):
 
    if event == cv2.EVENT_MOUSEMOVE:
        print('({}, {})'.format(x, y))
 
        imgCopy = img.copy()
        cv2.circle(imgCopy, (x, y), 10, (255, 0, 0), -1)
 
        cv2.imshow('image', imgCopy)
 
 
img = cv2.imread('C:/Users/N/Desktop/test.png')
cv2.imshow('image', img)
 
cv2.setMouseCallback('image', drawCircle)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
