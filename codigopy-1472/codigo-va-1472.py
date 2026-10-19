# jose solis nc 1472
# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-1472",
    "deshumificador.jpg"
)

imagen = cv2.imread(ruta_imagen)

# Imagen
# Vamos a crear nuestra matriz principal
deshumificador = cv2.imread(ruta_imagen)
# print(deshumificador) muestra las matrices de la imagen
# convertir de BGR a RGB color rojo COLOR_BGR2RGB
deshumi = cv2.cvtColor(deshumificador, cv2.COLOR_BGR2RGB)
# cv2.imshow("deshumificador original 1472", deshumificador)
cv2.imshow("deshumificador color 1472", deshumi)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas las ventanas de memoria
