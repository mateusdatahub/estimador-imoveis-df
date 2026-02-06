import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import json
from pathlib import Path


# Config basica do app
st.set_page_config(
    page_title='Estimador de Preços de Imóveis',
    page_icon='🏡',
    layout='wide'
)

st.title('🏡 Estimador de Preços de Imóveis no DF')
st.write(
    """
    Este aplicativo utiliza um modelo de *Machine Learning* treinado com dados
    imobiliários para estimar o valor de um imóvel com base em suas características
    """
)

st.markdown(
    
    """
    <style>
    .kpi-wrapper {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 14px;
        padding: 1rem;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    }

    /* Light mode */
    @media (prefers-color-scheme: light) {
        .kpi-wrapper {
            background-color: #ffffff;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carregando o modelo e metadados
BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_model():
    model_path = BASE_DIR / 'models' / 'Treinados'/ 'rf_valor_m2_pipeline.joblib'
    return joblib.load(model_path)

@st.cache_data
def load_metadata():
    meta_patch = BASE_DIR / 'models' / 'metadados' / 'rf_valor_metadata.json'
    with open(meta_patch, 'r', encoding='utf-8') as f:
        return json.load(f)

# Extraindo bairros a partir das features do modelo
@st.cache_data
def load_lista_bairros(metadata):
    bairros = [
        f.replace('cat__BAIRRO_TRATADO_', '')
        for f in metadata['features']
        if f.startswith('cat__BAIRRO_TRATADO_')
    ]
    return sorted(bairros)

@st.cache_data
def load_market_data():
    data_path = BASE_DIR / 'data' / 'processed' / 'imoveis_df_eda.csv'
    return pd.read_csv(data_path)

df_market = load_market_data()
df_market = df_market.dropna(subset=['VALOR_M2'])
df_market = df_market.sample(frac=1.0, random_state=42)
model = load_model()
metadata = load_metadata()
lista_bairros = load_lista_bairros(metadata)

st.success('Modelo carregado com sucesso!')

st.subheader('📊 Qualidade do modelo')

# Gereando Kpis
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown('<div class="kpi-wrapper">', unsafe_allow_html=True)
    st.metric(
        label="R² (Teste)",
        value=f"{metadata['r2_test']:.3f}"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with kpi2:
    st.markdown('<div class="kpi-wrapper">', unsafe_allow_html=True)
    st.metric(
        label="MAE",
        value=f"{metadata['mae']:,.2f}"
    )
    st.markdown('</div>', unsafe_allow_html=True)


with kpi3:
    st.markdown('<div class="kpi-wrapper">', unsafe_allow_html=True)
    st.metric(
        label="RMSE",
        value=f"{metadata['rmse']:,.2f}"
    )
    st.markdown('</div>', unsafe_allow_html=True)


st.caption(
    '*Metricas calculadas em conjunto de teste. O modelo utiliza Random Forest com validação cruzada.*'
)

st.subheader('📋 Informe as caracteristicas do imóvel')

# Criando botoes de imput
col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        'Área do imóvel (m²)',
        min_value=20,
        max_value= 1000,
        value=80,
        step=5
    )

    quartos = st.number_input(
        'Numero de quartos',
        min_value=1,
        max_value=10,
        value=2
)

with col2:
    bairro = st.selectbox(
        'Bairro',
        options=lista_bairros

    )

st.divider()

if st.button('🔮 Estimar valor do imóvel'):
    #Criando DataFrame no formato esperado pelo pipeline
    input_data = pd.DataFrame({
        'AREA':[area],
        'QUARTOS':[quartos],
        'BAIRRO_TRATADO':[bairro]
    })

    # Predição ( retorna LOG_VALOR_M2)
    pred_log = model.predict(input_data)[0]

    # Convertendo para escala original (R$ por m²)
    pred_valor_m2 = np.expm1(pred_log)
    valor_total = pred_valor_m2 * area
    
    st.markdown('### 😁 Resultado da estimativa')
    st.success(f'🤑 Valor estimado do m²: **R$ {pred_valor_m2:,.2f}**')
    st.info(f'🏡 Valor estimado do imovel: **R$ {valor_total:,.2f}**')
    
    # Graficozinho basico
    st.subheader('📊 Comparação com o mercado')

    fig = px.histogram(
        df_market,
        x='VALOR_M2',
        nbins=40,
        title='Distribuição do valor do m² no mercado',
        labels={'VALOR_M2': 'Valor do m² (R$)'},
        opacity=0.75
    )

    fig.add_vline(
        x=pred_valor_m2,
        line_width=3,
        line_dash='dash',
        annotation_text='Seu imóvel',
        annotation_position='top right'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Insight simples para usuario comum
    percentil = (df_market['VALOR_M2'] < pred_valor_m2).mean()*100

    st.info(
        f'🚨 Este imóvel está mais caro que aproximadamente **{percentil:.0f}%** dos imóveis do mercado.'
    )