# Actividad 2

## Hito II

En este repositorio hay un código escrito en Python llamado "loginautomatico.py". Este código automatiza 21 inicios de sesión en la página https://www.educarchile.cl/user/login. Esto se hace usando el ChromeDriver para Windows y Selenium.

## Hito III

### Primeros códigos

En este repositorio se tienen ocho archivos escritos en Python. Cada uno de estos códigos automatiza una acción en una página específica. Para lograr la automatización se usa el software Selenium y los códigos se ejecutan en Windows 10.

Cuatro de estos archivos (los que tienen en su nombre 'cl3') están relacionados a una página web chilena (https://chilesuplementos.cl/) y los otros cuatro archivos (los que tienen 'fuente' en su nombre) se relacionan a una página web española (https://lafuente.es/).

Las acciones que se automatizan son las siguientes:

- La primera acción que se automatiza es el registro de un nuevo usuario. Los archivos son "signincl3.py" y "registerfuente.py".

- La segunda acción que se automatiza es el inicio de sesión de usuario. Los archivos son "logincl3.py" y "loginfuente.py".

- La tercera acción que se automatiza es la modificación de la contraseña luego de haber ingresado en la cuenta de usuario. Los archivos son "modipasscl3.py" y "modipassfuente.py".

- La cuarta, y última, acción que se automatiza es la modificación de la contraseña sin haber iniciado la sesión. Los archivos son "resetpasscl3.py" y "resetpassfunte.py".

### Códigos optimizados

En este repositorio se tienen dos carpetas con códigos en Python en su interior. Cada uno de estos códigos es una optimización de los códigos antes subidos.

En la carpeta "Código para secuencia completa" se encuentran dos códigos escritos en Python. Cada código automatiza cuatro acciones, una después de la otra, en los sitios elegidos, un código para el sitio chileno (todoCL.py) y otro para el sitio español (todoES.py). Las tareas que automatizan son: registrar un usuario en la página, iniciar sesión en la página con una cuenta ya existente, modificar la contraseña de esa cuenta ya existente habiendo iniciado sesión previamente y restablecer la contraseña para esa misma (u otra) cuenta ya existente (que no requiere inicio de sesión).

La carpeta "Automatizaciones optimizadas" contiene dos subcarpetas: "Sitio chileno" y "Sitio español". Cada subcarpeta tiene por separado las cuatro automatizaciones requeridas. La diferencia entre estas automatizaciones y las que se subieron anteriormente es que en estas se minimiza el uso de la función sleep y se usa Wait Until que disminuye al mínimo el tiempo total de la automatización, evitando así una espera excesiva o un error de ejecución por la lenta carga de la página. 
