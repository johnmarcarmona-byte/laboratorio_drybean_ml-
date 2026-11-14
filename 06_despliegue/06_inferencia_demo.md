# Fase 6: Despliegue del Modelo (CRISP-DM)

## Arquitectura de Despliegue
Para poner el modelo a disposición de los usuarios finales sin requerir configuración local de Python, se implementó la siguiente arquitectura:

* **Control de Versiones:** Repositorio alojado en GitHub (`laboratorio_drybean_ml-`).
* **Interfaz Gráfica:** Desarrollada en Python utilizando la librería **Streamlit** (`main.py`), permitiendo la captura interactiva de las variables predictoras.
* **Gestión de Dependencias:** Definidas en `requirements.txt` para garantizar la reproducibilidad del entorno en el servidor.
* **Servidor en la Nube:** **Streamlit Community Cloud**, configurado para desplegar automáticamente cualquier actualización realizada en la rama `main`.

## URL de Producción
* **Aplicación Web:** [https://TU-ENLACE-AQUI.streamlit.app](https://drybeanml-git.streamlit.app/)
