Proyecto Visión Computacional
===============
Proyecto: Detección de caracteres
Creado por: Jonathan Alvarado
Correo: jonathan.aam92@gmail.com
Blog: http://programacionits.blogspot.mx/
Fecha Última de Modificación: 23 de Mayo de 2013

Instalación
===========

No es necesario instalar el programa, basta con descargarlo
para poder ejecutarlo. Para ver los requerimientos necesarios
para ejecutarlo correctamente, ver el archivo "INSTALL".

Ejecución
=========

Para correr el ejemplo en Linux, basta con abrir una terminal,
posicionarse en el directorio donde se encuentra el programa ocr.py
y escribir el comando:

  	python ocr.py

Uso
===

En ejecución el programa pregunta por la opción de utilizar la cámara 
para obtener las imágenes o cargrarlas desde el archivo "imagenes" que se 
encuentra en el mismo directorio que el script.

Si se utiliza la opción de la cámara se mostrará una ventana con el stream 
de video de la cámara web, para tomar imágenes se debe presionar la tecla 
"enter". Una vez que se hayan tomado las imágenes deseadas hay que 
preseionar la tecla "esc" para pasar a la siguiente pantalla.

Después se mostrarán de una en una las imágenes tomadas para que se elija 
la zona de interés (texto) a digitalizar, esto se hace haciendo clic 
izquierdo con el mouse y arrastrando el cursor hasta elegir toda la zona 
de interés.

Después hay que esperar a que el programa solicite el nombre y autor 
del libro. Aquí algo muy imoportante, el programa tiene un bug y 
esto es que hay que escribir al inicio del archivo "temp.txt", 
"Capitulo 1" esto es porque para crear el archivo epub se debe 
tener un índice y el programa por default no lo hace.

Una vez hecho esto se escribe el título del libro y el autor y el 
programa procederá a convertir el archivo a epub.

En caso de haber escogido la opción 2, que es importar las imágenes 
desde el archivo "imagenes", solo basta con esperar a que el programa 
pregunte por el título y autor del libro y realizar lo mismo de 
escribir al inicio del archivo "temp.txt", "Capitulo 1" esto es 
porque para crear el archivo epub se debe tener un índice y el 
programa por default no lo hace.

Acerca de
=========

Este programa es un proyecto para la materia de Visión Computacional
de la carrera de Ingeniería en Tecnología de Software en la Facultad 
de Ingeniería Mecánica y Eléctrica, impartida por la Doctora Elisa
Schaeffer. 

Página Web del curso:
http://elisa.dyndns-web.com/~elisa/teaching/comp/vision/2013.html

Para más información sobre el funcionamiento del proyecto, visitar
el post en la siguiente liga:
http://programacionits.blogspot.mx/2013/05/proyecto-final.html
