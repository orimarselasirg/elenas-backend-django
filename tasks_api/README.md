
# API creada con Django Rest Framework para challenge
<br/>
<br/>
<img src ='https://www.elenas.co/co/wp-content/uploads/2022/09/elenas.png'/>
<br/>
<br/>
<p align="justify"> Elenas Task Manager, es un proyecto individual desarrollado para una prueba tecnica de la empresa Elenas, los principales requerimiento estan basado en el proceso de login de un usuario el cual puede crear, editar, modificar y eliminar solo las taras relacionadas a su perfil, el diseño esta basado en algo simple, gestionando la tareas como una tarjetas independientes para comodida y mejor gestion del usuario.</p> 

<br/>
<br/>
<h1>Primeros pasos</h1>

por favor sigue las siguientes instrucciones para poder levantar los servicios del backend de manera correcta en un entorno local

**📑  Requerimientos**

Para poder poner a correr esta aplicación tendrás que tener instalado en tu ordenador con anterioridad la última versión de Python y Pip, puedes chequear en consola si la tienes instalada haciendo “python --version” y “pip --version”

Sino en el siguiente link puedes descargarla gratuitamente - 

🌐  [Python](https://www.python.org/)

Copia el repositorio haciendo click en Fork, así obtendrás una copia del mismo en tu Github.

<br>
<br>
<h1>Para instalar 🛠 </h1>

Llegó el momento para ejecutar en tu equipo el proyecto.

Abre la terminal desde tu editor de codigo o desde un consola aparte dentro de la carpeta api_task y ejecuta los siguientes comandos.
```sh
   pip install
```

Con este comando descargar e instalara todas las dependencias que se utiliza en el proyecto de forma automática. El tiempo de este proceso depende de tu conexión a internet y del poder del procesamiento de tu equipo, ten paciencia, puede tardar unos minutos.

<br>


<h3>Creación de base de datos PostgreSQL</h3>
En caso de aun no contar con una base de datos, sigue los siguientes pasos para crear una:

- Descargar la ultima versión estable de Postgres de su web oficial [Postgres](https://www.postgresql.org/download/)

- Ejecutamos el instalador, este incluye las herramientas de lineas de comando, la interfaz visual pgAdmin y el servidor de Postgres

- Asignar la contraseña para el superusuario de la base de datos de PostgreSQL

- En la próxima ventana dejaremos el puerto por defecto para PostgreSQL: 5432

- Una vez completa la instalación podemos seleccionar ingresar a través de la interfaz grafica o de la consola SQL Shell

- En SQL Shell completamos los requerimientos, por defecto podemos dar 'enter' en todos los campos MENOS en la contraseña, donde colocaremos la indicada previamente en el instalador 

- En este momento ya estamos conectados al servidor de Postgres. se debe crear una base de datos la cual debe llamarse elenas, se crea con el siguiente comando:
```
   CREATE DATABASE elenas;
``` 
- Veremos un mensaje de confirmación de que la base ha sido creada con éxito. A continuación podemos desplegar un listado de las bases de datos ejecutando el comando: 
```
   \l 
```
<br/>
<br/>
<h2>Ejecución  del proyecto 💻</h2>

Para realizar el despliegue local solo necesitas abrir una terminal en la raiz de la carpeta donde guardaste el repositorio en tu computador y ejecutar el comando.

```sh
  virtualenv 'nombredetuentornovirtual'
  por ejemplo "virtualenv venv"
```
porsteriormente en la misma carpeta raiz ejecutas el siguiente comando


si estas en windows
```sh
   ./venv/Scripts/activate
```

si estas en Mac
```sh
   source venv/bin/activate
```
Este comando genera el entorno virtual requerido para instalar las dependencias


Posterior, se debe ejecutar el sigueinte comando dentro de la carpeta task_api que se encuentra en la carpeta principal

```sh
  python manage.py runserver
```


Este comando levantara el servidor y la conexion a la base de datos. Ya estás listo para hacer peticiones!
<br/>
<br/>
<h1>Documentación API</h1>
En el siguiente link vas a tener acceso a la documentación de nuestra API
<br/>
<br/>
📄 [Documentación](https://documenter.getpostman.com/view/20686333/2s8YmPth7c#2f1f3d41-4d84-423d-82dd-9dfb960be23c)
<br/>
<br/>
Cualquier duda, por favor no dudes en comunicarte conmigo. Saludos

