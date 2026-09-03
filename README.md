# 🚗 Explorador de Anuncios de Venta de Coches

Aplicación web interactiva construida con [Streamlit](https://streamlit.io/) para explorar un conjunto de datos de anuncios de venta de vehículos usados en Estados Unidos.

## ¿Qué hace esta app?

La aplicación permite visualizar de forma interactiva la distribución de precios, kilometraje y otras características de los vehículos anunciados, mediante gráficos generados con Plotly directamente desde el navegador — sin necesidad de escribir código.

## Funcionalidad

- 📊 **Histograma interactivo**: visualiza la distribución de una variable numérica del dataset (por ejemplo, el kilometraje del odómetro).
- 🔵 **Gráfico de dispersión interactivo**: explora la relación entre dos variables del dataset.
- ✅ Controles simples (casillas de verificación) para activar cada visualización bajo demanda.

## Datos

El proyecto utiliza `vehicles_us.csv`, un conjunto de datos de anuncios de venta de vehículos con información sobre precio, año del modelo, kilometraje, condición, tipo de combustible, transmisión, y más.

## Cómo ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Aplicación desplegada

🔗 *(pendiente — se agregará el enlace una vez completado el despliegue en Render)*

## Análisis exploratorio

El notebook `notebooks/EDA.ipynb` contiene el análisis exploratorio de datos previo al desarrollo de la aplicación.