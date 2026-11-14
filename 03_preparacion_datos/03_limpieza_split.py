import pandas as pd

# Cargar el archivo CSV
ruta_archivo = "Datos/Datos Crudos/drybean_raw.csv"
df = pd.read_csv(ruta_archivo)

print("Dataset cargado")
print("Dimensiones:", df.shape)
