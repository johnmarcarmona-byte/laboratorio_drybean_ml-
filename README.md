# Laboratorio de Clasificación de Dry Bean (Metodología CRISP-DM)

Repositorio oficial para el laboratorio de Machine Learning enfocado en la clasificación automatizada de siete variedades de frijoles secos (*Dry Bean*) mediante técnicas de visión por computador y modelos predictivos, estructurado bajo el ciclo de vida **CRISP-DM** (Cross-Industry Standard Process for Data Mining).

Realizado por:
- Ferney David Antolinez Tobo
- John Mario Carmona David
- Erica Rocio Márquez Meneses

---

## ¿Por qué estamos usando la metodología CRISP-DM?

Utilizamos **CRISP-DM** como marco de trabajo estándar de la industria para el desarrollo de proyectos de minería de datos y Machine Learning por las siguientes razones clave:

1. **Enfoque Estructurado y Sistemático:** Divide el proyecto en 6 fases lógicas y secuenciales (Comprensión del negocio, comprensión de datos, preparación, modelado, evaluación y despliegue), evitando saltarse pasos críticos que pueden afectar el rendimiento del modelo.
2. **Alineación con el Problema Real:** Garantiza que el desarrollo técnico de machine learning responda directamente a una necesidad real de clasificación uniforme y automatizada de semillas agrícolas.
3. **Trazabilidad y Reproducibilidad:** Facilita la organización del repositorio en carpetas claras, permitiendo que cualquier evaluador o miembro del equipo audite o replique el flujo de trabajo de principio a fin.
4. **Flexibilidad Iterativa:** Permite retroceder entre fases según sea necesario (por ejemplo, volver a la etapa de preparación de datos si el modelado inicial arroja métricas de error mejorables).

---

## Estructura del Repositorio

El proyecto está organizado siguiendo rigurosamente las fases de la metodología CRISP-DM:

```text
├── 01_comprehension_negocio/    # Fase 1: Comprensión del negocio y objetivos del proyecto.
├── 02_comprehension_datos/      # Fase 2: Recopilación, análisis exploratorio y descripción inicial de los datos.
├── 03_preparacion_datos/        # Fase 3: Limpieza, transformación, ingeniería de características y preprocesamiento.
├── 04_modelado/                 # Fase 4: Selección, entrenamiento y ajuste de hiperparámetros de los modelos.
├── 05_evaluacion/               # Fase 5: Evaluación de resultados frente a los objetivos de negocio y métricas de rendimiento.
├── 06_despliegue/               # Fase 6: Plan de despliegue, documentación y artefactos para producción.
├── src/                         # Código fuente modular (scripts de python reutilizables).
├── .gitignore                   # Archivos y carpetas ignorados por Git.
├── requirements.txt             # Dependencias del proyecto (librerías y versiones).
└── README.md                    # Documentación principal del proyecto.

```
## Descripción del Dataset

| Atributo | Descripción |
| :--- | :--- |
| **Fuente** | UCI Machine Learning Repository - Dry Bean Dataset |
| **Instancias** | 13,611 granos de frijol |
| **Características (Features)** | 16 variables en total (12 dimensiones físicas y 4 formas geométricas extraídas mediante sistemas de visión computacional) |
| **Clases objetivo (Target)** | 7 variedades registradas: Seker, Barbunya, Bombay, Cali, Dermosan, Horoz, Sira |


## Instalación y Configuración
Sigue estos pasos para clonar el repositorio y configurar tu entorno de desarrollo local:

1. Clonar el repositorio: git clone [[https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/johnmarcarmona-byte/laboratorio_drybean_ml-.git))
cd nombre-del-repo
2. Crear y activar un entorno virtual (recomendado):
```text
        python -m venv venv
        # En Windows:
        venv\Scripts\activate
        # En macOS/Linux:
        source venv/bin/activate
```
4. Instalar las dependencias: pip install -r requirements.txt

## Modelado (XGBoost)
Durante la fase de modelado, se implementó y optimizó el algoritmo **XGBoost (Extreme Gradient Boosting)** para llevar a cabo la clasificación multiclase de las siete variedades de frijol seco (*Dry Bean*).

## Modelado (XGBoost)

Durante esta etapa del ciclo CRISP-DM, se implementó y configuró el algoritmo **XGBoost (Extreme Gradient Boosting)** para resolver el problema de clasificación multiclase, permitiendo identificar de forma automatizada las siete variedades de frijol seco (*Dry Bean*).

### Estrategia de Partición de Datos
* **División Estratificada (80/20):** El conjunto de datos se dividió preservando la proporción original de cada clase, destinando un **80% para entrenamiento (10,888 registros)** y un **20% para pruebas (2,723 registros)**. Esto garantiza una evaluación objetiva y sin sesgos de la capacidad de generalización del modelo ante datos no vistos.

### Hiperparámetros del Modelo
Para la configuración inicial del estimador de XGBoost, se establecieron los siguientes parámetros orientados a optimizar el rendimiento y la velocidad de entrenamiento:

| Hiperparámetro | Valor | Descripción |
| :--- | :--- | :--- |
| `n_estimators` | `100` | Cantidad de árboles de decisión generados en el proceso de boosting. |
| `learning_rate` | `0.3` | Tasa de aprendizaje que controla el peso de cada árbol en el resultado final. |
| `max_depth` | `6` | Profundidad máxima permitida en los árboles para controlar la complejidad. |
| `subsample` | `1.0` | Proporción de muestras utilizadas para el entrenamiento de cada árbol. |
| `colsample_bytree` | `1.0` | Proporción de características evaluadas en cada división de los árboles. |

### Justificación técnica
Se seleccionó **XGBoost** debido a su eficiencia superior en el procesamiento de datos tabulares, su manejo integrado de funciones de regularización contra el sobreajuste (*overfitting*) y su alta capacidad para modelar relaciones no lineales complejas entre las 16 características morfológicas y dimensionales extraídas del dataset.
