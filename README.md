# StarWarProyect
 proyecto hecho en base a starwars
Manual de Usuario de StarWarProyect
Introducción
StarWarProyect es un programa de Python que permite a los fanáticos de Star Wars explorar y gestionar información sobre el universo de Star Wars usando la API SWAPI. Este manual te guiará a través de las principales funcionalidades de la aplicación y cómo utilizarlas.

Requisitos
Antes de empezar, asegúrate de tener:

Python 3.x instalado en tu sistema.

Las librerías necesarias instaladas. Puedes instalar todas las dependencias usando:

bash
Copiar código
pip install -r requirements.txt
Ejecución de la Aplicación
Para ejecutar el programa, abre una terminal y navega al directorio del proyecto, luego ejecuta:

bash
Copiar código
python src/main.py
Verás un menú interactivo que te permitirá seleccionar diferentes opciones.

Funcionalidades y Cómo Usarlas
1. Listar Películas
Selecciona la opción 1 para listar las películas de Star Wars.

Qué se muestra: Título, número del episodio, fecha de lanzamiento, "Opening Crawl", y nombre del director.
Cómo usarlo: El programa imprimirá la lista de películas en la terminal.
2. Listar Especies
Selecciona la opción 2 para ver todas las especies de seres vivos de la saga.

Qué se muestra: Nombre, altura, clasificación, planeta de origen, lengua materna, nombres de los personajes que pertenecen a la especie, y episodios en los que aparecen.
Cómo usarlo: La aplicación imprimirá la lista de especies en la terminal.
3. Listar Planetas
Selecciona la opción 3 para listar los planetas.

Qué se muestra: Nombre, período de órbita, período de rotación, cantidad de habitantes, tipo de clima, episodios en los que aparece, y personajes originarios del planeta.
Cómo usarlo: El programa mostrará la lista de planetas en la terminal y generará un gráfico con la cantidad de personajes nacidos en cada planeta.
4. Buscar Personaje
Selecciona la opción 4 para buscar personajes.

Qué se muestra: Nombre, planeta de origen, títulos de los episodios en los que aparece, género, especie, naves y vehículos que utiliza.
Cómo usarlo: Introduce un nombre o una parte del nombre del personaje que deseas buscar. La aplicación mostrará una lista de personajes que coinciden con la búsqueda.
5. Crear Misión
Selecciona la opción 5 para crear una misión.

Qué se solicita: Nombre de la misión, planeta destino, nave a utilizar, armas (hasta 7) e integrantes de la misión (hasta 7).
Cómo usarlo: Ingresa los detalles solicitados. La misión será creada y mostrada en la terminal.
6. Guardar Misiones
Selecciona la opción 6 para guardar las misiones en un archivo de texto.

Qué se hace: Las misiones actuales se guardarán en un archivo missions.txt.
Cómo usarlo: Asegúrate de que las misiones están bien definidas antes de guardar.
7. Cargar Misiones
Selecciona la opción 7 para cargar misiones desde un archivo de texto.

Qué se hace: Carga las misiones desde el archivo missions.txt.
Cómo usarlo: Asegúrate de que el archivo missions.txt existe y contiene misiones en el formato correcto.
8. Salir
Selecciona la opción 8 para salir del programa.

Qué se hace: Termina la ejecución del programa.
Ejemplos de Uso
Listar Películas
Selecciona la opción 1.
Revisa la lista de películas que aparece en la terminal.
Buscar Personaje
Selecciona la opción 4.
Introduce un fragmento del nombre del personaje, por ejemplo, "Luke".
Revisa la lista de personajes que coinciden con tu búsqueda.
Crear Misión
Selecciona la opción 5.
Ingresa el nombre de la misión, planeta destino, nave, armas e integrantes cuando se te solicite.
La misión creada se mostrará en la terminal.
Consejos Adicionales
Verifica los Datos: Asegúrate de que los datos introducidos para las misiones son válidos y están en el formato correcto.
Guardar Regularmente: Guarda tus misiones frecuentemente para evitar la pérdida de datos.
Revisa los Gráficos: Utiliza los gráficos generados para obtener una visión visual de las estadísticas y características de Star Wars.
