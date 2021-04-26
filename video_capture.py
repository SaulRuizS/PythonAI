import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

##greenlight_classifier = cv2.CascadeClassifier('C:\\Users\\sfrs_\\OneDrive\\Escritorio\\cascade_files_green\\classifier\\cascade.xml')

while True:
    ret,frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
	    break

cap.release()
cv2.destroyAllWindows()