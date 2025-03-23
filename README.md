# Actividad Grupal

Una aplicación web simple desarrollada con Flask, diseñada para simular una tienda online con productos ficticios. La aplicación permite a los usuarios ver productos y realizar compras de manera interactiva.

## Características

- *Visualización de Productos*: Los productos disponibles se muestran con su nombre y precio.
- *Compra de Productos*: Los usuarios pueden realizar una compra de un producto específico.
- *Mensajes de Confirmación*: Después de realizar una compra, el usuario ve un mensaje de confirmación con el producto comprado.
- *Interfaz Responsiva*: La página está diseñada para verse bien tanto en computadoras de escritorio como en dispositivos móviles.
- *Estilos Mejorados*: Se ha mejorado el diseño con un archivo CSS moderno para hacer la página más profesional.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener lo siguiente instalado en tu entorno:

- Python 3.x
- Flask

## Instalación

Sigue estos pasos para instalar y ejecutar la aplicación:

### 1. Clona o descarga el proyecto

Clona el repositorio o descarga el archivo del proyecto en tu máquina local:

bash
git clone https://github.com/tuusuario/tienda-online-flask.git



### 2. Crea un entorno virtual (opcional pero recomendado)

Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto. Si no tienes virtualenv instalado, puedes hacerlo con el siguiente comando:

bash
pip install virtualenv


Luego, crea y activa el entorno virtual:

#### En Windows:

bash
python -m venv .venv
.\.venv\Scripts\activate


#### En macOS/Linux:

bash
python3 -m venv .venv
source .venv/bin/activate


### 3. Instala las dependencias

Una vez que el entorno virtual esté activado, instala Flask utilizando pip:

bash
pip install flask


### 4. Ejecuta la aplicación

Para iniciar la aplicación, ejecuta el siguiente comando:

bash
python app.py


La aplicación debería estar disponible en http://127.0.0.1:5000 en tu navegador.

### 5. Accede a la aplicación

Abre tu navegador web y ve a http://127.0.0.1:5000 para ver la página. En la página de inicio, podrás ver los productos disponibles y realizar compras.