# Advanced Data Analysis
## Requisitos

- MySQL
- Entorno virtual (`venv`)
- Paquetes de Python requeridos (ver [Instalación](#instalación))

## Estructura del Proyecto
- **main.py**: El script principal que realiza la extracción, análisis y visualización de los datos.
- **.env**: Archivo de configuración que contiene las credenciales para la conexión a la base de datos
- **requirements.txt**: Lista de las dependencias de Python necesarias para ejecutar el proyecto.

## Instalación

### 1. Clonar el repositorio


### 2. Crear y activar un entorno virtual

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

En macOS y Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar el archivo `.env`

Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido, ajustando los valores según tus credenciales de MySQL:

```plaintext
DB_HOST= localhost
DB_USER=tu usuario
DB_PASSWORD=tu contraseña
DB_NAME= CompanyData
```

## Uso

1. Asegúrate de tener la base de datos `CompanyData` creada en MySQL y la tabla `EmployeePerformance` poblada con datos ficticios.
   
2. Ejecuta el script principal para realizar el análisis y generar las visualizaciones:

```bash
python main.py
```

3. Se generarán varias estadísticas y gráficos, incluyendo histogramas de rendimiento por departamento y gráficos de dispersión con líneas de tendencia para explorar la relación entre años con la empresa, salario y rendimiento.
