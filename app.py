import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Configuración de la página: layout ancho para aprovechar toda la pantalla
# (debe ser el primer comando de Streamlit del archivo)
st.set_page_config(page_title='Explorador de Coches', layout='wide')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# ============================================================
# ENCABEZADO
# ============================================================
st.header('🚗 Explorador de Anuncios de Venta de Coches')
st.write(
    'Esta aplicación permite explorar de forma interactiva el conjunto de datos '
    'de anuncios de venta de vehículos usados en Estados Unidos.'
)

# ============================================================
# LAYOUT PRINCIPAL: 45% | 10% (espaciador) | 45%
# ============================================================
col_izq, col_espacio, col_der = st.columns([45, 10, 45])

# ------------------------------------------------------------
# COLUMNA IZQUIERDA — Histograma de precios
# ------------------------------------------------------------
with col_izq:
    st.subheader('Distribución de precios')
    st.markdown(
        '*Este histograma muestra cuántos anuncios hay en cada nivel de precio. '
        'Usa los controles de abajo para explorar distintos rangos y ver cómo '
        'cambia la distribución dentro de cada uno.*'
    )

    rangos_precio = {
        'US$0 - US$10,000': (0, 10000),
        'US$10,000 - US$25,000': (10000, 25000),
        'US$25,000 - US$50,000': (25000, 50000),
        'Más de US$50,000': (50000, car_data['price'].max()),
    }

    if 'rango_seleccionado' not in st.session_state:
        st.session_state.rango_seleccionado = 'US$0 - US$10,000'

    rango_seleccionado = st.radio(
        'Rango de precio:',
        options=list(rangos_precio.keys()),
        key='rango_seleccionado',
        horizontal=True
    )

    rango = rangos_precio[rango_seleccionado]
    datos_precio_filtrados = car_data[(car_data['price'] >= rango[0]) & (car_data['price'] <= rango[1])]

    fig_hist = go.Figure(data=[go.Histogram(x=datos_precio_filtrados['price'], nbinsx=50)])
    fig_hist.update_layout(
        title_text=f'Distribución del Precio — {rango_seleccionado}',
        xaxis_title='Precio (USD)',
        yaxis_title='Cantidad de anuncios'
    )
    fig_hist.update_xaxes(range=[rango[0], rango[1]])

    st.plotly_chart(fig_hist, use_container_width=True)
    st.caption(f'Anuncios mostrados: {len(datos_precio_filtrados):,} de {len(car_data):,} totales')

    if st.button('🔄 Restablecer vista', key='reset_precio'):
        st.session_state.rango_seleccionado = 'US$0 - US$10,000'
        st.rerun()

# ------------------------------------------------------------
# COLUMNA DERECHA — Gráfico de dispersión
# ------------------------------------------------------------
with col_der:
    st.subheader('Año del modelo vs. Precio')
    st.markdown(
        '*Este gráfico muestra la relación entre el año del modelo y el precio de '
        'venta de cada anuncio. Activa o desactiva décadas para enfocarte en un '
        'período específico y observar cómo varía el precio según la antigüedad.*'
    )

    car_data_reciente = car_data[(car_data['model_year'] >= 1960) & (car_data['model_year'] <= 2020)]

    decadas = {
        '1960s': (1960, 1969),
        '1970s': (1970, 1979),
        '1980s': (1980, 1989),
        '1990s': (1990, 1999),
        '2000s': (2000, 2009),
        '2010-2020': (2010, 2020),
    }

    for nombre_decada in decadas:
        key_decada = f'decada_{nombre_decada}'
        if key_decada not in st.session_state:
            st.session_state[key_decada] = True

    decadas_activas = [d for d in decadas if st.session_state.get(f'decada_{d}', True)]

    if decadas_activas:
        mascara = pd.Series(False, index=car_data_reciente.index)
        for nombre_decada in decadas_activas:
            inicio, fin = decadas[nombre_decada]
            mascara |= (car_data_reciente['model_year'] >= inicio) & (car_data_reciente['model_year'] <= fin)
        datos_scatter_filtrados = car_data_reciente[mascara]
    else:
        datos_scatter_filtrados = car_data_reciente.iloc[0:0]

    titulo_decadas = ', '.join(decadas_activas) if decadas_activas else 'ninguna década seleccionada'

    fig_scatter = px.scatter(
        datos_scatter_filtrados,
        x='model_year',
        y='price',
        title=f'Año del Modelo vs. Precio — {titulo_decadas}',
        labels={'model_year': 'Año del Modelo', 'price': 'Precio (USD)'},
        opacity=0.4
    )
    fig_scatter.update_yaxes(type='log')
    fig_scatter.update_xaxes(range=[1960, 2020])

    if decadas_activas:
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.caption(f'Anuncios mostrados: {len(datos_scatter_filtrados):,} de {len(car_data_reciente):,} en el rango 1960-2020')
    else:
        st.warning('Selecciona al menos una década para mostrar el gráfico.')

    st.write('Décadas a mostrar:')
    fila1 = st.columns(3)
    fila2 = st.columns(3)
    columnas_decadas = fila1 + fila2

    for col, nombre_decada in zip(columnas_decadas, decadas):
        with col:
            st.checkbox(nombre_decada, key=f'decada_{nombre_decada}')

    if st.button('🔄 Restablecer vista', key='reset_decadas'):
        for nombre_decada in decadas:
            st.session_state[f'decada_{nombre_decada}'] = True
        st.rerun()