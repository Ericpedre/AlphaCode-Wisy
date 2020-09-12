# AlphaCode-Wisy 🚀

Código que dado un archivo de entrada “people.in” con Datos públicos de LinkedIn, encuentra a las 100 personas con mayor probabilidad de convertirse en clientes de una empresa x, mediante el envío de una campaña de marketing por correo electrónico, los IDs de los usuarios se guardan en “people.out”.

# ¿Cómo funciona?

El algoritmo principal “AlphaCode.py” fue previamente “entrenado” con el algoritmo “AlphaTraining.py” que busca palabras asociadas entre sí y las guarda en el archivo “Learn.txt”
Posteriormente el archivo es utilizado por el algoritmo principal para asociar la “la palabra que describe  el tipo de persona a la que va dirigido el marketing” (Ingresada por el usuario) con una categoría y luego las palabras en esa categoría con clientes cuyo “CurrenRole” o “Industry” coincida, finalmente ordena los resultados poniendo a las personas con mayor número de conexiones ya que esas personas podrían ser más activas, escoje las 100 primeras y las graba en el archivo “people.out”



### Pre-requisitos 📋

_Tener pyton3.x instalado_

_Sistema operativo Windows_

### Instalación 🔧

_Para instalarlo solo tienes que clonar el repositorio_

_Clonar repositorio:_

```
git clone https://github.com/Ericpedre/AlphaCode-Wisy.git
```
```
cd AlphaCode-Wisy
```

_Para ejecutarlo abre el archivo AlphaCode.py_

## Ejecutando el algoritmo principal ⚙️

_Para ejecutarlo escribe el sigiente comando el la carpeta del proyecto:_

```
python AlphaCode.py
```
o

```
python3 AlphaCode.py
```

_para ejecutar el modo "entrenador":_
```
python AlphaTraining.py 
```
o 

```
python3 AlphaTraining.py
```

⌨️ Por [EricPedreschi](https://github.com/EricPedre)
