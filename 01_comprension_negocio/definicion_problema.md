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

## 4. Fuente de Datos
* **Dataset:** Dry Bean Dataset (UCI Machine Learning Repository, ID: 602). https://archive.ics.uci.edu/dataset/602/dry+bean+dataset
* **Volumen:** 13,611 instancias, 16 variables predictoras numéricas y 1 variable objetivo categórica (`Class` con 7 clases).

## 5. Organización del Equipo 

* **Ingeniero de Datos:** Se encargo de todo le tratamiento de la data./ Erica Rocio Marquez
* **Cientifico de Datos** se encarga del modelado / David Antolinez
* **Ing DevOps:** Se encarga de la infraestructura y despliegue de la solucion/ John Carmona
* **Producto Owner:** Se encarga de coordinar los equipos de trabajo / John Carmona
