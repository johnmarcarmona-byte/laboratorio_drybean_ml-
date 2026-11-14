# Fase 1: Comprensión del Negocio (Business Understanding)

## 1. Contexto y Problema de Negocio
Una empresa del sector agrícola requiere automatizar la clasificación de granos de frijol seco (*Dry Bean*) para optimizar su proceso de control de calidad. Actualmente, gran parte de esta clasificación se realiza de manera manual, lo cual resulta lento, costoso y propenso a errores humanos por fatiga visual.

## 2. Objetivo del Proyecto
Desarrollar un modelo de Machine Learning de clasificación supervisada capaz de identificar automáticamente la variedad de frijol (`Class`) a partir de 16 características geométricas (área, perímetro, ejes, excentricidad, solidez, entre otras) extraídas mediante visión por computador.

## 3. Criterios de Éxito
* **Criterio de Negocio:** Reducir el tiempo de inspección manual y estandarizar la separación de las 7 variedades de frijol (*Seker, Barbunya, Bombay, Cali, Dermason, Horoz, Sira*).
* **Criterio Técnico (Métricas):**
  * Superar el desempeño de un modelo base (*Baseline* de Regresión Logística).
  * Priorizar la métrica **F1 Macro** sobre el *Accuracy* simple, garantizando un rendimiento equilibrado en todas las variedades de frijol a pesar del desbalance en la cantidad de muestras por clase.
  * Entregar un modelo serializado (`.joblib`) listo para ser consumido de forma reproducible.

## 4. Fuente de Datos
* **Dataset:** Dry Bean Dataset (UCI Machine Learning Repository, ID: 602).
* **Volumen:** 13,611 instancias, 16 variables predictoras numéricas y 1 variable objetivo categórica (`Class` con 7 clases).

## 5. Organización del Equipo (Scrum ML)
* **Product Owner:** Define el valor del modelo, prioriza el backlog y valida las métricas finales.
* **Scrum Master:** Asegura el cumplimiento de CRISP-DM/TDSP, gestiona el repositorio en GitHub y el tablero Kanban.
* **Data Engineer / Analyst:** Ejecuta la descarga, análisis exploratorio, limpieza y partición de los datos (Fases 2 y 3).
* **ML Engineer:** Entrena, evalúa, compara los modelos y prepara el despliegue local (Fases 4, 5 y 6).
