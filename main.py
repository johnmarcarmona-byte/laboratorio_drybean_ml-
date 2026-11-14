import streamlit as st
import pandas as pd
import joblib
import os

# Configuración de la página
st.set_page_config(
    page_title="Clasificador de Dry Bean", page_icon="🫘", layout="centered"
)

st.title("🫘 Clasificador de Variedades de Frijol Seco (Dry Bean)")
st.markdown(
    "Esta aplicación utiliza un modelo de Machine Learning (**XGBoost**) para clasificar la variedad del grano basándose en sus características físicas y geométricas."
)

st.sidebar.header("Parámetros del Grano")

# Función para capturar los datos de entrada del usuario
def user_input_features():
    area = st.sidebar.number_input("Area (pixels)", min_value=20000, max_value=260000, value=28395)
    perimeter = st.sidebar.number_input("Perimeter", min_value=500.0, max_value=2000.0, value=610.29)
    major_axis = st.sidebar.number_input("Major Axis Length", min_value=180.0, max_value=750.0, value=208.17)
    minor_axis = st.sidebar.number_input("Minor Axis Length", min_value=120.0, max_value=470.0, value=173.88)
    aspect_ratio = st.sidebar.number_input("Aspect Ratio", min_value=1.0, max_value=3.0, value=1.19)
    convex_area = st.sidebar.number_input("Convex Area", min_value=20000, max_value=270000, value=28715)
    equiv_diameter = st.sidebar.number_input("Equiv Diameter", min_value=150.0, max_value=600.0, value=190.14)
    
    # Diccionario con las variables
    data = {
        "Area": area,
        "Perimeter": perimeter,
        "MajorAxisLength": major_axis,
        "MinorAxisLength": minor_axis,
        "AspectRatio": aspect_ratio,
        "ConvexArea": convex_area,
        "EquivDiameter": equiv_diameter,
    }
    return pd.DataFrame(data, index=[0])

df_input = user_input_features()

st.subheader("📊 Datos ingresados del grano:")
st.write(df_input)

# Botón de predicción conectado al archivo .pkl
if st.button("Clasificar Variedad"):
    # Ruta donde se encuentra tu modelo entrenado (.pkl)
    ruta_modelo = "04_modelado/modelo_xgboost.pkl"
    
    if os.path.exists(ruta_modelo):
        # 1. Cargar el modelo guardado previamente
        model = joblib.load(ruta_modelo)
        
        # 2. Realizar la predicción real
        prediccion = model.predict(df_input)
        
        # 3. Mostrar el resultado en pantalla
        st.success(f"🎉 La variedad predicha para el frijol es: **{prediccion[0]}**")
    else:
        st.error(f"⚠️ No se encontró el archivo del modelo en `{ruta_modelo}`. Entrena y guarda tu modelo primero en esa ruta.")
