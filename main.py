import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import os


load_dotenv()

conexion_db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Extracción de datos
consulta = "SELECT * FROM EmployeePerformance"
df = pd.read_sql(consulta, conexion_db)

# Estadísticas por departamento
estadisticas = df.groupby('department').agg({
    'performance_score': ['mean', 'median', 'std'],
    'salary': ['mean', 'median', 'std'],
    'employee_id': 'count'
})
print(estadisticas)

# Correlaciones
correlacion1 = df['years_with_company'].corr(df['performance_score'])
correlacion2 = df['salary'].corr(df['performance_score'])
print(f"Correlación entre años con la empresa y puntaje de rendimiento: {correlacion1}")
print(f"Correlación entre salario y puntaje de rendimiento: {correlacion2}")

departamentos = df['department'].unique()

for departamento in departamentos:
    df_departamento = df[df['department'] == departamento]
    
    # Histograma del puntaje de rendimiento
    plt.figure()
    df_departamento['performance_score'].hist()
    plt.title(f"Histograma del puntaje de rendimiento - {departamento}")
    plt.xlabel("Puntaje de rendimiento")
    plt.ylabel("Frecuencia")
    plt.show()

# graficos de dispercion
#  años con la empresa  vs puntaje de rendimiento
plt.figure()
plt.scatter(df['years_with_company'], df['performance_score'])
z = np.polyfit(df['years_with_company'], df['performance_score'], 1)
p = np.poly1d(z)
plt.plot(df['years_with_company'], p(df['years_with_company']), "r--")

plt.title("Años con la empresa vs. Puntaje de rendimiento")
plt.xlabel("Años con la empresa")
plt.ylabel("Puntaje de rendimiento")
plt.show()

# salario vs puntaje de rendimiento
plt.figure()
plt.scatter(df['salary'], df['performance_score'])
z = np.polyfit(df['salary'], df['performance_score'], 1)
p = np.poly1d(z)
plt.plot(df['salary'], p(df['salary']), "r--")
plt.title("Salario vs. Puntaje de rendimiento")
plt.xlabel("Salario")
plt.ylabel("Puntaje de rendimiento")
plt.show()
