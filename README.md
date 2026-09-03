# 🚗 Explorador de Anuncios de Venta de Coches

Aplicación web interactiva construida con [Streamlit](https://streamlit.io/) para explorar un conjunto de datos de anuncios de venta de vehículos usados en Estados Unidos.

## ¿Qué hace esta app?

La aplicación permite visualizar de forma interactiva la distribución de precios y la relación entre el año del modelo y el precio de los vehículos anunciados, mediante gráficos generados con Plotly directamente desde el navegador — sin necesidad de escribir código.

## Funcionalidad

- 📊 **Histograma de precios**: muestra cuántos anuncios hay en cada nivel de precio, con controles para explorar distintos rangos (US$0-10,000, US$10,000-25,000, US$25,000-50,000 y más de US$50,000).
- 🔵 **Gráfico de dispersión**: relaciona el año del modelo con el precio de venta, con casillas de verificación para activar o desactivar décadas específicas (1960s a 2010-2020) y enfocar el análisis en un período determinado.
- ✅ Controles interactivos (botones y casillas de verificación) para actualizar cada visualización en tiempo real.

## Datos

El proyecto utiliza `vehicles_us.csv`, un conjunto de datos de más de 51,000 anuncios de venta de vehículos con información sobre precio, año del modelo, kilometraje, condición, tipo de combustible, transmisión, y más.

## Aplicación desplegada

🔗 **[https://streamlit-app-sprint7.onrender.com/](https://streamlit-app-sprint7.onrender.com/)**

## Análisis exploratorio

El notebook `notebooks/EDA.ipynb` contiene el análisis exploratorio de datos previo al desarrollo de la aplicación.

## Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) — framework para la aplicación web
- [Plotly](https://plotly.com/python/) — visualizaciones interactivas
- [Pandas](https://pandas.pydata.org/) — manipulación de datos
- [Render](https://render.com/) — despliegue en la nube