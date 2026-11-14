import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Clasificador de Dry Bean",
    page_icon="🫘",
    layout="centered",
)

st.title("🫘 Clasificador de Variedades de Frijol Seco (Dry Bean)")
st.markdown(
    "Esta aplicación utiliza un modelo de Machine Learning (**XGBoost**) para clasificar la variedad del grano basándose en sus **16 características físicas y geométricas**."
)

st.sidebar.header("Parámetros del Grano (16 Features)")


# Función para capturar las 16 características exactas del dataset
def user_input_features():
    area = st.sidebar.number_input("Area", min_value=20000, max_value=260000, value=28395)
    perimeter = st.sidebar.number_input("Perimeter", min_value=500.0, max_value=2000.0, value=610.29)
    major_axis = st.sidebar.number_input("MajorAxisLength", min_value=180.0, max_value=750.0, value=208.17)
    minor_axis = st.sidebar.number_input("MinorAxisLength", min_value=120.0, max_value=470.0, value=173.88)
    aspect_ratio = st.sidebar.number_input("AspectRatio", min_value=1.0, max_value=3.0, value=1.19)
    eccentricity = st.sidebar.number_input("Eccentricity", min_value=0.2, max_value=1.0, value=0.55)
    convex_area = st.sidebar.number_input("ConvexArea", min_value=20000, max_value=270000, value=28715)
    equiv_diameter = st.sidebar.number_input("EquivDiameter", min_value=150.0, max_value=600.0, value=190.14)
    extent = st.sidebar.number_input("Extent", min_value=0.5, max_value=0.9, value=0.76)
    solidity = st.sidebar.number_input("Solidity", min_value=0.9, max_value=1.0, value=0.99)
    roundness = st.sidebar.number_input("Roundness", min_value=0.4, max_value=1.0, value=0.96)
    compactness = st.sidebar.number_input("Compactness", min_value=0.6, max_value=1.0, value=0.91)
    shape_factor_1 = st.sidebar.number_input("ShapeFactor1", min_value=0.002, max_value=0.012, value=0.0073, format="%.4f")
    shape_factor_2 = st.sidebar.number_input("ShapeFactor2", min_value=0.0005, max_value=0.004, value=0.0031, format="%.4f")
    shape_factor_3 = st.sidebar.number_input("ShapeFactor3", min_value=0.4, max_value=1.0, value=0.8342, format="%.4f")
    shape_factor_4 = st.sidebar.number_input("ShapeFactor4", min_value=0.9, max_value=1.0, value=0.9987, format="%.4f")

    data = {
        "Area": area,
        "Perimeter": perimeter,
        "MajorAxisLength": major_axis,
        "MinorAxisLength": minor_axis,
        "AspectRatio": aspect_ratio,
        "Eccentricity": eccentricity,
        "ConvexArea": convex_area,
        "EquivDiameter": equiv_diameter,
        "Extent": extent,
        "Solidity": solidity,
        "Roundness": roundness,
        "Compactness": compactness,
        "ShapeFactor1": shape_factor_1,
        "ShapeFactor2": shape_factor_2,
        "ShapeFactor3": shape_factor_3,
        "ShapeFactor4": shape_factor_4,
    }
    return pd.DataFrame(data, index=[0])


df_input = user_input_features()

st.subheader("📊 Datos ingresados del grano:")
st.write(df_input)

# Botón de predicción conectado al archivo .pkl
if st.button("Clasificar Variedad"):

    ruta_modelo = "04_modelado/modelo_xgboost.pkl"
    ruta_encoder = "Datos/Datos Limpios/labelencoder.joblib"

    if os.path.exists(ruta_modelo):
        try:
            # Cargar modelo
            model = joblib.load(ruta_modelo)

            # Realizar predicción
            prediccion = model.predict(df_input)
            clase_id = int(prediccion[0])

            # Traducir el índice (0-6) al nombre real de la variedad
            if os.path.exists(ruta_encoder):
                le = joblib.load(ruta_encoder)
                nombre_variedad = le.inverse_transform([clase_id])[0]
            else:
                clases = ["BARBUNYA", "BOMBAY", "CALI", "DERMASON", "HOROZ", "SEKER", "SIRA"]
                nombre_variedad = clases[clase_id]

            # Mostrar resultado
            st.success(
                f"🎉 La variedad predicha para el frijol es: **{str(nombre_variedad).upper()}** (Clase {clase_id})"
            )

        except ModuleNotFoundError as e:
            st.error(f"No se encuentra esta librería: {e.name}")
            st.exception(e)

        except Exception as e:
            st.error(f"Error al cargar o ejecutar el modelo: {e}")
            st.exception(e)

    else:
        st.error(
            "⚠️ No se encontró el archivo `modelo_xgboost.pkl` en la carpeta `04_modelado`."
        )
