import cv2

# Asignacion del documento Xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Imagen a trabajar
image = cv2.imread('G:\Documentos\Programacion\python\AI\Ejemplo_OpenCV\Resources\yo1.jpg')

# Conversion de color a gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Deteccion de rostros
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Asignacion de rectangulos por rostro detectado
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Muestra de imagen
cv2.imshow('Image', image)

cv2.waitKey()
