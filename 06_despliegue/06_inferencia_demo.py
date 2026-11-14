## Despliegue en la Nube (Streamlit)

El modelo de clasificación multiclase (**XGBoost**) se encuentra desplegado y operativo en la web mediante **Streamlit Community Cloud**, conectado directamente a este repositorio mediante integración continua.

* **Enlace a la aplicación en vivo:** [Abrir Clasificador Dry Bean](https://drybeanml-git.streamlit.app/)
* **Archivo principal de ejecución:** `main.py`

### ¿Cómo interactuar con la aplicación?
1. Ingresa al enlace de la aplicación web.
2. En el panel lateral izquierdo (**Parámetros del Grano**), ajusta los valores morfológicos y geométricos de la semilla (Área, Perímetro, Eje Mayor, Eje Menor, etc.).
3. Haz clic en el botón **Clasificar Variedad** para obtener en tiempo real la predicción entre las siete clases registradas (*Seker, Barbunya, Bombay, Cali, Dermosan, Horoz* y *Sira*).
